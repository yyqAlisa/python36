''''
   用解析解的方式求解
'''

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import BaggingRegressor


#1.加载数据
path = './datas/household_power_consumption_201.txt'
df = pd.read_csv(filepath_or_buffer=path, sep=';')

#查看一下info信息
# print(df.info())

#2.数据清洗
df.replace('?',np.nan, inplace=True)
df = df.dropna(axis=0, how='any')
# print(df.info())

#3.模型所需要的特征属性获取（构建特征属性矩阵Xhe目标属性Y）
X = df.iloc[:, 2:5]
Y = df.iloc[:, 5]

#4.数据分割
x_train,x_test,y_train,y_test = train_test_split(X,Y,train_size=0.7,random_state=28)

#6.方式一：直接使用线性回归
algo = LinearRegression()
algo.fit(x_train,y_train)
print('线性回归模型效果：{}'.format(algo.score(x_train,y_train)))

#7.方式二：使用Boosting的算法
'''
base_estimator=None, #给定基础的模型对象，也就是子模型
n_estimators=10, #给定子模型的数目
max_samples=1.0, #给定子模型训练的时候，使用多少个样本训练，这个是总样本的百分比
max_features=1.0, #给定子模型训练的时候，使用样本的多少个特征属性来训练，这个是总样本的百分比
bootstrap=True, #给定子模型训练的时候，每个训练集的产生样本是否基于重采样，默认为True,表示是
bootstrap_features=False, #给定子模型训练的时候，每个训练集的产生用于训练的特征属性是否基于
                           重采样，默认为False,表示不是
oob_score=False,
warm_start=False,
n_jobs=None,
random_state=None,
verbose=0)
'''
br = BaggingRegressor(base_estimator=LinearRegression(), n_estimators=100,
                 max_samples=0.8, max_features=0.7)
br.fit(x_train,y_train)
print('线性回归的模型效果:{}'.format(br.score(x_train,y_train)))
