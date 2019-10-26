# def func1(x,y):
#     return x+y(1,2)
#
#
# f = lambda x,y:x+y
# # print(f(1,2))
#
# print(func1(1,f))


# map  映射
# list1 = [1,2,3,4,5]
# list2 = [1,3,4,5,6]
# new_list1 = list(map(lambda x,y:x<y,list1,list2))
# print(new_list1)

# filter  过滤
# list3 = [1,2,3,4,5]
# new_list3 = list(filter(lambda x:x-3,list3))
# print(new_list3)

# reduce  合并
import functools
list4 = [1,2,3,4,5]
r = functools.reduce(lambda x,y:x+y,list4,99)
print(r)

# 案例一：格式化用户的英文名，要求首字母大小，其它字母小写
# names = ['tom','jason','lily','jack']
# new_names = list(map(lambda x:x.title(),names))
# print(new_names)
#
# # 案例二：将用户英文名、年龄、性别三个列表的数据结合到一起，形成一个列表
# ages = [11,12,13,14]
# sex = ['nan','nan','nv','nan']
# info =  list(map(lambda x,y,z:[x,y,z],new_names,ages,sex))
# print(info)
#
# # 案例三：过滤性别为男的用户
# info_f = list(filter(lambda x:x[-1]=='nan',info))
# print(info_f)
# # 案例四：求性别为男的用户的平均年龄
# import functools
# avg_age = round(functools.reduce(lambda x,y:x+y[1],info_f,0)/len(info_f),2)
# print(avg_age)
