# file_a = open('./t/a.txt','r',encoding='utf8')
# file_a.write('111')
# print(file_a.read()) #读取文件内容
# file_a.close() #必须执行才能关闭文件

#r模式  只能读取不能写入,无法创建新文件
# with open('./t/b.txt','r',encoding='utf8') as file_a:  #会在适当的地方自动关闭
#     print(file_a.tell())
#     file_a.seek(7)  #设置游标位置（字节）  一个中文等于3个字节
#     print(file_a.read())
#     print(file_a.tell()) #设置游标位置（字节）

#r+模式  能读取能写入,无法创建新文件
# with open('./t/b.txt','r+',encoding='utf8') as file_a:  #会在适当的地方自动关闭
#     file_a.seek(3)
#     file_a.write('周杰伦') #会从游标位置开始按字节长度替换原有内容

#w模式  只能写入不能读取,可以创建新文件,在打开时会直接清空原有内容
# with open('./t/b.txt','w',encoding='utf8') as file_b:  #会在适当的地方自动关闭
#     file_b.write('22')

#w+模式  能写入能读取,可以创建新文件,在打开时会直接清空原有内容
# with open('./t/b.txt','w+',encoding='utf8') as file_b:  #会在适当的地方自动关闭
#     print(file_b.read())
#     file_b.write('22')
#     file_b.seek(0)
#     print(file_b.read())

#a模式  只能写入不能读取,末尾追加,可以创建新文件
# with open('./t/c.txt','a',encoding='utf8') as file_c:  #会在适当的地方自动关闭
#     print(file_c.tell())
#     file_c.seek(0)
#     file_c.write('222')

#a+模式  能写入能读取,末尾追加,可以创建新文件,开始时游标位置在开头，当要执行 write 方式，游标会自动移动到最末尾
# with open('./t/c.txt','a+',encoding='utf8') as file_c:  #会在适当的地方自动关闭
#     print(file_c.tell())
#     print(file_c.read())
#     print(file_c.tell())
#     file_c.seek(0)
#     file_c.write('222')

# 二进制 读取图片 生成一张新图片
# with open('./images/timg.jpg','rb') as file_image:  #会在适当的地方自动关闭
#     old_image = file_image.read()
#     with open('./images/new_timg.jpg','wb') as file_image_new:
#         file_image_new.write(old_image)


# 文章中间插入，开头插入，替换 等效果的实现方式
# with open('./t/c.txt','r',encoding='utf8') as file_c_r:
#     old_txt = file_c_r.read()
#     new_txt = '444'+old_txt
#     with open('./t/c.txt', 'w', encoding='utf8') as file_c_w:
#         file_c_w.write(new_txt)


# with open('./t/d.txt','r+',encoding='utf8') as file_d:
#     # file_d.write('111\n')
#     # file_d.write('222')
#     # print(file_d.readlines())  #读取多行内容，以列表显示
#     file_d.writelines(['1111','222\n','333'])


# 题目3:访客：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写
# 入到文件guest.txt 中。

#
# with open('./guest.txt','a',encoding='utf8') as file_guest:
#     name = input('请输入你的名字:')
#     file_guest.write(name+'\n')


# 题目4:访客名单：编写一个while 循环，提示用户输入其名字。用户输入其名字后，
# 在屏幕上打印一句问候语，并将一条访问记录添加到文件guest_book.txt 中。确保这个
# 文件中的每条记录都独占一行。

# whil True:
#     names = input("请输入你的名字:")
#     """输入#号结束名字输入"""
#     if names=='#':
#         break
#     with open('./guest_book.txt','a',encoding='utf8') as file_guest_book:
#         file_guest_book.write(names+'你好'+'\n')

# 题目5:关于编程的调查：编写一个while 循环，询问用户为何喜欢编程。每当用户输
# 入一个原因后，都将其添加到一个存储所有原因的文件中。
#
while True:
    with open('./question.txt','a',encoding='utf8') as question:
        q = input('提问 ：#代表结束')
        if q == '#':
            break
        question.write(q+'\n')
        with open('./answer.txt','a',encoding='utf8') as answer:
            a = input('回答')
            answer.write(a+'\n')



