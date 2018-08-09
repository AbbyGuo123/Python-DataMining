import pandas as pd

inputfile = 'D:\ITA\phython\ClassTest\FirstDemo\python\data\data\price_info.csv'


import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def get_data(file_name):

    data = pd.read_csv(file_name)
    print(data)
    X_parameter = []
    Y_parameter = []
    for single_square_feet, single_price_value in zip(data['square_feet'], data['price']):
        X_parameter.append([float(single_square_feet)])
        Y_parameter.append(float(single_price_value))

    return X_parameter, Y_parameter



def linear_model_main(X_parameter,Y_parameter,predict_square_feet):
    regr =LinearRegression();
    regr.fit(X_parameter,Y_parameter)
    y=regr.predict(X_parameter)
    from sklearn.externals import joblib

    joblib.dump(regr, 'D:\ITA\phython\ClassTest\FirstDemo\python\data\data\price_info_test')
    # 模型加载
    clf = joblib.load("price_info_test")
    clf.predict()
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
    plt.xlabel('square feet')
    plt.ylabel('price')
    plt.show()




def main():
    # 1. 读取数据
    X,Y = get_data(inputfile)
    # 2. 获取预测值，在这里我们预测700平方英尺大小的房子的房价
    predict_square_feet = 700
    result = linear_model_main(X,Y,predict_square_feet)
    for key,value in result.items():
        print(key,value)
    # 3. 绘图
    show_linear_line(X,Y)




if __name__ == '__main__':
    main()
