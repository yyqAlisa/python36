import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib
from sklearn.metrics import f1_score,recall_score


#设置字符集，防止中文乱码
from matplotlib.font_manager import FontProperties

plt.rcParams['font.family'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False


#1.加载数据
file_path = '../datas/iris.txt'
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

X = datas[names[0:-1]]
Y = datas[names[-1]]
# print(X)

#3.数据分割
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.9, random_state=28)

#4.高斯朴素贝叶斯算法模型的训练
algo = GaussianNB(priors=[1.0 / 3, 1.0 / 3, 1.0 / 3])

#5.算法模型的训练
algo.fit(x_train, y_train)

#6.打印模型参数
item_x = x_test.iloc[0]
item_y = y_test.iloc[0]
print(item_x)
print(item_y)
print(algo.predict(item_x))

print('各个类别的概率:{}'.format(algo.class_prior_))
print('各个类别的样本数目:{}'.format(algo.class_count_))
print('各个类别各个特征属性所服从的高斯分布的均值:{}'.format(algo.theta_))
print('各个类别各个特征属性所服从的高斯分布的均值:{}'.format(algo.sigma_))

#6.模型效果评估
print('='*50)
print('训练集上的准确率:{}'.format(algo.score(x_train,y_train)))
print('测试集上的准确率:{}'.format(algo.score(x_test,y_test)))
print('训练集上的F1值:{}'.format(f1_score(y_train,algo.predict(x_train),average='macro')))
print('测试集上的F1值:{}'.format(f1_score(y_test,algo.predict(x_test),average='macro')))
print('训练集上的召回率:{}'.format(recall_score(y_train,algo.predict(x_train),average='macro')))
print('测试集上的召回率:{}'.format(recall_score(y_train,algo.predict(x_train),average='macro')))

#7.模型保存
joblib.dump(algo, './model/algo3.m')








