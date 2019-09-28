name = '小明'#input('请输入姓名')
age = 18 #int(input('请输入年龄'))
hetght = 178.5 #float(input('请输入身高'))

# print(name+'今年'+str(age)+'岁,身高'+str(hetght)+'cm')
# 格式化输出
# %s 以字符串型显示  %-10s 最少占10个长度  左对齐
# %d 以整数显示 %+010d 最少占10个长度  - 左对齐   + 数字前带+符号   用0来填充空格
#  %f 以浮点数显示  默认以6位小数显示    %+015.2f  最少占15个长度  - 左对齐   + 数字前带+符号   用0来填充空格  四舍五入保留两位小数
# print('%-10s今年%s岁，身高%scm'%(name,age,hetght))
# print('%s今年%+010d岁，身高%scm'%(name,age,hetght))
# print('%s今年%s岁，身高%+015.2fcm'%(name,age,hetght))

# str1 = 'aaabcdedfgabc'
# print(str1.find('a'))  #找得到返回第一个符合条件的下标值，找不到返回-1  只能用在字符串上
# print(str1[1:].find('a'))
# print(str1.find('a',2,10))  #默认整体，可以限制范围， 前闭后开
# print(str1.count('aa')) #统计出现的个数（字符不会重复使用）
#  #找不到会报错。所以小心使用
#
# list1 = ['aaa','bbb','ccc']
# print(list1.index('aaa'))  #index 可使用在除字符串以外的数据类型
# print(list1.count('a'))

# str2 = 'aaaaaa hello world aaaaaa'  #利用切片 集合 字符串内置方法实现 得到 new_str2
# new_str2 = 'aaaaaa hello 你好 world aaaaaa'


str3 = 'hello world'
str4 = '你好'
# str3_1 = str3[0:6]
str3_1 = str3[0:str3.find('world')]
print(str3_1)
str3_2 = str3[str3.find('world'):]
print(str3_2)
print(str3_1 + '你好 ' + str3_2)
