# 有一个列表a[],里面有若干个整数未知。我希望将里面的整数两两做差（即a[1]-a[0],a[3]-a[2]....），
# 并将得数保存在另一个列表b[]中，请问如何实现？

a = [123,12,213,1,312,4]
b = [a[1]-a[0],a[3]-a[2],a[5]-a[4]]
print(b)

tup1 = (1,2,3,4)
print(tup1)
print(type(tup1))
print(len(tup1))
print(tup1[0])
print(tup1[0:3])

list1 = [1]
print(list1)
#
# tup2 = ('a',)
# print(tup2)
#
# tup3 = ('a','v','b')
# tup3[0] = 'aaa'

# s = (1,2,3,4,5,6,7,8,9)
# print(s[0:6])


# dict1 = {1:'a',2:[1,2,3],'aaa':333,(1,2,3):111}
# dict2 = {}  #空字典
# print(type(dict2))
# print(dict1)
# print(type(dict1))
# print(len(dict1))
# print(dict1[2])  #通过键名查询对应的值

# 字典使用人名作为键，每个人的信息用另一个字典来表示，
# 其键”phone”和”addr”分别表示他们的联系电话和地址，
# 重复输入3次，最后将字典打印出来。

# info = {
#     '张三':{'phone':111,'addr':'上海'},
#     '李四':{'phone':222,'addr':'上海2'},
#     '王五':{'phone':333,'addr':'上海3'}
# }
# print(info['张三'])
# print(info['张三']['phone'])
# print(info['李四']['addr'])
# info['张三']['phone'] = 444
# print(info)


# set1 = {2,3,1,4,111,212,131,5,'aaa',(1,2,3),1} #都是不可变数据类型  元素唯一  无序
# print(set1)
# print(type(set1))


# 利用集合的元素唯一性 快速实现去重操作（不考虑顺序）
# list1 = [111,111,22,333,22,333,1,2,3,4,1]
# set2 = set(list1)
# new_list1 = list(set2)
# print(new_list1)

# set3 = {1,2,3}
# set3.add(999)  #增加元素
# print(set3)
# set3.remove(3)  #删除指定元素
# print(set3)

set4 = {1,2,3,4,5,6}
set5 = {3,4,5,6,7,8}

print(set4 | set5) #并集
print(set4 & set5) #交集
print(set5 - set4) #差集

