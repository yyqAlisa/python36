'''
  实现基于梯度下降的回归算法
'''

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import math

#设置字符集，防止中文乱码
from matplotlib.font_manager import FontProperties

plt.rcParams['font.family'] = ['Arial Unicode MS'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

#1.构建模拟数据
np.random.seed(28)
N = 10
#linspace:用于产生指定范围内的指定数量点数，相邻数据跨度相同，并返回一个行向量。
x = np.linspace(start=0, stop=6, num=N) + np.random.randn()
y = 1.8 * x ** 3 + x ** 2 - 14 * x - 7 + np.random.randn()
x.shape = -1, 1  #将x从原来的元组形式变成矩阵形式
y.shape = -1,1
# y = y.reshape(-1,1)
# y = np.reshape(y, (-1, 1))
print(x.shape)
print(y.shape)

def validate(X,Y):

   #校验下X和Y的格式是否正常,如果不正常返回False,否则返回True

    m1,n1 = np.shape(X)
    m2,n2 = np.shape(Y)
    if m1 != m2:
        return False
    else:
        if n2 != 1:
            return False
        else:
            return True

def predict(x, theta, intercept=0):
    result = 0.0
    #1.x和Θ相乘
    n = len(x)
    for i in range(n):
        result+= x[i] * theta[i]
    #2.加上截距项
    result +=intercept
    #3.返回结果
    return result

def predict_X(X,theta,intercept=0.0):
    Y = []
    for x in X:
        Y.append(predict_X(x,theta,intercept))
    return Y



alpha=0.1
max_iter=100
tol=1e-4
fit_intercept=True
def fit(X, Y, alpha=0.1,max_iter=100,tol=1e-4,fit_intercept=True):

 # X:输入的特征矩阵x,格式为二维数组形式，m*n,m表示样本数目，n表示每个样本的特征维度数目
 # Y:输入的目标矩阵y,格式为二维数组形式，m*l,m表示样本数目，l表示每个样本有一个带预测的特征
 # alpha:梯度下降中的步长或者学习率
 # max_iter:梯度下降迭代中最大迭代次数（数据从头到尾处理一遍，认为是一个迭代）
 # tol:收敛变换最小值
 # fit_intercept:是否训练模型的截距项


    #1.校验下X和Y的格式是否正常
    assert validate(X,Y)

    #2.开始获取参数
    #获取样本数和维度数目
    m,n = np.shape(X)
    #定义theta参数
    theta = np.zeros(shape = [m])
    #定义截距项
    intercept = 0
    #获取最大允许迭代次数
    max_iter = 100 if max_iter <=0 else max_iter
    #构建一个误差保存对象
    diff =np.zeros(shape = [m])
    #定义一个之前状态的损失函数值
    pre_sum_j = 1 << 32


    #3.开始迭代，获取模型参数
    for i in range(max_iter):
        '''
           作业只实现BGD的算法
        '''
        #a.在当前的theta取值的情况下，计算预测值与实际值之间的差值（误差error）
        for k in range(m):
            y_true = Y[k][0]
            y_predict = predict(x[k],theta,intercept)
            diff[k] = y_true-y_predict

        #b.对每个Θ遍历求解
        for j in range(n):
            #求解梯度值
            gd = 0
            for k in range(m):
                gd += diff[k]*X[k][j]
            #进行参数模型更新
            theta[j] += alpha * gd

        #c.对截距项求解
        if fit_intercept:
            #求解梯度值
            # gd = 0
            # for k in range(m):
            #     gd += diff[k] * 1
            gd = np.sum(diff)
            # 进行参数模型更新
            intercept += alpha * gd

        #d.计算在当前模型参数的情况下的误差值
        sum_j= 0.0
        for k in range(m):
            y_true = Y[k][0]
            y_predict = predict(x[k],theta,intercept)
            current_y = y_true - y_predict
            sum_j = math.pow(current_y,2) #做2次平方
        sum_j /= m
        #保存之前的最小损失函数值
        tmp_sum_j = pre_sum_j
        pre_sum_j = sum_j

        #当两次的误差损失函数的值变化小于tol的时候，直接结束模型训练
        if np.abs(pre_sum_j-sum_j) < tol:
            break

    #函数返回值
    print('迭代{}次后，损失函数值为:{}'.format(i,pre_sum_j))
    return theta,intercept,pre_sum_j

def score_X_Y(X,Y,theta,intercept=0):
    #计算R^2

    #1.获取预测值
    y_predict = predict_X(X,theta,intercept)
    #2.获取R^2
    r2 = score(Y,y_predict)
    #3.结果返回
    return r2

def score(y_true,y_predict):
    #1.计算rss和tss
    average_y_true = np.average(y_true)
    m = len(y_true)
    rss = 0.0
    tss = 0.0
    for k in range(m):
        rss += math.pow(y_true[k]-y_predict[k],2)
        tss += math.pow(y_true[k]-average_y_true,2)

    #2.计算R^2
    r2 = 1 - 1.0 * rss / tss
    #3.返回结果
    return r2






#2.算法构建
#使用sklearn中的算法
model = LinearRegression()
model.fit(x, y)
# s1 = model.score(x,y)
s1 = score_X_Y(x,y,model.coef_,model.intercept_)
print('模块自带线性回归默认实现模型==============')
print('模型自带score API评估值为:{}'.format(s1))
print('参数列表为:{}'.format(model.coef_)) #coef_指的是回归系数
print('截距项为:{}'.format(model.intercept_))

#b.使用自定义的梯度下降线性回归算法进行模型构建
theta,intercept,sum_j = fit(x,y)
s2 = score_X_Y(x, y,theta)
print('自定义的线性回归模型============')
print('自定义模型自带score API评估值为:{}'.format(s2))
print('参数为:{}'.format(theta))
print('截距项为:{}'.format(intercept))



#构建画图用的模拟数据
x_hat = np.linspace(x.min(), x.max(),num=100)
x_hat.shape = -1,1
y_hat = model.predict(x_hat)
y_hat2 = predict_X(x_hat,theta,intercept)



#画图看一下
plt.plot(x, y, 'ro', ms=10)
plt.plot(x_hat, y_hat, color='#b624db', lw=2, label='sklearn线性模型,$R^2$:%.3f' % s1)
plt.plot(x_hat, y_hat2, color='#b649b6', lw=2, label='自定义线性模型,$R^2$:%.3f' % s2)
plt.legend(loc='upper left')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.suptitle('sklearn模型和自定义模型的效果比较',fontsize=20)
plt.show()
