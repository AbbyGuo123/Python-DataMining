import pandas as pd

inputfile='D:\ITA\phython\ClassTest\FirstDemo\python\data\data\\bankloan.xls'
data = pd.read_excel(inputfile,'bankloan')

# data1 = data.drop(u'地址',axis=1).values
data1 = data.drop(u'教育',axis=1).values
data1 =data.values
p=0.8
data2 = data1[:int(len(data1)*p),:]
testdata = data1[int(len(data1)*p):,:]

x = data2[:,:8].astype(int)
y = data2[:,8].astype(int)

test_x = testdata[:,:8].astype(int)
test_y = testdata[:,8].astype(int)


from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB

bayes = GaussianNB()
bayes.fit(x,y)
print('高斯贝叶斯\n')
print(bayes.score(test_x,test_y))

bayes = BernoulliNB()
bayes.fit(x,y)
print('伯努利贝叶斯\n')
print(bayes.score(test_x,test_y))

bayes = MultinomialNB()
bayes.fit(x,y)
print('多项式贝叶斯\n')
print(bayes.score(test_x,test_y))

from sklearn.ensemble import RandomForestClassifier
randomForest = RandomForestClassifier()
randomForest.fit(x,y)
print('随机森林')
print(randomForest.score(test_x,test_y))
print(randomForest.feature_importances_)

from sklearn.tree import DecisionTreeClassifier as DTC
dtc= DTC()
dtc.fit(x,y)
print('决策树')
print(dtc.score(test_x,test_y))


from sklearn.linear_model import LogisticRegression
LR = LogisticRegression()
LR.fit(x,y)
print(LR.score(test_x,test_y))



print(data1)

