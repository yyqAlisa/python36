# for i in range(10):
#     if i%2 !=0:
#         print(i)
#         continue
#     i+=2
#     print(i)
#
# m = ['2','4','6']
# m.insert(0,'8')
# print(m)
# m.remove('2')
# print(m)
# m.pop()
# print(m)
# m.pop()
# print(m)
#
# a =[1,2,3,4,5]
# b =[6,7,8,9,0,1]
# print(list(zip(a,b)))
# print(a+b)
#
# def back():
#     return(1,'小甲鱼',3.14)
#
# print(back())
#
# old_price = float(input('请输入价格'))
# rate = float(input('请输入折扣'))
# def discounts(price,rate):
#     final_price = price * rate
#     old_price =50
#     print('修改后old_price的值1是：',old_price)
#     return final_price
#
#
# new_price = discounts(old_price,rate)
# print('修改后old_price的值2是：',old_price)
# print('打折后的价格是',new_price)

# count = 5
# def myfun ():
#     count=10
#     print(10)
#
# myfun()
# print(count)


# count = 5
# def myfun ():
#     global count
#     count=10
#     print(10)
#
# myfun()
# print(count)


# def FunX(x):
#     def FunY(y):
#         return x * y
#     return FunY
#
# i = FunX(8)
# print(type(i))
# print(i(5))

# def fun1():
#     x = 5
#     def fun2():
#         return x * x
#     return fun2
#
# fun1()

# dict3 = dict((('F',70),('A',40),('V',10),('S',38)))
# print(dict3)
#
# dict4 = dict([('F',70),('A',40),('V',10),('S',38)])
# print(dict4)
#
# dir_5 = {"name":"zhang san ","age":12,"tel":"199200000"}
# name = dir_5['name']
# tel = dir_5['tel']
#
#
# print("name = " + dir_5["name"])
# print(dir_5)
# print(name)
# print(tel)

# result = []
# for index in range(6):
#     if result[index]:
#         print('答对了')
#
# print(result)

#斐波那契数列 1，1，2，3，5，8，13，21，....
#迭代方法
# class Fibs:
#     def __init__(self,n=10):
#         self.a = 0
#         self.b = 1
#         self.n = n
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a,self.b=self.b,self.a+self.b
#         if self.a>self.n:
#             raise StopIteration
#         else:
#             return self.a

# fibs=Fibs()
# for each in fibs:
#     print(each)
#
# #生成器方法 yield
# def libs():
#     a=0
#     b=1
#     while True:
#         a,b=b,a+b
#         yield a
#
# for each in libs():
#     if each >100:
#         break
#     else:
#         print(each)