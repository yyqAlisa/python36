# 创建一个列表，用于存储同学姓名。依次访问该列表中的元素。
# 并且将老师和班主任的姓名添加至列表的开头和末尾。
# 将每个同学的姓名打印出来，并且添加一句问候语。
# names = []
# student_nums = int(input('请输入同学的数量'))
# for i in range(1,student_nums+1):
#     student_name = input('请输入第%s位同学的姓名'%i)
#     names.append(student_name)
# print(names)
# names.append('班主任')
# names.insert(0,'老师')
# print(names)

# 遍历方式1
# for i in names[1:-1]:
#     print(i)

# 遍历方式2
# for i in names:
#     if i !='老师' and i!='班主任':
#         print('%s同学你好'%i)


# 字典的使用  增删改查
dict1 = {'a':111,'b':222,3:333,4:'444'}
print(dict1)
# k = input('请输入键名')
# if k in dict1:
#     print(dict1[k])  # 通过存在的键名 查询对应的值
#     v = input('请输入一个新的值')
#     dict1[k] = v  #修改对应键名的值
#     print(dict1)
#
# else:
#     dict1[k] = 888  #新增键值对
#     print(dict1)
#
# del(dict1['a'])  #删除键名为 a 这个键值对
# print(dict1)

# 2.创建多个字典，对于每个字典，都使用一个宠物的名称来给给它命名；
# 在每个字典中，包含宠物的类型及其主人的名字。
# 将这这些字典存储在一个名为pets的列表中，再遍历该列表,并将宠物的所有信息都打印出来。

pets_nums = int(input('请输入宠物的数量'))
# pets = [{'name':'xxx','type':'zzz','hoster':'mmm'},{},{}]  #在其中创建三个字典  代表三只宠物
pets = []
print(pets_nums)
for i in range(1,pets_nums+1):
    name=input('请输入第%s宠物的姓名'%i)
    type = input('请输入第%s宠物的类型' %i)
    hoster = input('请输入第%s宠物的主人' %i)
    pets.append({'name':name,'type':type,'hoster':hoster})
print(pets)



