from sklearn import datasets

iris = datasets.load_iris()
print(iris.data.shape)

# from sklearn import svm
#
# clf = svm.LinearSVC()
# clf.fit(iris.data, iris.target)
# print(type(iris))
#
# print(iris.target)
# print(clf.predict([[5.0, 3.6, 1.3, 0.25]]))
#

from sklearn.tree import DecisionTreeClassifier as DTC
dtc=DTC()
# dtc.fit(iris.data,iris.target)
# print(dtc.predict(iris.data))

import pandas as pd
inputfile = 'D:\ITA\phython\ClassTest\FirstDemo\python\data\data\sales_data.xls'
data = pd.read_excel(inputfile,'sales_data',index_col = u'序号')

data[data==u'好']=1
data[data==u'是']=1
data[data==u'高']=1

data[data!=1]=-1

x=data.iloc[:,:3].as_matrix().astype(int)
# print(x)
y=data.iloc[:,3].as_matrix().astype(int)
# print(y)
# print(type(data))

dtc.fit(x,y)
# dtc.predict(x)
print(dtc.score(x,y))
# print(data)

inputfile = 'D:\ITA\phython\ClassTest\FirstDemo\python\data\data\sales_test.xlsx'
data = pd.read_excel(inputfile,'Sheet1',index_col = u'序号')

data[data==u'好']=1
data[data==u'是']=1
data[data==u'高']=1

data[data!=1]=-1

x=data.iloc[:,:3].as_matrix().astype(int)
# print(x)
y=data.iloc[:,3].as_matrix().astype(int)
# print(y)
# print(type(data))

dtc.fit(x,y)
# dtc.predict(x)
print(dtc.score(x,y))


# from sklearn import grid_search
# parameters = {'criterion':('entropy', 'gini'), 'max_depth':[1, 10]}
# clf = grid_search.GridSearchCV(dtc, parameters)
# print(clf.best_params_)

from sklearn import grid_search
parameters = {'criterion':('entropy','gini'),'max_depth':[1,10]}

clf=grid_search.GridSearchCV(dtc,parameters)
clf.fit(x,y)
print(clf.best_params_)


dtc1 = DTC(criterion='entropy',max_depth=20,max_features=1)
dtc1.fit(x,y)
print(dtc1.score(x,y))