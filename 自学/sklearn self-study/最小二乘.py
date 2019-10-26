'''
   用解析解的方式求解
'''

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

#设置字符集，防止中文乱码
from matplotlib.font_manager import FontProperties

plt.rcParams['font.family'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

#加载数据
path = './datas/household_power_consumption_200.txt'
df = pd.read_csv(filepath_or_buffer=path,sep=';')

#查看一下info信息
# print(df.info())
# print(df.head(5))

#获取功率的值作为特征属性X,获取电流的值作为目标属性Y
X = df.iloc[:,2:4]
Y = df.iloc[:,5]

print(X.head(5))
print(Y)

#将数据分成训练集和测试集
#random_state:随机数种子，保证在分割数据的时候，多次执行的情况产生的数据是一样的
x_train,x_test,y_train,y_test = train_test_split(X,Y,train_size=0.7,random_state=28)
print(x_train.shape)
print(type(x_train))
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

#模型构建
#1.使用numpy的API将DataFrame转换为矩阵的对象
x = np.mat(x_train)
y = np.mat(y_train).reshape(-1,1)
print(y.shape)

#2.求解形式
theta = (x.T*x).I*x.T*y
print(theta)

#使用模型对数据做预测
y_hat = np.mat(x_test)*theta

#画图看一下效果
t = np.arange(len(x_test))
plt.figure(facecolor='w')
plt.plot(t,y_test,'r-',linewidth=2,label='真实值')
plt.plot(t,y_hat,'g-',linewidth=2,label='预测值')
plt.legend(loc='lower right')
plt.title('线性回归')
plt.show()





