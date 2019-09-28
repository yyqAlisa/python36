# 题目5：计算从1到某个值以内所有能被3或者17整除的数的和并输出
# list1 = []
# num = int(input('请输入大于1的整数'))
# for i in range(1,num):
#     if i%3==0 or i%17==0:
#         list1.append(i)
# print(list1)
# print(sum(list1)) #对列表进行求和，每个元素都必须是number

# 题目11：最多循环问99次  “老婆，你爱我吗？”，如果回答的是“爱”，那么就结束循环，否则就继续问。用程序描述这个故事
# 如果最终没有拿到我要的答案，回复一句话 “对不起打扰了”

# 方式一
# flag = False
# for i in range(3):
#     q = input('老婆，你爱我吗？')
#     if q=='爱':
#         flag = True
#         print('老婆我也爱你')
#         break
#     else:
#         print('在给你一次机会')
#
# if not flag:
#     print('对不起打扰了')

# 方式二  利用与for 对应的else关键字效果
# for i in range(3):
#     q = input('老婆，你爱我吗？')
#     if q=='爱':
#         print('老婆我也爱你')
#         break
#     else:
#         print('在给你一次机会')
# else:  #只要break触发，它就不触发；反之，触发
#     print('对不起打扰了')


# 题目1：使用Python编程，求1～100间所有偶数的和。
# list2 = []
# for i in range(2,101,2):  #（开始，结束，步长）
#     list2.append(i)
# print(sum(list2))

# 题目14：输出1到100之间所有的质数
# list1 = []
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             print('%s不是质数'%i)
#             break
#     else:
#         print('%s是质数' % i)
#         list1.append(i)
# print(list1)

