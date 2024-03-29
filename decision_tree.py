import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

puredata=np.loadtxt('new_dataset.txt',delimiter=',')
X=puredata[:,:15]
Y=[]

for x in puredata:
    Y.append(x[15])

print "Dataset Lenght:: ", len(puredata)
print "Dataset Shape:: ", puredata.shape

X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)

clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100,
                               max_depth=3, min_samples_leaf=5)
clf_gini.fit(X_train, y_train)

DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=3,
            max_features=None, max_leaf_nodes=None, min_samples_leaf=5,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            presort=False, random_state=100, splitter='best')

clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
 max_depth=3, min_samples_leaf=5)
clf_entropy.fit(X_train, y_train)

DecisionTreeClassifier(class_weight=None, criterion='entropy', max_depth=3,
            max_features=None, max_leaf_nodes=None, min_samples_leaf=5,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            presort=False, random_state=100, splitter='best')

y_pred = clf_gini.predict(X_test)
#y_pred

y_pred_en = clf_entropy.predict(X_test)
#y_pred_en

print "Accuracy is ", accuracy_score(y_test, y_pred) * 100
print "Accuracy is ", accuracy_score(y_test,y_pred_en)*100