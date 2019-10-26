import pandas as pd
import math

from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures


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

flag = 3

if flag == 1:
    #4.需求一：使用Ridge构建模型
    '''
    alpha=1.0 指定的是L2的正则化项系数，也就是ppt上的λ
    fit_intercept=True 模型是否训练截距项，默认为True表示训练
    '''
    algo1 = Ridge(alpha=1.0, fit_intercept=True)
    algo1.fit(x_train, y_train)
    print('=' * 50)
    print('Ridge算法模型训练集上的效果:{}'.format(algo1.score(x_train, y_train)))
    print('Ridge算法模型测试集上的效果:{}'.format(algo1.score(x_test, y_test)))

if flag == 2:
    #需求二：分别考虑Lasso和Ridge算法在做多项式扩展后的模型效果，并输出最优的模型参数
    '''
    ploy1 + lasso
    ploy2 + lasso 
    ploy3 + lasso
    ploy1 + ridge
    ploy2 + ridge 
    ploy3 + ridge
    
    '''

    models = [
        Pipeline([
            ('poly', PolynomialFeatures()),
            ('linear', Lasso())
        ]),
        Pipeline([
            ('poly', PolynomialFeatures()),
            ('linear', Ridge())
        ]),
    ]

    #用于网格交叉验证时候的模型参数

    parameters = {
        'poly_degree': [1, 2, 3],
        'linear_alpha': [0.5, 1, 1.5],
        'linear_fit_intercept': [True, False],
        'linear_normalize': [False, True]
    }

    titles = ['poly + lasso', 'poly + ridge']
    #迭代管道模型
    for t in range(2):
        #做网格交叉验证来选择最优模型
        model = GridSearchCV(estimator=models[t], param_grid=parameters, cv=5)
        #模型训练
        model.fit(x_train, y_train)
        print('{}算法模型训练集上的效果:{}'.format(titles[t], model.score(x_train, y_train)))
        print('{}Ridge算法模型测试集上的效果:{}'.format(titles[t], model.score(x_test, y_test)))
        print('{}算法模型的最优参数:{}'.format(titles[t], model.best_params_))

if flag == 3:
    #需求三：使用Lasso的最优参数来做特征选择
    print('=' * 50)
    print('进入模型的数据大小:{}---{}'.format(x_train.shape, y_train.shape))
    poly = PolynomialFeatures(degree=2)
    x_train = poly.fit_transform(x_train, y_train)
    x_test = poly.fit_transform(x_test)
    print('经过多项式扩展后的数据大小:{}---{}'.format(x_train.shape, y_train.shape))
    print('经过多项式扩展后的数据类型:{}---{}'.format(type(x_train), type(y_train)))

    linear = Lasso(alpha=0.5, fit_intercept=True, normalize=False, random_state=28)
    linear.fit(x_train, y_train)
    print('获取模型参数:{}')
    print(linear.coef_)

    #开始进行特征选择的操作
    final_column_indexs = []
    poly_column_num = x_train.shape[1]  #获得列数
    for index, coef in zip(range(poly_column_num),linear.coef_):
        if math.fabs(coef) > 0:
            final_column_indexs.append(index)
        else:
            print('删除第{}列数据'.format(index))
    x_train = x_train[:, final_column_indexs]
    x_test = x_test[:, final_column_indexs]
    print('进行特征选择后训练集的数据大小:{}'.format(x_train.shape))
    print('进行特征选择后测试集的数据大小:{}'.format(x_test.shape))

    #基于特征选择之后的样本做其他模型的构建
    algo2 = Ridge(alpha=0.5, fit_intercept=True)
    algo2.fit(x_train, y_train)
    print('=' * 50)
    print('Ridge算法模型训练集上的效果:{}'.format(algo2.score(x_train, y_train)))
    print('Ridge算法模型测试集上的效果:{}'.format(algo2.score(x_test, y_test)))


