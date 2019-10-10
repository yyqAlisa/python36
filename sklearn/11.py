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
n = 100000
b_values = np.random.normal(loc= -1.0,scale=10.0,size=n)
c_values = np.random.normal(loc= 0.0,scale=10.0,size=n)

x = np.random.randint(low=-10, high=10)

def f(x, b, c):
    return x ** 2 + b * x + c


def f1(x, b_values, c_values):
    result = 0
    for b, c in zip(b_values, c_values):
        # 遍历所有b和c的组合，这里求均值（防止数据量太大，计算困难）
        result += f1(x, b, c) / n
    return result
    print('当前参数为:')
    print('b_values={}'.format(b_values))
    print('c_values={}'.format(c_values))


f1(x, b_values, c_values)


