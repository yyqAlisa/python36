# 题目18：打印出如下图案（菱形）
#  
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

# for i in range(7):
#     if i<=2:
#         print(('*'*(2*i+1)).center(7))
#     else:
#         print(('*' * (13-2 * i )).center(7))
#
# --------------------------------------------
# h = 7
# # 上半部分
# for i in range(h//2):
#     for k in range(h//2-i):
#         print(' ',end='')
#     for j in range(2*i+1):
#         print('*',end='')
#     print()
# # 下半部分
# for i in range(h//2+1):
#     for k in range(i):
#         print(' ',end='')
#     for j in range(h-2*i):
#         print('*',end='')
#     print()



# 函数

# def func1(): #定义函数
#     '''我是文档字符串'''
#     print(111)
#
# func1()  #调用函数
# print(func1.__doc__)  #可以获取到文档字符串


# def func2(a):  #形参
#     print(a)
#
# func2(111)  #实参

#必备参数-》匿名不定长参数-》默认参数-》命名不定长参数
def func3(a,b,*d,c=999,**e):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
func3(1,2,3,4,5,6,7,c=888,aa=1,bb=2,cc=3)
# func3(b=222,a=111)
# func3(a=111,111)  #这种情况绝对不能出现