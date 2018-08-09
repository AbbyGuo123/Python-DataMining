from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB

import pandas as pd

inputfile = 'D:\ITA\phython\ClassTest\FirstDemo\python\data\data\sales_test.xlsx'
data = pd.read_excel(inputfile,'Sheet1',index_col = u'序号')

data[data==u'好']=1
data[data==u'是']=1
data[data==u'高']=1

data[data!=1]=0

x=data.iloc[:,:3].as_matrix().astype(int)
# print(x)
y=data.iloc[:,3].as_matrix().astype(int)

bayes = MultinomialNB()
bayes.fit(x,y)
print(bayes.score(x,y))


bayes = GaussianNB()
bayes.fit(x,y)
print(bayes.score(x,y))

bayes = BernoulliNB()
bayes.fit(x,y)
print(bayes.score(x,y))