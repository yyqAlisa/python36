# 题目1：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
grade = {'小张':99,'小李':88,'小明':66,'小赵':55}
# for name in grade:
#     if grade[name]>=90:
#         print('%s成绩为A'%name)
#     elif grade[name]>=60:
#         print('%s成绩为B' % name)
#     else:
#         print('%s成绩为C' % name)

#输入一个姓名，查询该同学的分值和成绩等级
# for i in range(9999):  #可最多循环9999次
#     name = input('请输入要查询的同学')
#     if name in grade: #如果人名存在
#         if grade[name]>=90:
#             print('%s分数为%s,成绩等级为为A'%(name,grade[name]))
#         elif grade[name]>=60:
#             print('%s分数为%s,成绩等级为为B' % (name, grade[name]))
#         else:
#             print('%s分数为%s,成绩等级为为C' % (name, grade[name]))
#     else:#如果人名不存在
#         print('查询错误')


# 题目2：猜拳游戏 (人机互战)
#        random.randint(x,y) 返回 x 到 y 之间的随机数
# import random #随机数模块
# print(random.randint(0,2))

# 实现三局两胜
import random
computer_win = 0  #电脑赢得次数
user_win = 0  #玩家赢得次数
info = ['石头','剪刀','布']
for i in range(999):
    computer = random.randint(0,2)
    user = int(input('请输入 0 石头 1 剪刀 2 布: '))
    if 2>=user>=0:
        # if (info[computer]=='石头' and info[user] =='剪刀') or (info[computer]=='剪刀' and info[user] =='布') or (info[computer]=='布' and info[user] =='石头'):
        #     print('电脑出了%s，玩家出了%s，电脑胜利'%(info[computer],info[user]))
        if user-computer==1  or user-computer==-2:
            print('电脑出了%s，玩家出了%s，电脑胜利' % (info[computer], info[user]))
            computer_win+=1
        elif computer == user:
            print('电脑出了%s，玩家出了%s，平局' % (info[computer], info[user]))
        else:
            print('电脑出了%s，玩家出了%s，玩家胜利' % (info[computer], info[user]))
            user_win+=1
    else:
        print('请按提示输入范围内的数字')

    if computer_win>=2:
        print('电脑获得最终胜利')
        break  #直接跳出循环
    if user_win>=2:
        print('玩家获得最终胜利')
        break  # 直接跳出循环