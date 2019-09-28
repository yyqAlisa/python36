from lxml import etree
import requests

#创建lxml对象
html = etree.HTML(open('web.html',encoding='utf-8').read()) #容错率高
html1 = etree.parse(open('web.html',encoding='utf-8'))
html2 = etree.fromstring(open('web.html',encoding='utf-8').read())

print(html)

#将lxml 对象 字符串序列化
result = etree.tostring(html,pretty_print=True,encoding='utf-8').decode('utf-8')
print(result)

'''
   选取节点
'''
print(html.xpath('//div'))
print(html.xpath('/html/body/div')) # / 从根节点开始查找
print(html.xpath('//div/a'))  # // 从全文中开始查找
print(html.xpath('//div/a/..'))  # .. 查找该节点的父节点
print(html.xpath('//div[@class="left"]/a'))   #[@class ='xxx'] 查找属性
print(html.xpath('//div[@class="right"]/a')[0])   #通过下标获取某个元素
print(html.xpath('//div[@class="right"]/a[1]'))  #返回的是列表通过下标获取某个元素
print(html.xpath('//div[@class="right"]/a[last()]'))  #获取最后一个元素
print(html.xpath('//div[@class="right"]/a[position()<3]'))   #获取前两个元素
print(html.xpath('//div[@id="menu"]/a[span="haha"]'))   #获取a标签里面span的文本
print(html.xpath('//*[@id="menu"]/a[span="haha"]'))   #*表示任意标签
print(html.xpath('//*[@id="menu"]/a[span="haha"]')|'//div[@class="right"]/a[1]') # | 表示标签的结果集
print(html.xpath('//*[@id="menu"]/a[span=11]+//*[@id="menu"]/a[span=50]'))

print(html.xpath('//div[@class="right"]/a[1]/text'))  #里面没有子节点使用text()方法获取
print(html.xpath('string(//div[@class="right"]'))  #有子节点的情况下使用srting()方法获取


'''
               bs4    lxml
   没有子节点  string  text()
   有子节点    text    string()
'''

#获取属性
print(html.xpath('//div[@class="left"]/a[1]/@href'))


