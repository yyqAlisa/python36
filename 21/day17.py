# a = 10
# while a>5:
#     print(a)
#     a-=2


# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%s'%(j,i,i*j),end=' ')
#     print()

# 99乘法表  （while嵌套方式）
# i = 1
# j = 1
# while i<10:
#     while j<i+1:
#         print('%s*%s=%s' % (j, i, i * j), end=' ')
#         j+=1
#     i+=1
#     j = 1
#     print()

# 题目4：3000米长的绳子，每天减一半。问多少天这个绳子会小于5米？
# length = 20
# day = 0
# while length>=5:
#     length/=2
#     day+=1
# print(day)

# 题目4：猜数游戏。预设一个0~9之间的整数，让用户猜一猜并输入所猜的数，
# 如果大于预设的数，显示“太大”；小于预设的数，显示“太小”，如此循环，直至猜中该数，显示“恭喜！你猜中了！”。
# num = int(input('请预设一个0~9之间的整数'))
# u = int(input('请猜一个0~9之间的整数'))
# while True:
#     if num==u:
#         print('恭喜！你猜中了！')
#         break
#     elif u>num:
#         u = int(input('太大，请重新输入'))
#     else:
#         u = int(input('太小，请重新输入'))

# 题目16：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
# num = int(input('请输入一个大于2的整数'))
# s = num
# list1 = []
# for i in range(2,num+1):
#     while num%i==0:
#         list1.append(str(i))
#         num//=i
#     if num==1:
#         break
# print(list1)
# print('%s=%s'%(s,'*'.join(list1)))
# print(num)

