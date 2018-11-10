import numpy as np
from sklearn import neighbors
from sklearn.metrics import confusion_matrix

puredata=np.loadtxt('new_dataset.txt',delimiter=',')
X=puredata[:,:15]
Y=[]

for x in puredata:
    Y.append(x[15])

clf=neighbors.KNeighborsClassifier()
clf.fit(X,Y)
pred=clf.predict(X)
cm=confusion_matrix(Y,pred)

#print cm

tp=cm[0][0]
fp=cm[0][1]
fn=cm[1][0]
tn=cm[1][1]

accuracy=round(float(tp+tn)/float(tp+tn+fp+fn),4)
tnr=round(float(tn)/float(tn+fp),4)
tpr=round(float(tp)/float(tp+fn),4)

print "Accuracy : ",accuracy
print "True Negative : ",tnr
print "True Positive : ",tpr