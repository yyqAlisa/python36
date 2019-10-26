''''
   用解析解的方式求解
'''

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

#设置字符集，防止中文乱码
from matplotlib.font_manager import FontProperties

plt.rcParams['font.family'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

#1.加载数据
path = '../datas/household_power_consumption_201.txt'
df = pd.read_csv(filepath_or_buffer=path,sep=';')

#查看一下info信息
# print(df.info())

#2.数据清洗
#inplace:当设置为True的时候，表示对原始的DataFrame做修改；默认为False
df.replace('?', np.nan, inplace=True)
#DataFrame：axis=0对行做处理，axis=1表示对列做处理
#how:可选参数any和all,any表示只要有一个为nan,那么进行数据删除；如果为all,表示所有值为nan,数据删除
#功能：只要有任意一个样本中的任意数据特征属性为nan的形式，就将该样本删除
df = df.dropna(axis=0, how='any')
print(df.info())

#3.模型所需要的特征属性获取（构建特征属性矩阵Xhe目标属性Y）
X = df.iloc[:, 2:4]
Y = df.iloc[:, 5]

#4.数据分割
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.7, random_state=28)

#5.特征工程
#操作可选
#主要是：哑编码、连续数据离散化、数据的转换、标准化、归一化、降维...
ss = StandardScaler()
x_train = ss.fit_transform(x_train)  #训练并转换
x_test = ss.fit_transform(x_test)    #直接使用在模型构建数据上进行一个数据标准化操作


#6.算法/模型对象构建
algo = LinearRegression()

#7.算法模型训练
algo.fit(x_train,y_train)

#8.模型效果评估
#可选，主要目的就是评估一下模型的效果
#主要就是根据算法类型，分别选择精确率、FI、RMSE、MSE、R2等指标进行校验
print('模型效果：{}'.format(algo.score(x_train,y_train)))

#9.模型的保存
'''
两种保存方式：
  1.直接保存模型对象
  2.保存模型的预测结果到数据库或者其他数据存储位置
'''

# a.直接保存模型对象
joblib.dump(algo, './model/linear')

#b.保存模型的预测结果
#获取预测结果
y_hat = algo.predict(x_test)
print(y_hat)

#画图看一下效果
t = np.arange(len(x_test))
plt.figure(facecolor='w')
plt.plot(t, y_test, 'r-', linewidth=2, label='真实值')
plt.plot(t, y_hat, 'g-', linewidth=2, label='预测值')
plt.legend(loc='lower right')
plt.title('线性回归')
plt.show()
