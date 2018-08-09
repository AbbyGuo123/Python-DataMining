#导入数据
import pandas as pd

inputfile = 'D:\ITA\phython\ClassTest\FirstDemo\python\data\data\missing_data.xls'
data = pd.read_excel(inputfile,'Sheet1',header=None)

#
from scipy.interpolate import lagrange #导入拉格朗日插值函数
#数据填充
outputfile = 'D:\ITA\phython\ClassTest\FirstDemo\python\data\data\missing_data_out.xls'
#
# def fill_na_data(s,n,k=5):
#     y=s[list(range(n-k,n))+list(range(n+1,n+1+k))]#取数
#     y=y[y.notnull()]#剔除空值
#     return lagrange(y.index,list(y))(n) #插值并返回插值结果
# for i in data.columns:
#   for j in range(len(data)):
#     if (data[i].isnull())[j]: #如果为空即插值。
#       data[i][j] = fill_na_data(data[i], j)
#
data.to_excel(outputfile, header=None, index=False) #输出结果



# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Wed Aug  8 13:20:32 2018
# @author: apple
# """
# # #数据读取
# import pandas as pd
# # inputFile = 'D:\ITA\phython\ClassTest\FirstDemo\python\data\data\missing_data.xls'
# # data = pd.read_excel(inputFile,'Sheet1',header=None)
# # #数据填充
# # outputfile = 'D:\ITA\phython\ClassTest\FirstDemo\python\data\data\missing_data_process.xls'
# #
# # from scipy.interpolate import lagrange
# #
# # def fill_na_data(s,n,k=5):
# #     y = s[list(range(n-k,n))+list(range(n+1,n+1+k))]
# #     y = y[y.notnull()]
# #     return lagrange(y.index,list(y))(n)
# #
# # for i in data.columns:
# #   for j in range(len(data)):
# #     if (data[i].isnull())[j]: #如果为空即插值。
# #       data[i][j] = fill_na_data(data[i], j)
# #
# # data.to_excel(outputfile, header=None, index=False) #输出结果
#
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.naive_bayes import GaussianNB
# from sklearn.naive_bayes import BernoulliNB
# inputFile2 = 'D:\ITA\phython\ClassTest\FirstDemo\python\data\data\model.xls'
# data = pd.read_excel(inputFile2,'Sheet1')
# #
# # inputFile3 = 'D:\ITA\phython\ClassTest\FirstDemo\python\data\data\model_test_1.xlsx'
# # data_tset = pd.(inputFile3,'Sheet1',index_col=u'电量趋势下降指标')
# #
# data = data.values
# #
# p=0.8
# train = data[:int(len(data)*p),:]
# test = data[int(len(data)*p):,:]
# print(data)
# #
# x=data[:,:3].astype(int)
#
# y=data[:,3].astype(int)
# #
# # test_x=test[:,:3].astype(int)
# #
# # test_y=test[:,3].astype(int)
# #
# # bayes = MultinomialNB();
# # bayes.fit(x,y)
# # print(bayes.score(test_x,test_y))
#
# bayes = GaussianNB();
# bayes.fit(x,y)
# print(bayes.score(x,y))
#
#
#
#
# # !/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # #数据读取
# # import pandas as pd
# # inputFile = 'D:\ITA\phython\ClassTest\FirstDemo\python\data\data\missing_data.xls'
# # data = pd.read_excel(inputFile,'Sheet1',header=None)
# # #数据填充
# # outputfile = 'D:\ITA\phython\ClassTest\FirstDemo\python\data\data\missing_data_out.xls'
# #
# # from scipy.interpolate import lagrange
# #
# # def fill_na_data(s,n,k=5):
# #     y = s[list(range(n-k,n))+list(range(n+1,n+1+k))]
# #     y = y[y.notnull()]
# #     return lagrange(y.index,list(y))(n)
# #
# # for i in data.columns:
# #   for j in range(len(data)):
# #     if (data[i].isnull())[j]: #如果为空即插值。
# #       data[i][j] = fill_na_data(data[i], j)
# #
# # data.to_excel(outputfile, header=None, index=False) #输出结果
# #
#
#
#
# from sklearn.ensemble import RandomForestClassifier
# randomForest= RandomForestClassifier()
# randomForest.fit(x,y)
# print(randomForest.score(x,y))
# print(randomForest.feature_importances_)
#
#
# from sklearn.ensemble import AdaBoostClassifier
# adaBoost = AdaBoostClassifier()
# adaBoost.fit(x,y)
# print(adaBoost.score(x,y))
#
# from sklearn.linear_model import LogisticRegression
# lr = LogisticRegression(max_iter=10)
# lr.fit(x,y)
# print(lr.score(x,y))
