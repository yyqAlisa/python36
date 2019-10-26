import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib
from sklearn.metrics import f1_score,recall_score


#设置字符集，防止中文乱码
from matplotlib.font_manager import FontProperties

plt.rcParams['font.family'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False


#1.加载数据
file_path = './datas/iris.txt'
names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'cla']
df = pd.read_csv(file_path, header=None, names=names)
# print(df.head(10))
# print(df.info)

#2.提取数据
def parse_record(record):
    result = []
    # print(type(record))
    r = zip(names, record)
    for name, value in r:
        # print(type(value))
        if name == 'cla':
            if value == 'Iris-setosa':
                result.append(1)
            elif value == 'Iris-versicolor':
                result.append(2)
            else:
                result.append(3)
        else:
            result.append(value)

    return result


datas = df.apply(lambda r: parse_record(r), axis=1)
print(datas.head(10))
# print(datas.cla.value_counts()) 打印不了

X = datas[names[0:-1]]
Y = datas[names[-1]]
# print(X)

#3.数据分割
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.9, random_state=28)

#4.决策树算法模型构建
'''
criterion="gini",
#给定采用gini还是entropy作为纯度的衡量指标
splitter="best",
#进行划分特征选择的时候采用什么方式来选择，best表示每次选择的划分特征都是全局最优的（所有特征属性的最优
划分);random表示每次选择的划分不是所有特征属性中的最优特征，而且先从所有特征中随机的抽取部分特征属性，
然后在这个部分特征属性中选择最优的，也就是random选择的是局部最优
#best每次都选择最优的划分特征，但是这个最优划分特征其实是在训练集数据上的这一个最优部分。但是这个最优在
实际的属性中可能该属性就不是最优的，所以容易陷入过拟合的情况--->如果存在过拟合，可以考虑random的方式来
选择
max_depth=None,
#指定构建的决策树允许的最高层次是多少，默认不限制
min_samples_split=2,
#指定进行数据划分的时候，当前节点中包含的数据至少要取的数据量
min_samples_leaf=1,
min_weight_fraction_leaf=0.,
max_features=None,
#在random的划分过程中，给定每次选择局部最优划分特征的时候，使用多少个特征属性
random_state=None,
max_leaf_nodes=None,
min_impurity_decrease=0.,
min_impurity_split=None,
class_weight=None,
presort=False):
'''
algo = DecisionTreeClassifier(criterion="gini",max_depth=7)

#5.算法模型的训练
algo.fit(x_train, y_train)

#6.模型效果评估
print('训练集上的准确率:{}'.format(algo.score(x_train,y_train)))
print('测试集上的准确率:{}'.format(algo.score(x_test,y_test)))
print('训练集上的F1值:{}'.format(f1_score(y_train,algo.predict(x_train),average='macro')))
print('测试集上的F1值:{}'.format(f1_score(y_test,algo.predict(x_test),average='macro')))
print('训练集上的召回率:{}'.format(recall_score(y_train,algo.predict(x_train),average='macro')))
print('测试集上的召回率:{}'.format(recall_score(y_train,algo.predict(x_train),average='macro')))

#7.模型保存
joblib.dump(algo, './model/algo.m')








