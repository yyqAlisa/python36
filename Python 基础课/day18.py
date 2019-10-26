# list1 = []
# for i in range(10):
#     if i>6:
#         for j in range(10):
#             if j>5:
#                 list1.append((i,j))
#
# print(list1)
# #
# #
# # print(list(range(1,101)))
#
#
# list2 = [(i,j) for i in range(10) if i>6 for j in range(10) if j>5]
# print(list2)

# 题目19：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？
# 各是多少？ 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。
# 组成所有的排列后再去掉不满足条件的排列。(用列表推导式)

# list3 = []
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and i!=k and j!=k:
#                 list3.append(i*100+j*10+k)
# print(list3)
#
# list4 = [i*100+j*10+k for i in range(1,5) for j in range(1,5) for k in range(1,5) if i!=j and i!=k and j!=k]
# print(list4)


# 生成器推导式（元组推导式）
# str1 = (i for i in range(1,10))
# print(str1)

# 集合推导式
# set1 = {i for i in range(1,10)}
# print(set1)

# 字典推导式
print(list(zip(range(5),range(5))))
dict1 = {k:v for k,v in zip(range(5),range(5))}
print(dict1)

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
print(dict(zip(list1,list2)))

# {0:0,1:1,2:2,3:3,4:4}

# 题目15： names = ['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe','Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva']
# 找出上述名字中长度大于4的名字,组成列表打印出来.
# 过滤掉长度小于6的字符串列表，并将剩下的转换成大写字母.
names = ['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe','Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva']
new_names = [i.upper() for i in names if len(i)==5]
print(new_names)

#
# 题目18：打印出如下图案（菱形）
#  
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
