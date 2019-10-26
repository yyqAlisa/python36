import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
from sklearn.metrics import f1_score,recall_score


#设置字符集，防止中文乱码
from matplotlib.font_manager import FontProperties

plt.rcParams['font.family'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False


#1.加载数据
file_path = '../datas/iris.txt'
names = ['sepal length','sepal width','petal length','petal width','cla']
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

#4.KNN算法模型构建
#n_neighbors:邻居数，默认为5，一般需要调整参数
#weights:做预测的时候采用何种预测方式，是等权重还是不同权重
#algorithm:模型训练过程中的采用方式
#leaf_size:构建Tree的过程中，停止构建的条件，最多的叶子数目
#p&metric:样本相似度度量方式，默认为欧几米得距离

algo = KNeighborsClassifier(n_neighbors=5, weights='uniform', algorithm='auto', leaf_size=30,
                 p=2, metric='minkowski', metric_params=None, n_jobs=None)

#5.算法模型的训练
algo.fit(x_train,y_train)

#6.模型效果评估
print('训练集上的准确率:{}'.format(algo.score(x_train,y_train)))
print('测试集上的准确率:{}'.format(algo.score(x_test,y_test)))
print('训练集上的F1值:{}'.format(f1_score(y_train,algo.predict(x_train),average='macro')))
print('测试集上的F1值:{}'.format(f1_score(y_test,algo.predict(x_test),average='macro')))
print('训练集上的召回率:{}'.format(recall_score(y_train,algo.predict(x_train),average='macro')))
print('测试集上的召回率:{}'.format(recall_score(y_train,algo.predict(x_train),average='macro')))

#7.模型保存
joblib.dump(algo, './model/algo.m')








