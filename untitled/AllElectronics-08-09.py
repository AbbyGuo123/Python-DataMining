import pandas as pd

if __name__=='__main__':
    inputFile = 'D:\ITA\phython\ClassTest\FirstDemo\python\data\data\AllElectronics.csv'
    data = pd.read_csv(inputFile)
    # print(data)
    # data[data is 'youth']=1
    data = data.replace('youth', 1)
    data = data.replace('middle_aged', 2)
    data = data.replace('senior', 3)
    data = data.replace('low', 1)
    data = data.replace('medium', 2)
    data = data.replace('high', 3)
    data = data.replace('no', 0)
    data = data.replace('yes', 1)
    data = data.replace('fair', 0)
    data = data.replace('excellent', 1)
    print(data)
    p = 0.8
    train_data = data.values[:int(len(data)*p), :]
    test_data = data.values[int(len(data) * p):, :]
    print(data)
    #p=0.8
    #train_data = data[:int(len(data)*p),:]
    #test_data = data[int(len(data)*p):,:]
    x = train_data[:,:4]
    y = train_data[:,4]
    test_x = test_data[:,:4]
    test_y = test_data[:,4]

    from sklearn.tree import DecisionTreeClassifier as DTC
    from sklearn.cluster import KMeans
    dtc = DTC()
    dtc.fit(x,y)
    print(dtc.score(test_x,test_y))
    data = (data - data.mean(axis = 0))/(data.std(axis = 0))
    k=3
    kmodel = KMeans(n_clusters = k, n_jobs = 4)
    kmodel.fit(data)
    print(kmodel.cluster_centers_)
    print(kmodel.labels_)






