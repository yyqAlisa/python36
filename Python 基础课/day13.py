# 1.创建一个名为favorite_places的字典。
# 在这个字典中，将三个人的名字用作键；对于其中的每个人，
# 都存储他喜欢的1〜3个地方，用户输入一个地方判断有那些人是喜欢这个地方的；
# 如果三个人都不喜欢这个地方  最终只打印出一句话 :'没人喜欢这个地方'

# favorite_places = {'a1':['上海','北京','广州'],'a2':['上海','北京','厦门'],'a3':['上海','重庆','厦门']}
# place = input('请输入一个地名')
# flag = False  #开关（关）
# for k,v in favorite_places.items():
#     if place in v:
#         print('%s喜欢%s'%(k,place))
#         flag = True  #改变状态（开）
#
# if not flag:
#     print('没人喜欢这个地方')

# 浅拷贝   第一层内存地址不同，从第二层开始相同
# copy()  切片   copy.copy()  都属于浅拷贝
# import copy  #导入copy 模块   才能在之后使用copy模块里的相关方法
# list1 = [1,2,3,4,5,[6,7,8,[111,222,333]]]
# list2 = copy.copy(list1)
# list2[0] = 111
# list2[-1][0] = 999
# list2[-1][-1][0] = 888
# print(id(list1))
# print('子集列表',id(list1[-1]))
# print(list1)
# print(id(list2))
# print('子集列表',id(list2[-1]))
# print(list2)

# 深拷贝  内存地址完全不同（两者都独立出来）
# import copy  #导入copy 模块   才能在之后使用copy模块里的相关方法
# list1 = [1,2,3,4,5,[6,7,8]]
# list2 = copy.deepcopy(list1)
# list2[0] = 111
# list2[-1][0] = 999
# print(id(list1))
# print('子集列表',id(list1[-1]))
# print(list1)
# print(id(list2))
# print('子集列表',id(list2[-1]))
# print(list2)

# 直接赋值  两者完全一致
# list1 = [1,2,3,4,5,[6,7,8]]
# list2 = list1
# list2[0] = 111
# list2[-1][0] = 999
# print(id(list1))
# print('子集列表',id(list1[-1]))
# print(list1)
# print(id(list2))
# print('子集列表',id(list2[-1]))
# print(list2)


#条件
# a = 5
# if a>1:
#     if a>2:
#         print(11)
#     else:
#         print(22)
# elif a>2 :
#     print(222)
# elif a>3:
#     print(333)
# else:
#     print(444)


# 题目1：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。


# grade = {'小张':99,'小李':88,'小明':66,'小赵':55}
# for i in range(999):
#     name = input('请输入要查询的同学')
#     if name in grade:
#         if grade[name] >= 90:
#             print('%s同学的分数为%s,学习成绩为A' % (name, grade[name]))
#         elif grade[name] < 60:
#             print('%s同学的分数为%s,学习成绩为C' % (name, grade[name]))
#         else:
#             print('%s同学的分数为%s,学习成绩为B' % (name, grade[name]))
#     else:
#         print('查询错误')


# 题目2：猜拳游戏 (人机互战)
#        random.randint(x,y) 返回 x 到 y 之间的随机数
# import random #随机数模块
# print(random.randint(0,2))

import random
computer_win = 0
user_win = 0
info = ('石头','剪刀','布')
for i in range(9999):
    computer = random.randint(0, 2)
    user = int(input('0>石头 1>剪刀 2>布'))
    if 0<=user<=2:
        if (info[computer] == '石头' and info[user] == '剪刀') or (info[computer] == '剪刀' and info[user] == '布') or (info[computer] == '布' and info[user] == '石头'):
            print('电脑出了%s,玩家出了%s,电脑胜利'%(info[computer],info[user]))
            computer_win+=1
        elif computer == user:
            print('电脑出了%s,玩家出了%s,平局'%(info[computer],info[user]))
        else:
            print('电脑出了%s,玩家出了%s,玩家胜利'%(info[computer],info[user]))
            user_win+=1
    else:
        print('请按提示输入范围内的数字')

    if computer_win >=2:
        print('电脑获得最终胜利')
        break
    elif user_win >=2:
        print('玩家获得最终胜利')
        break
