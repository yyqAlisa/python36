# str1 = 'hello java java'
# new_str1 = str1.replace('java','python')
# print(new_str1)
# print(str1)

# str1_1 = str1[0:str1.find('java')+4]
# str1_2 = str1[str1.find('java')+4:].replace('java','python')
# print(str1_1+str1_2)

# split  以指定的字符串分隔 字符，得到一个列表
# str3 = 'hello world china'
# print(list(str3))
# print(str3.split(' '))
# print(str3.split('world'))

# partition  以指定的字符串作为中间的元素   得到一个长度为3的元组
# print(str3.partition('world'))
# print(str3.partition('hello'))

# join 以指定的字符连接列表的每一个元素 (必须都是字符串)    得到一串字符串
# list1 = ['1','2','3','4']
# print(eval('1+1'))  #能够计算字符串型的公式
# print('%s=%s'%('+'.join(list1),eval('+'.join(list1))))


# lstrip
# str2 = 'ccc  aaa'
# new_str2 = str2.lstrip('c')  #删除最左侧指定的字符  默认为空格
# print(new_str2)

str4 = 'hello world111'
#判断该字符串  特殊符号 字母 数字 空格  各有多少个

print(str4.isspace())  #只有空格返回True
print(str4.isalpha())  #只有字母返回True
print(str4.isdigit()) #只有数字返回True
print(str4.isalnum()) #数字或字母返回True

# if str4.isspace():
#     print(111)
# elif str4.isdigit():
#     print(222)
# elif str4.isalnum():
#     print(333)
# else:
#     print('特殊符号')

str4 = 'hello world111'
t_nums = 0 #特殊符号出现的次数
alnum_nums = 0 #字母出现的次数
digit_nums = 0 #数字出现的次数
space_nums = 0 #空格出现的次数
for i in str4:

    print(i)

    if i.isspace():
        space_nums += 1
    elif i.isdigit():
        digit_nums += 1
    elif i.isalnum():
        alnum_nums += 1
    else:
        t_nums += 1
print('特殊符号有%s个，字母有%s个，数字有%s个，空格有%s个'%(t_nums,alnum_nums,digit_nums,space_nums))