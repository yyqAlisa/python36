#局部作用域能获取到全局变量的值
#全局作用域 不能 获取局部变量的值
#全局作用域
# c = 333 #全局变量

# def func1():
#     #局部作用域
#     b = 222  #局部变量
#     print(c)
#     return b,999  #返回值，丢出这个数据


# def func2():
#     # print(b)
#     print(func1())
#     pass

# re_func1 = func1()
# print(re_func1)
# func2()

# a = [1,2,3]
# def func3():
#     a.append(1111)
#     print(a)
#
# func3()
# print(a)

# b = 'aaa'
# def func4():
#     b = 'bbb'
#     print(b)
#
# def func5():
#     b = 'ccc'
#
# func4()
# print(b)


# def func5():
#     return 111
#
# print(func5())


# 账号 aaa
# 密码 111111
# 输入错误超过3次提示用户"密码错误,请取卡”
# def login():
#     user = input('请输入账号')
#     password = input('请输入密码')
#     if user=='aaa' and password=='111111':
#         return True
#     else:
#         return False
# def get_money():
#     while True:
#         money = int(input('请输入取款金额0~1000，必须是100的倍数'))
#         if 1000>=money>=0 and money%100==0:
#             print('交易完成，请取卡')
#             break
#         else:
#             print('取款失败,请输入符合要求的金额')
# for i in range(3):
#     r = login()
#     if r:
#         print('密码正确，请取款')
#         get_money()
#         break
#     else:
#         print('账号或密码错误,请重新输入')
# else:
#     print('密码错误,请取卡')

# def login():
#     c=0
#     while True:
#         user=input('请输入账号')
#         password=input('请输入密码')
#         if user=='aaa':
#             if password=='11111':
#                 print('登入成功')
#                 return True
#             else:
#                 print('密码错误')
#                 c+=1
#                 if c==3:
#                     print('密码错误3次，请取卡')
#                     return False
#         else:
#             print('账号错误')
#             c+=1
#             if c==3:
#                 return False
#
# def get_money():
#     while True:
#         qushu=int(input('请输入金额'))
#         if qushu%100==0 and 0<=qushu<=1000:
#             print(qushu)
#             print('交易完成，请取卡')
#             break
#         else:
#             print('请重新输入金额')
# if login():
#     get_money()


#自己写的
# a=111
# def func1():
#     b = 222
#     print(a)
#     return b
#
# def func2():
#     print(func1())
#
# # func1()
# func2()
# # print(func1())

