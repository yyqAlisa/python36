# str4 = 'hell#$o world11'
# str4 = input('请输入一段字符')
#判断该字符串  特殊符号 字母 数字 空格  各有多少个
# t_nums = 0 #特殊符号的个数
# alnum_nums = 0 #字母出现的个数
# digit_nums = 0  #数字的个数
# space_nums = 0 #空格的个数
# for i in str4:
#     if i.isspace():
#         space_nums+=1
#     elif i.isdigit():
#         digit_nums+=1
#     elif i.isalnum():
#         alnum_nums+=1
#     else:
#         t_nums+=1
# print('特殊符号有%s个，字母有%s个，数字有%s个，空格有%s个'%(t_nums,alnum_nums,digit_nums,space_nums))


# list1 = ['a','b','c','aaa',123,[1,2,3]]
# print(id(list1))
# print(len(list1))
# print(list1[3])  #查询
# print(list1[-1][0])
# print(list1[0:3:2])
#
#
# # list1[0] = 111  #修改元素
# # print(list1)
# # print(id(list1))  #地址不变 才叫修改
#
# # list1.append('bbb') #往末尾追加一个指定元素
# # print(list1)
# # list1.insert(0,222)  #往指定的列表元素之前插入指定的值
# # list1.insert(len(list1),222)   #这样 就是往最末尾追加元素
# # print(list1)
#
#
# list3 = ['a','b','ccc','d','a','aa','aaa']
# # list3.pop(0)  #删除一个指定位置上的元素，超出范围会报错，默认删除最后一个元素
# # for i in range(len(list3)):
# #     list3.pop(0)
# # print(list3)
#
# # list3.remove('aa')  #从左到右 删除一个指定元素，若不存在会报错
# # print(list3)
#
# #1 删除列表中所有  'a' 元素  (利用for循环)

#
# #2  删除列表中所有包含 'a' 字符的元素 (利用for循环)
#
#
# # 创建一个1-100的列表
# # list2 = []
# # print(list(range(1,101,1)))   #开始，结束，步长（默认为1）    如果只写一个参数  代表从0开始到这个数字   前闭后开
# # for i in range(1,101):
# #     list2.append(i)
# # print(list2)])