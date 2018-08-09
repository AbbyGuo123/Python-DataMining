# import pyfpgrowth
# transactions = [[1, 2, 5],
#                 [2, 4],
#                 [2, 3],
#                 [1, 2, 4],
#                 [1, 3],
#                 [2, 3],
#                 [1, 3],
#                 [1, 2, 3, 5],
#                 [1, 2, 3]]
# patterns = pyfpgrowth.find_frequent_patterns(transactions, 2)
# rules = pyfpgrowth.generate_association_rules(patterns, 0.7)
# print(rules)

from sklearn import datasets
from sklearn.linear_model import LinearRegression

loaded_data=datasets.load_boston()
data_x =loaded_data.data
data_y=loaded_data.target

model = LinearRegression()
model.fit(data_x,data_y)
print(model.predict(data_x[:4,:]))
print(data_y[:4])
print(type(loaded_data))


