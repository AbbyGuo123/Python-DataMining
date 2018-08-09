import pandas as pd

inputfile='D:\ITA\phython\ClassTest\FirstDemo\python\data\data\\bankloan.xls'

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

def get_data(file_name,x_column):

    data = pd.read_excel(file_name)
    print(data)
    X_parameter = []
    Y_parameter = []
    for single_work, single_price_value in zip(data[x_column], data[u'收入']):
        X_parameter.append([float(single_work)])
        Y_parameter.append(float(single_price_value))

    return X_parameter, Y_parameter



def linear_model_main(X_parameter,Y_parameter,predict_square_feet):
    regr =LinearRegression()
    regr.fit(X_parameter,Y_parameter)
    y=regr.predict(X_parameter)
    predict_outcome=regr.predict(predict_square_feet)
    predictions={}
    predictions['intercept']=regr.intercept_
    predictions['coefficient']=regr.coef_
    predictions['predict_value']=predict_outcome
    print(mean_squared_error(Y_parameter,y))
    print(r2_score(Y_parameter,y))
    return predictions


def show_linear_line(X_parameter, Y_parameter):
    # 1. 构造回归对象
    regr = LinearRegression()
    regr.fit(X_parameter, Y_parameter)

    # 2. 绘出已知数据散点图
    plt.scatter(X_parameter, Y_parameter, color='blue')

    # 3. 绘出预测直线
    plt.plot(X_parameter, regr.predict(X_parameter), color='red', linewidth=4)
    plt.title('Predict the house price')
    plt.xlabel(u'工龄')
    plt.ylabel(u'收入')
    plt.show()




def main(x_column):
    # 1. 读取数据
    X,Y = get_data(inputfile,x_column)
    # 2. 获取预测值，在这里我们预测700平方英尺大小的房子的房价
    predict_square_feet = 70
    result = linear_model_main(X,Y,predict_square_feet)
    for key,value in result.items():
        print(key,value)
    # 3. 绘图
    show_linear_line(X,Y)





if __name__ == '__main__':
    main(u'工龄')
    main(u'年龄')
    main(u'教育')