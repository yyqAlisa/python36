# 石头剪刀布
# import random
#
# player = int(input('请输入 石头 1 剪刀 2 布 3 :'))
# computer = random.randint(1, 3)
#
# print("player输入的是：%d" % player)
# print("computer 输入的是：%d" % computer)
#
# if ((player == 1 and computer == 2)
#         or (player == 2 and computer == 3)
#         or (player == 3 and computer == 1)):
#
#     print('电脑弱爆了')
# elif player == computer:
#     print('太心有灵犀了')
# else:
#     print('不服，再来一盘')

# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%-2s'%(j,i,i*j),end=' ')
#     print()

row = 1
while row <=9:
    col = 1
    while col <=row:
        print('%d*%d=%d'%(row,col,row*col),end='\t ')
        col += 1
    print('')
    row += 1


