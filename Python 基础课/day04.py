str1 = '你好123'
print(str1[0])
print(str1[0:2]) #前闭后开
print(str1[0:4:2]) #步长正代表从开始向右  负代表向左 不写默认为1
print(str1[3:0:-2])
print(str1[3::-1])

str2 = 'hello world'
print(str2[0:5]) #hello
print(str2[len(str2)-1:-6:-1])#dlrow
print(str2[4::-1])#olleh
print(str2[::-2])#drwolh

str3 = '你好'
str4 = 'china'
print(str3 +' ' +str4)
new_str = str3 +' '+str4 #拼接
print(new_str)

print('-'*30) #复制

#列表
list1 = [1.1,'你好',True,4,[1,2,3,4]]
print(list1[-1][0])
list2 = [1,1,2]
print(id(list2))
print(type(list1))
print(len(list1))
print(list1[0])
print(list1[0:4])
print(list1[4::-2])

new_list =list1 +list2
print(list1)

list2[0]=111 #列表式可变的
print(list2)
print(id(list2)) #可查看内存地址 因为是可变数据类型 修改里面的元素 整个数据的内存地址不变

str3 = 'aaa'
print(id(str3))
str4 = 'bbb'
print(id(str4)) #地址发生了变化，说明不是同一个内存地址了

