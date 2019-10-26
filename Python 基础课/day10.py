list3 = ['a','b','ccc','d','a','a','aa','aaa']
new_list3 = []
#删除所有元素
# for i in range(len(list3)):
#     list3.pop(0)
# print(list3)

# 1 删除列表中所有  'a' 元素  (利用for循环)
# for i in list3:
#     if i!='a':
#         new_list3.append(i)
# print(new_list3)

# 2  删除列表中所有包含 'a' 字符的元素 (利用for循环)

for i in list3:
    # 方式一
    if 'a' not in i:
        new_list3.append(i)

# print(new_list3)

    # 方式二
    if i.count('a') == 0:
        new_list3.append(i)
print(new_list3)


# list1 = ['aa','b','c','d']
# str2 = 'aaaa'
# del(list1[-1])
# del(list1[::2])
# del(list1)  #释放内存
# str1 = 'aaa'
# del(str1)
# print(list1)
# print('a' in str2)

# 字符串比较大小   z>a>Z>A
# list2 = [11,2,2312,3,123,123,21,33]
# print(max(list2))  #列表中所有元素的数据类型相同
# print(min(list2))  #列表中所有元素的数据类型相同

# 对调列表中最大最小值得位置  假设最大最小值是唯一的
# max_num = max(list2)
# min_num = min(list2)
# max_num_index = list2.index(max_num)
# min_num_index = list2.index(min_num)
# list2[max_num_index] = min_num
# list2[min_num_index] = max_num
# print(list2)


# 要注意列表是否是发生了变化
# list2[list2.index(max(list2))]=min(list2)
# print(list2)
# list2[list2.index(min(list2))]=max(list2)
# print(list2)



# list3 = [1,2,3]
# list4 = [2,3,4]
# print(list3+list4) #返回新列表，原列表没有发生变化
#
# print(list3.extend(list4)) #没有返回新的列表  所以直接打印为 None
# print(list3)  #改变原列表

# list5 = [1,2,3]
# list5.clear() #清空列表元素
# print(list5)
# list6 = list5.copy() #复制列表
# print(list6)

# list7 = [1,2,3,5,7,9,4,8]
# list7.sort(reverse=True) #默认升序  列表里的元素数据类型必须一致
# print(list7)
# list7.reverse() #直接反向排序
# print(list7)

# 创建一个列表，用于存储同学姓名。依次访问该列表中的元素。
# 并且将老师和班主任的姓名添加至列表的开头和末尾。
# 将每个同学的姓名打印出来，并且添加一句问候语。
#
# names = []
# students_nums = int(input('请输入同学的数量:'))
# print(students_nums)
#
# for i in range(1,students_nums+1):
#     student_name = input('请输入第%s位同学的姓名 ' %i)
#     names.append(student_name)
# print(names)
# names.append('班主任')
# names.insert(0,'老师')
# print(names)
#
# for i in names[1:-1]:
#     print(i)
#
# for i in names:
#     if i!='班主任' and i!='老师':
#         print('%s同学你好'%i)






# def add(a , b ):
#     c = a + b
#     return c
#
#
# def test1(a , b ):
#     c = a * b
#     return c
#
#
# c = add(2,3)
# print(c)
# print(test1(10,2))

print(help(str))

