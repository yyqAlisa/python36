# n = num = int(input('请输入一个数字：'))  # 用num保留初始值
# f = []  # 存放质因数的列表
#
# for j in range(int(num / 2) + 1):  # 判断次数仅需该数字的一半多1次
#     for i in range(2, n):
#         t = n % i  # i不能是n本身
#         if t == 0:  # 若能整除
#             f.append(i)  # 则表示i是99质因数
#             n = n // i  # 除以质因数后的n重新进入判断，注意应用两个除号，使n保持整数
#             break  # 找到1个质因数后马上break，防止非质数却可以整除的数字进入质因数列表
#
# if len(f) == 0:  # 若一个质因数也没有
#     print('该数字没有任何质因数。')
# else:  # 若至少有一个质因数
#     f.append(n)  # 此时n已被某个质因数整除过，最后一个n也是其中一个质因数
#     f.sort()  # 排下序
#     print('%d=%d' % (num, f[0]), end='')
#     for i in range(1, len(f)):
#         print('*%d' % f[i], end='')


# numbers = list(range(1,11)) #0-10人围在一起坐成环状
# kit = 0 #从某个编号开始报数
# mon = 3 #数到3时
# while len(numbers)>2: #判断人数人数是否大于2人
#     kit = (kit+3-1)%len(numbers) #kit不能超过总人数
#     numbers.pop(kit)
#     print(kit)
#     print(numbers)
#     print('-'*30)
#
# list = [] #创建一个空列表
# list1 = [1,1,1,2,3,4,5,6,1,7,1]
# val = 1
# for i in list1: #如果i在列表1中
#     if i not in list: #判断是否在空列表中
#         list.append(i) #将不重复的数字追加在list中
#         for x in list:
#             if x == val:
#                 list.pop(x)
#
# print(list)

#  一个足球队在寻找年龄在10岁到12岁的小女孩(包括10岁和12岁)加入。
# 编写个程序，询问用户的性别(m表示男性，f表示女性)和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
#
# count = 0 #记录询问次数
# sum = 0 #统计 符合条件的总人数
# for item in range(1,11):
#     print('第',count + 1,'次询问')
#     sex = input('请输入性别（m表示男性，f表示女性) :')
#     age = int(input('请输入年龄:'))
#     if sex == 'm'or 10<age<12:
#         print('很遗憾，我们需要10-12岁小女孩')
#     elif sex == 'f' and age<10 or age>12:
#         print('你的年龄不符合要求')
#     elif sex == 'f' and 10<=age<=12:
#         sum+=1 #该变量用来统计符合条件的人数
#         print('等的就是你')
#     count+=1
#
#     print("符合条件的总人数:%d " % sum)

# backpack_goods=['book','computer','cup','pen']
# dangerous_goods=['knife','gun','drug']
# for dangerous_good in dangerous_goods:
#     if dangerous_good in backpack_goods:
#         print('你不可以进入地铁')
#     else:
#         print('你可以进入地铁')







# flag = True
# with open('wow.txt', 'w', encoding='utf8') as file_wow:
#     try:
#         while (flag):
#             q = input('请输入你的感受，退出请输入#')
#             if q == "#":
#                 flag = False
#                 break
#             file_wow.writelines(q + " \n")
#     except Exception as result:
#         print('未知错误%s' % result)

# dict = {1:'a',2:'b'}
# dict[0]='aaa'
# print(dict)
#
# list1 = [7,8,9,10,11,12]
#
# row =20
# n = 1
# for a in range(n):#循环三角形的个数
#     for i in range(1,row+1):#打印三角形,加1是因为range函数的特殊性
#         for j in range(1,row+1-i):
#             print(" ",end="")
#         for k in range(1,i+1):
#             if k not in list1:
#                 print("* " ,end="")
#         print("")

# h = 11
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

# for k in range(11):
#     if k <=4:
#         print(("*"*(2*k+1)).center(33))
#     else:
#         print(("*" * (21-2 * k)).center(33))
#
# i = 1
# while i <= 6:
#     j = 1
#     while j <= 6 - i:  # 第一行4个空格，第二行3个空格，第三行2个空格
#         print(" ", end="")
#         j += 1
#     j = 1
#     while j <= 11:  # *的个数是一定的
#         print("*", end="")
#         j += 1
#     print()
#     i = i + 1
#
# i = 1
# while i <= 6:
#     j = 1
#     while j < 3:
#         print(" "*(j-1), end="")
#         j += 1
#         while j <=11:
#             print("*", end="")
#             j += 1
#
#     print()
#     i = i + 1


if x>y:
    print(x)