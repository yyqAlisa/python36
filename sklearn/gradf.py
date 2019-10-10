'''
   梯度下降作业：
   目标函数：y = x**2 +b * x + c
   需求：求解最小值对应的x和y
   要求：写代码
     数据：
        b:服从均值为-1，方差为10的随机数
        c:服从均值为0，方差为10的随机数

   假定a、b、c这样的数据组合总共10、100、10w、100w条数据，求解现在的数据情况下，
   目标函数取最小值的时候，x和y分别对应多少？
'''

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#设置字符集，防止中文乱码
from matplotlib.font_manager import FontProperties

plt.rcParams['font.family'] = ['Arial Unicode MS'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

#1.随机数据产生
#给定随机数种子:当程序多次运行的时候，可以保证每次运行的时候随机的数据都是一样的
np.random.seed(28)
n = 10
b_values = np.random.normal(loc= -1.0,scale=10.0,size=n)
c_values = np.random.normal(loc= 0.0,scale=10.0,size=n)

#随机数据可视化查看
# plt.figure(facecolor='w')
# plt.subplot(1,2,1)
# plt.hist(b_values,100,color='#FF0000')
# plt.subplot(1,2,2)
# plt.hist(b_values,100,color='#00FF00')
# plt.title('随机数据可视化')
# plt.show()

max_iter = 1000
tol = 0.00001
alpha = 0.01
def calc_min_value_with_one_sample(n,b_values,c_values,max_iter,tol,alpha):

# '''
#    计算最小值对应的x和y
#    n:样本数量
#    b_values:样本对应的b值
#    c_values:样本对应的c值
#    max_iter:最大迭代次数
#    tol:当变量小于该值的时候收敛
#    alpha:梯度下降学习率
# '''

    def f(x,b,c):
        return x**2 + b * x +c

    def f1(x,b_values,c_values):
        result = 0
        for b,c in zip(b_values,c_values):
            #遍历所有b和c的组合，这里求均值（防止数据量太大，计算困难）
            result += f1(x,b,c)/n
        return result



    def h(x,b,c):
        return 2*x + b

    def h1(x,b_values,c_values):
        result = 0
        for b, c in zip(b_values, c_values):
        # 遍历所有b和c的组合，这里求均值（防止数据量太大，计算困难）
            result += h1(x,b,c) / n
        return result

    #定义变量
    step_change = 1.0 + tol
    step = 0

    #获取第一个样本
    b = b_values[0]
    c = c_values[0]

    #给定一个初始的x值
    current_x = np.random.randint(low=-10,high=10)
    current_y = f1(current_x,b_values,c_values)

    print('当前参数为:')
    print('b_values={},b的均值为:{}'.format(b_values,np.mean(b_values)))
    print('c_values={},c的均值为:{}'.format(c_values,np.mean(c_values)))

    #开始迭代循环
    while step_change > tol and step <max_iter:
        #1.计算梯度值
        current_d_f = h1(current_x,b_values,c_values)
        #2.更新参数
        current_x = current_x - alpha*current_d_f
        #3.计算更新x之后的y值
        tmp_y = f(current_x,b_values,c_values)
        #4.记录y的变化大小，更新迭代次数，更新当前的y值
        step_change = np.abs(current_y - tmp_y)
        step +=1
        current_y = tmp_y
    print('最终更新的次数：{},最终的变化率'.format(step,step_change))
    print('最终的结果为：{}----{}'.format(current_x,current_y))

print('*'*50)
calc_min_value_with_one_sample(n,b_values,c_values,max_iter,tol,alpha)


