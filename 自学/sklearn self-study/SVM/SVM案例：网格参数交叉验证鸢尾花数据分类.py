import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.externals import joblib
from sklearn.metrics import f1_score,recall_score


#设置字符集，防止中文乱码
from matplotlib.font_manager import FontProperties

plt.rcParams['font.family'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False


#1.加载数据
file_path = '../datas/iris.txt'
df = pd.read_csv(file_path, header=None)
# print(df.head(10))
# print(df.info)

#2.提取数据
X = df[list(range(4))]
Y = pd.Categorical(df[4]).codes  #把Y转换成分类型的0，1，2
print('总样本数目:%d;特征属性数目:%d' %X.shape)
# print(X)
# print(Y)


#3.数据分割
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.9, random_state=28)

#4.SVC算法模型构建

svm = SVC()

#构建网格参数选择的交叉验证对象
#estimator:给定对哪个模型算法对象进行调优
#param_grid:给定estimator对应的 模型可选的参数列表有哪些，是一个dict字典数据类型
#param_grid中的key是estimator算法对应的参数是字符串形式，value是该参数可选的值列表集合
param_grid = {
    'C': [0.01, 0.1, 1.0, 10.0],
    'kernel': ['rbf', 'linear', 'poly']
}
algo = GridSearchCV(estimator=svm,param_grid=param_grid)

#5.算法模型的训练
algo.fit(x_train, y_train)

#获取实际最优模型
print('最优模型:{}'.format(algo.best_estimator_))
print('最优模型对应的参数:{}'.format(algo.best_params_))

#6.模型效果评估
print('训练集上的准确率:{}'.format(algo.best_estimator_.score(x_train,y_train)))
print('测试集上的准确率:{}'.format(algo.best_estimator_.score(x_test,y_test)))
print('训练集上的F1值:{}'.format(f1_score(y_train,algo.predict(x_train),average='macro')))
print('测试集上的F1值:{}'.format(f1_score(y_test,algo.predict(x_test),average='macro')))
print('训练集上的召回率:{}'.format(recall_score(y_train,algo.predict(x_train),average='macro')))
print('测试集上的召回率:{}'.format(recall_score(y_train,algo.predict(x_train),average='macro')))

#7.模型保存
joblib.dump(algo.best_estimator_, './model/algo2.m')





