import pandas as pd
import math


from sklearn.model_selection import train_test_split, GridSearchCV
import xgboost as xgb
from sklearn.metrics import mean_squared_error,r2_score


#1.加载数据
file_path = '../datas/slump_test.txt'
df = pd.read_csv(file_path, sep=',')
# print(help(pd.read_csv))
# print(df.head(5))

#2.获取特征矩阵X和目标属性Y
x = df.iloc[:, 1:8]
y = df.iloc[:, -1]

#3.数据分割
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.9, random_state=28)
print('训练集大小:{}'.format(x_train.shape))
print('测试集大小:{}'.format(x_test.shape))

'''
开始使用xgboost的相关API
'''
#一：直接使用xgboost的相关API
#a.数据转换
dtrain = xgb.DMatrix(data=x_train, label=y_train)
dtest = xgb.DMatrix(data=x_test)

#b.模型参数构建
params = {'max_depth': 2, 'eta': 0.1, 'objective': 'reg:linear'}  #eta是学习率
num_boost_round = 2   #迭代次数

#c.模型训练
model = xgb.train(params=params, dtrain=dtrain,num_boost_round=num_boost_round)

#d.模型保存
model.save_model('xgb.model')
print(model)


#a.加载模型预测
model2 = xgb.Booster()
model2.load_model('xgb.model')
print(model2)
print('训练集MSE:{}'.format(mean_squared_error(y_test, model2.predict(dtest))))
print('训练集R2:{}'.format(r2_score(y_test, model2.predict(dtest))))
