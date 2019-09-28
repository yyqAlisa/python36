# 递归：1、有自变量
#     2、有一个边界值
#1到100之和
# def func1(n):
#     if n==1:
#         return 1
#     return n+func1(n-1)
#
# print(func1(100))


# 斐波那契数列（Fibonacci sequence）指的是这样一个数列：1、1、2、3、5、8、13、21、34、……
# 在数学上，斐波纳契数列以如下被以递归的方法定义：F(0)=0，F(1)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）

# print(111)
# def fbnq(n):
#     if n==1 or n==2 :
#         return 1
#     return fbnq(n-1)+fbnq(n-2)
# # print(__name__)
# if __name__ == "__main__":  #主函数
#     n  = int(input('取斐波那契数列前几个数字'))
#     list1= []
#     for i in range(1,n+1):
#         list1.append(fbnq(i))
#     print(list1)
#
# # 约瑟夫环
# # （1）一群人围在一起坐成环状（如：N）
# # （2）从某个编号开始报数（如：K）
# # （3）数到某数（如：M）的时候，此人出列，下一个人重新报数
# # （4）一直循环，直到剩余2个人，约瑟夫环结束
N = list(range(1,11))
K = 0
M = 3
while len(N)>2:
    K = (K+3-1)%len(N)
    N.pop(K)
    print(K)
    print(N)
    print('----------------')