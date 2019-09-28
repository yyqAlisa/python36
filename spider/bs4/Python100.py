from bs4 import BeautifulSoup
import requests

'''
   1.明确需求
      爬取Python100列
         标题
         题目
         程序分析
         源代码
   2.分析源码
      入口地址：https://www.runoob.com/python/python-100-examples.html
      1.获取100道题的a链接
      2.分别请求这个100个链接对应的详细页面
   3.代码实现
'''

# starUrl = 'https://www.runoob.com/python/python-100-examples.html'
# headers = {
#           "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
# }
#
# #请求入口地址，获取100个a链接的href
# response = requests.get(starUrl,headers = headers).content.decode('utf-8')
# # print(response)
#
# #解析 文档
# soup = BeautifulSoup(response,'html.parser')
# # print(soup)
#
# num = 1
# #提取100个a链接
# # print(soup.find(id ='content').ul.find_all('a'))
# link = []
# for i in soup.find(id ='content').ul.find_all('a'):
#     link.append(i['href'])
# print(link[0])
#
# #2.请求100个a链接
# for a in link:
#     print('第{0}道题'.format(num))
#     result = requests.get('http://www.runoob.com'+a,headers = headers).content.decode('utf-8')
#     # print(result)
#
#     #解析源代码
#     html = BeautifulSoup(result,'html.parser')
#     # print(html)
#
#     #提取内容
#     content = {}
#
#     #标题
#     content['title'] = html.find(id = 'content').h1.string
#
#     #题目
#     content['timu'] = html.find(id = 'content').find_all('p')[1].text
#
#     #程序分析
#     content['cxfx'] = html.find(id = 'content').find_all('p')[2].text
#
#     #源代码
#     content['code'] = html.find(class_='hl-main').text
#
#     try:
#         content['code'] = html.find(class_='hl-main').text
#     except:
#         # content['code'] = html.find(class_='pre').text
#         content['code'] = html.find(id = 'content').find(class_='prettyprint prettyprinted').text
#
#     #保存内容
#     with open('python100.text','a+',encoding='utf-8') as file:
#         file.write(content['title']+'\n')
#         file.write(content['timu']+'\n')
#         file.write(content['cxfx']+'\n')
#         file.write(content['code']+'\n')
#         file.write('='*80+'\n')
#
#     num +=1


starUrl = 'https://www.runoob.com/python/python-100-examples.html'
headers = {
          "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}

#请求入口地址，获取100个a链接的herf
response = requests.get(starUrl,headers = headers).content.decode('utf-8')
# print(response)

#解析 文档
soup = BeautifulSoup(response,'html.parser')
# print(soup)


#CSS选择器
num = 1
#提取100个a链接
# print(soup.find(id ='content').ul.find_all('a'))
link = []
for i in soup.select('#content ul a'):
    link.append(i['href'])

#2.请求100个a链接
for a in link:
    print('第{0}道题'.format(num))
    result = requests.get('http://www.runoob.com'+a,headers = headers).content.decode('utf-8')
    # print(result)

    #解析源代码
    html = BeautifulSoup(result,'html.parser')
    # print(html)

    #提取内容
    content = {}

    #标题
    content['title'] = html.select('#content h1')[0].text

    #题目
    content['timu'] = html.select('#content p')[1].text

    #程序分析
    content['cxfx'] = html.select('#content p')[2].text

    #源代码
    content['code'] = html.select('.hl-main')[0].text

    try:
        content['code'] = html.select('.hl-main')[0].text
    except:
        # content['code'] = html.select('.pre').text
        content['code'] = html.select('#content' 'pre').text

    #保存内容
    with open('python101.text','a+',encoding='utf-8') as file:
        file.write(content['title']+'\n')
        file.write(content['timu']+'\n')
        file.write(content['cxfx']+'\n')
        file.write(content['code']+'\n')
        file.write('='*80+'\n')

    num +=1


