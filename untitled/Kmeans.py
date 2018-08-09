# import pandas as pd
#
# inputFile = 'D:\ITA\phython\ClassTest\FirstDemo\python\data\data\\air_data.csv'
# data = pd.read_csv(inputFile,encoding='utf-8')
# print(data.head(5))
#
#
# explore=data.describe().T
# explore['null']= len(data)-explore['count']
# explore = explore[['null','max','min']]
# explore.columns=[u'空值数',u'最大值',u'最小值']
#
# # print(explore)
#
#
# data = data[data['SUM_YR_1'].notnull()&data['SUM_YR_2'].notnull()]
#
# index1 = data['SUM_YR_1']!=0
# index2 = data['SUM_YR_2']!=0
# index3 = (data['SUM_YR_1']==0) & (data['SUM_YR_2']==0)
# data = data[index1|index2|index3]
# print(data)

if __name__=='__main__':

    import pandas as pd

    inputFile = 'D:\ITA\phython\ClassTest\FirstDemo\python\data\data\zscoredata.xls'

    data = pd.read_excel(inputFile,'Sheet1')
    print(data)
    from sklearn.cluster import KMeans
    data = (data - data.mean(axis = 0))/(data.std(axis = 0))
    k=3
    kmodel = KMeans(n_clusters = k, n_jobs = 4)
    kmodel.fit(data)
    print(kmodel.cluster_centers_)
    print(kmodel.labels_)