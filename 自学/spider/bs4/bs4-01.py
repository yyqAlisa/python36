from bs4 import BeautifulSoup
import requests

# response = requests.get('http://www.baidu.com').content.decode('utf-8')
# print(response)

#使用BeautifulSoup 解析 请求到的Html文档
# soup = BeautifulSoup(response,'html.parser')  #html.parser解析方法
# print(soup)
# print(type(soup))

# soup = BeautifulSoup(response,'html.parser')  #lxml解析方法  解析速度快，容错率高
# print(soup)
# print(soup.prettify())  #格式美化

#解析 web.html  #这里么有本地文件web.html
result = BeautifulSoup(open('web.html',encoding='utf-8'),'html.parser')
# print(result)

#四大对象之Tag
# print(result.html.body)  #默认会找第一个叫这个的Tag
# print(type(result.html.body.div.span))

#四大对象之NavigableString  标签中的文本
# print(result.html.body.div.span.string.a)  #通过string获取标签中的文本，使用string必须保证里面没有子标签
# print(type(result.html.body.div.span.string.a))
#
# print(result.html.body.div.span.strings)  #有子标签的情况下使用 可以获取所有的文本内容
# strs = result.html.body.div.span.strings
# for i in strs:
#     print(i)

'''
   遍历文档树
'''
#获取直接节点
# print(result.html.body.contents)   #可以获取该节点下的所有子节点，包括换行符
# print(result.html.body.div.contents[3])
# print(result.html.body.div.children)
# for i in result.html.body.div.children:
#     print(i)

#递归获取子孙节点
# print(result.html.body.div.descendants)
# for i in result.html.body.div.descendants:
#     print(i)

#获取标签内容
# print(result.html.body.div.span.a.string) #没有子节点的情况下
# print(result.html.body.div.span.text)  #获取该标签下的所有文本

#获取当前节点的父节点
# print(result.html.body.div.span.a)
# print(result.html.body.div.span.a.parent.parent)
# print(result.html.body.div.span.a.parents)
# for i in result.html.body.div.span.a.parents:
#     print(i)

#获取兄弟节点  可以自主选择你需要的标签节点
# print(result.html.body.div.next_sibling)

#1.发送请求获取源码 2.解析源码 3.提取相关标签以及文本内容



#find_all 获取所有的节点
# print(result.find_all('span'))  #传递字符串 表示标签名
# print(result.find_all(name = 'a'))
# print(result.html.body.div.find_all('span')) #获取第一个div里所有的span标签
#
# print(result.find_all(['span','a']))  #获取多个标签
# print(result.find_all(id = 'header'))
# print(result.find_all(class_ = 'left'))
# print(result.find_all(class_ = 'left'),attrs = {'name':'aa'})  #attrs添加属性条件


#标签选择器 id选择器 class选择器 就是相当于给标签取名字
#id的名称是不能重复的 class可以重复

# print(result.find_all(text = 'haha'))  #不建议

#find 查找单个节点
# print(result.find(class_ = 'right').find_all('a')[2:]) #进行定位
# for i in result.find(class_ = 'right').find_all('a')[2:]:
#     print(i.string)

#获取属性
# print(result.find(class_ = 'right').find_all('a')) #进行定位
# for i in result.find(class_ = 'right').find_all('a'): #提取属性
#      print(i['href'])  #第一种
#      print(i.string)
#      print(i.attrs['href'])  #第二种

# print(result.find(class_ = 'right').find_all('a',limit = 2))

'''
   CSS选择器
'''
#1.通过标签名查找
print(result.select('a'))
print(result.find_all('a'))

#2.通过类名查找
print(result.select('.left'))   #都是保存在列表当中
print(result.find(class_='.left'))

# #content  id = 'content'
# .left  class = 'left'

#3.通过id查找
print(result.select('#menu'))   #都是保存在列表当中
print(result.find(id='menu'))

#4.通过属性查找
print(result.select('a[name="aa"]'))  #都是保存在列表当中
print(result.find(name='a',attrs={'name':'aa'}))

#5.组合查找
print(result.select('#content .left'))
print(result.find(id='content').find_all(class_='left'))

#6.获取内容
print(result.select('a[name="aa"]')[0].get_text)  #第一种
print(result.select('a[name="aa"]')[0].text)   #第二种

#7.获取属性
print(result.select('a[name="aa"]')[0]['href'])  #第一种
print(result.select('a[name="aa"]')[0].attrs['href'])   #第二种



