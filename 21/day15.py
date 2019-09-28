# list1 = ['a','b','c']
# for i in list1:
#     print(i)

# for i in range(10):
#     print(i)

# for i,j in [(1,2),(2,3)]:
#     print(i,j)

# list2 = [1,2,3,4,5]
# for i in list2:
#     for j in list2:
#         print(i,j)


# 99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%-2s'%(j,i,i*j),end=' ')
#     print()

# 题目19：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？
# 各是多少？ 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。
# 组成所有的排列后再去掉不满足条件的排列。

# list3 = []
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and j!=k and i!=k:
#                 # list3.append(i*100+j*10+k)
#                 list3.append(int(str(i)+str(j)+str(j)))
# print(list3)
# print(len(list3))


# for i in range(10):
#     for j in range(10):
#         if i==5 and j==5:
#             # break  #跳出当前这一层循环,无法直接跳出多重循环
#             continue  #跳过当前小循环，进入下一个元素
#         print(i,j)
# if i==5 and j==5:
#     break


# 题目5：计算从1到某个值以内所有能被3或者17整除的数的和并输出


# i = int(input('请输入值'))
# list1=[]
# for i in range(0,i+1):
#     if i%3 == 0 or i%17 == 0:
#         list1.append(i)
# print(list1)
# print(sum(list1))

# 题目11：最多循环问99次  “老婆，你爱我吗？”，如果回答的是“爱”，那么就结束循环，否则就继续问。用程序描述这个故事

# for i in range(0, 99):
#     tmp = input("老婆，你爱我吗？")
#
#     if tmp =="爱":
#         print("我也爱你")
#         break
#     else:
#         print('再给你一次回答的机会')

# 题目1：使用Python编程，求1～100间所有偶数的和。

# 方法一：
# a = 0
# for i in range(1,101):
#     if i%2 == 0:
#         # print(i)
#         a+=i
# print(a)

# 方法二：
# list2=[]
# for i in range(2,101,2):
#     list2.append(i)
# print(sum(list2))

# 题目14：输出1到100之间所有的质数

list3 = []
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            print('%s不是质数' % i)
    else:
        print('%s是质数' % i)
        list3.append(i)

print(list3)

