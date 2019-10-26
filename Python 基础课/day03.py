#可变数据类型
#list dic
# 不可变数据类型
#number string tuple
num1 = 111  #  整数
print(num1)
print(type(num1))
num2 = 111.1 #浮点数
print(num2)
print(type(num2))

bool1 = True #布尔值
bool2 = False
print(bool1)
print(type(bool1))
print(num1+num2)

print(int(num1+num2)) #将浮点数转化成整数

float1 = num1 + num2  #将浮点数转化成整数
print(int(float1))
print(float1)

int1 = 111+222  #将整数转化成浮点数
print(float(int1))

print(bool(1)) #转为布尔值，除了0以外的所有数字都为True

#字符串 string
str1 = '111'
print(type(str1))



print(str1+'222')

print('你好'+'111')

str2 = "你好"
print(str2)
print(type(str2))

str3 = 'i\'\'m'
print(str3)

print('hello world')
print('\'hello world\'')
print('\'hello,\'tom\\\'')

str5 = '你好123'
print(len(str5)) #返回数据长度
print(str5[0])   #索引从0开始（必须是整数）能对应的找到相应的字符
print(str5[4])
print(str5[-1])



