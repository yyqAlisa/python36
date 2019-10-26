# 算术运算符
num1 = 10
num2 = 5
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1//num2)
print(num1**2)
print(num1%num2)
print(num1%num2 == 0)
if num1%num2 == 0:
    print(num1//num2)
else:
    print(num1 / num2)

# 赋值运算符
a = 1
b = 2
a += 1
a = a+1

a+=b
a = a+b
print(a)

#比较运算符
a = [2,4,3]
b = [2,3]
print(a == b)
print(a != b)
# 字符串之间比较大小  z>a>Z>A
print(a > b)
print(a >= b)

# 逻辑运算符
print(True and False)
print(False or True)
print(not True)
print(1 and 0)
print(0 or 2)
print(not 2)
print(bool(' '))

# 输入
name = input('请输入姓名') #不管输入什么数据  接收到都是字符串
print(name)
print(type(name))
num1 = input('请输入第一个数字')
num2 = input('请输入第二个数字')
print(int(num1)+int(num2))

# 输出
print(111,222,333,sep='\n',end='=\n')
print(111)
print(222)