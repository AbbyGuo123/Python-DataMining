if __name__=='__main__':

    import pandas as pd

    inputFile = 'D:\ITA\phython\ClassTest\FirstDemo\python\data\data\\bankloan.xls'

    data = pd.read_excel(inputFile,'bankloan')
    data = data[[ u'工龄',u'年龄',u'教育']]
    print(data)
    from sklearn.cluster import KMeans
    data = (data - data.mean(axis = 0))/(data.std(axis = 0))
    k=3
    kmodel = KMeans(n_clusters = k, n_jobs = 4)
    kmodel.fit(data)
    print(kmodel.cluster_centers_)
    print(kmodel.labels_)