# 2.创建多个字典，对于每个字典，都使用一个宠物的名称来给给它命名；
# 在每个字典中，包含宠物的类型及其主人的名字。
# 将这这些字典存储在一个名为pets的列表中，再遍历该列表,并将宠物的所有信息都打印出来。

# pets_nums = int(input('请输入宠物的数量'))
# pets = [{'name':'xxx','type':'zzz','hoster':'mmm'},{},{}]  #在其中创建三个字典  代表三只宠物

# pets = []
# pets_num = int(input('请输入宠物的数量'))
# for i in range(1,pets_num+1):
#     name = input('请输入第%s只宠物的姓名'%i)
#     type = input('请输入第%s只宠物的类型'%i)
#     hoster = input('请输入第%s只宠物的主人'%i)
#     pets.append({'name':name,'type':type,'hoster':hoster})
# print(pets)
# pets = [{'name': 'aaa', 'type': '111', 'hoster': 'a'}, {'name': 'bbb', 'type': '222', 'hoster': 'b'}, {'name': 'ccc', 'type': '333', 'hoster': 'c'}]

# for i in pets:
#     print('%s是一只%s,它的主人是%s'%(i['name'],i['type'],i['hoster']))


dict1 = {'a':111,'b':222,'c':333}
# print(dict1.clear())  #不会返回新的字典，会修改原字典
# print(dict1)
# print(len(dict1))
# print(str(dict1)) #将整个字典转成字符串  包括符号

# dict2 = dict.fromkeys(['aa','bb','cc'],['p2','p3'])  #只能创建值全部一样的键值对
# print(dict2)

# print(dict1.get('aa','未知')) #找得到就返回对应的值，找不到返回第二个参数，默认为None
# print(dict1)
# print(dict1.setdefault('a','未知')) #找得到就返回对应的值，找不到返回第二个参数，默认为None,会新增一个键值对
# print(dict1)

# print(dict1.values())
# print(111 in dict1)
# print(111 in dict1.keys())  #获取所有键名的序列
# print(111 in dict1.values()) #获取所有值得序列
# print(dict1.items())#获取所有 (键，值) 得序列
# for i,j in dict1.items():
#     print(i,j)

# 1.创建一个名为favorite_places的字典。
# 在这个字典中，将三个人的名字用作键；对于其中的每个人，
# 都存储他喜欢的1〜3个地方，用户输入一个地方判断有那些人是喜欢这个地方的；
# 如果三个人都不喜欢这个地方  最终只打印出一句话 :'没人喜欢这个地方'

favorite_places = {'a1':['北京','上海','广州'],'a2':['厦门','重庆','上海'],'a3':['上海','厦门','天津']}
place = input('请输入一个地名')
flag = False #开关（关）
for k,v in favorite_places.items():
    # print(k,v)

    if place in v:
        print('%s喜欢%s' % (k, place))
        flag = True #开关（开）

if not flag:
    print('没人喜欢这个地方')








