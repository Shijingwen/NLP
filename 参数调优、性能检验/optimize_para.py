#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC
import jieba
import jieba.analyse
import cPickle as pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets.base import Bunch
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
print(__doc__)

count_error = 0
def Update():
    count_error = 2
    if count_error >1:
        f1 = open('data/New_Error.txt')
        f2 = open('data/labelMessage.txt','a')
        for line in f1.readlines():
            f2.write(line)
            #Update();
        f1.close()
        f2.close()
    print ("Update model successful!")
    return

def readbunchobj(path):
    file_obj = open(path, "rb")
    bunch = pickle.load(file_obj)
    file_obj.close()
    return bunch


def get_stop_words():
    result = set()
    for line in open('stopwords.txt', 'r').readlines():
        result.add(line.strip())
    return result

stop_words = get_stop_words()


def writebunchobj(path, bunchobj):
    file_obj = open(path, "wb")
    pickle.dump(bunchobj, file_obj)
    file_obj.close()


def preprocess(path):
    new_table = []
    f = open(path)
    for line in f:
        single_line = line.decode('utf-8', 'ignore').encode('utf-8').split('\t')
        key_words = single_line[1:]
        user_word = ''
        for item in key_words:
            seg_list = jieba.cut(item)
            for check in seg_list:
                if check != ' ':
                    check = check.encode('utf-8')
                    user_word = user_word + ' '+check
        new_item = [single_line[0], user_word]
        new_table.append(new_item)

    bunch = Bunch(label=[], contents=[])
    for k in new_table:
        bunch.label.append(k[0])
        bunch.contents.append(k[1])
    return bunch

data_train = preprocess('data/labelmeaage-100000.txt')
#writebunchobj('seg_train_test2.txt', data_train)
stop_words = get_stop_words()
vectorizer = TfidfVectorizer(max_df=0.5, min_df=3)
content = vectorizer.fit_transform(data_train.contents)
label = data_train.label
from sklearn.feature_selection import SelectKBest, chi2
ch2 = SelectKBest(chi2, k=30000)

#content = ch2.fit_transform(X_train)
from sklearn import svm
from sklearn.calibration import CalibratedClassifierCV
clf_ = svm.LinearSVC()
clf_SVM = CalibratedClassifierCV(clf_)

# Split the dataset in two equal parts
X_train, X_test, y_train, y_test = train_test_split(
    content, label, test_size=0.5, random_state=0)

# Set the parameters by cross-validation
tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                     'C': [0.5,1, 10,100,1000]},
                    {'kernel': ['linear'], 'C': [0.5,1, 10,100,1000]}]

scores = ['precision', 'recall']

for score in scores:
    print("# Tuning hyper-parameters for %s" % score)
    print()

    clf = GridSearchCV(SVC(C=1), tuned_parameters, cv=5,
                       scoring='%s_weighted' % score)
    clf.fit(X_train, y_train)

    print("Best parameters set found on development set:")
    print()
    print(clf.best_params_)
    print()
    print("Grid scores on development set:")
    print()
    for params, mean_score, scores in clf.grid_scores_:
        print("%0.3f (+/-%0.03f) for %r"
              % (mean_score, scores.std() * 2, params))
    print()

    print("Detailed classification report:")
    print()
    print("The model is trained on the full development set.")
    print("The scores are computed on the full evaluation set.")
    print()
    y_true, y_pred = y_test, clf.predict(X_test)
    print(classification_report(y_true, y_pred))
    print()