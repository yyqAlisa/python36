import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomTreesEmbedding
from sklearn.externals import joblib
from sklearn.metrics import f1_score,recall_score


#设置字符集，防止中文乱码
from matplotlib.font_manager import FontProperties

plt.rcParams['font.family'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False


#1.加载数据
file_path = './datas/iris.txt'
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

#4.决策树算法模型构建
'''
n_estimators='warn',
#随机森林中，子模型决策树的数目默认为warn
criterion="gini",
#同决策树算法
max_depth=None,
#同决策树算法
min_samples_split=2,
min_samples_leaf=1,
min_weight_fraction_leaf=0.,
max_features="auto",
#同决策树算法
max_leaf_nodes=None,
min_impurity_decrease=0.,
min_impurity_split=None,
bootstrap=True,
#给定是否采用有放回的方式产生子数据集，默认为True表示采用
oob_score=False,
n_jobs=None,
random_state=None,
verbose=0,
warm_start=False,
class_weight=None)
'''
algo = RandomTreesEmbedding(n_estimators=100,max_depth=3)

#5.算法模型的训练
algo.fit(x_train, y_train)

#6.直接获取模型的扩展结果
x_train2 = algo.transform(x_train)
x_test2 = algo.transform(x_test)
print('扩展前大小:{},扩展后大小:{}'.format(x_train.shape,x_train2.shape))
print('扩展前大小:{},扩展后大小:{}'.format(x_test.shape,x_test2.shape))

#8.随机森林可视化
print('随机森林中的子模型列表:{}'.format(len(algo.estimators_)))
#2.方式二：直接使用pydotplus插件直接生成pdf文件进行保存
from sklearn import tree
import pydotplus

#feature_names=None,class_names=None 分别给定特征属性和目标属性的name信息
for i in range(len(algo.estimators_)):
    dt = algo.estimators_[i]
    dot_data = train_test_split(decision_tree=algo,out_file=None,
                                feature_names=['sepal length','sepal width','petal length','petal width'],
                                class_names=['Iris-setosa','Iris-versicolor','Iris-virginica'],
                                filled=True)

    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_png('iris{}.png'.format(i))
    graph.write_pdf('iris2.pdf'.format(i))









