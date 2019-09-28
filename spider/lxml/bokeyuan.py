from lxml import etree
import requests
import time

'''
   1.明确需求
      1)帖子标题
      2)帖子内容
   2.分析源码
      1)入口地址：https://www.cnblogs.com/
      2)获取帖子链接: //div[@class='post_item_body']/h3/a
      3)获取下一页://div[@class='pager']/a[last()]/text    获取文本及href属性
                  //div[@class='pager']/a[last()]/@href
                  
      4）帖子标题: //*[@id='cb_post_title_url']
      5）帖子内容: string(//*[@id='cnblogs_post_body'])
   3.代码实现
'''

'''
   一：发送请求，获取帖子的Url
'''
starUrl = 'https://www.cnblogs.com/'
headers = {
         "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}

#请求入口地址
response = requests.get(starUrl,headers = headers).text
# print(response)

#解析源代码
html = etree.HTML(response)

#获取帖子Url
href = html.xpath('//div[@class="post_item_body"]/h3/a/@href')

#获取下一页的文本及Url
nextPage = html.xpath('//div[@class="pager"]/a[last()]/text')
nextPageUrl = html.xpath('//div[@class="pager"]/a[last()]/@href')
# print(nextPageUrl)

'''
   二：获取每一篇帖子的内容及标题
'''
num = 1
for i in href:

    result = requests.get(href[0],headers = headers).text

    #解析源码
    contents = etree.HTML(result)

    #提取帖子标题
    title = contents.xpath('//*[@id="cb_post_title_url"]')

    #提取帖子内容
    info = contents.xpath('string(//*[@id="cnblogs_post_body"])')
    # print(type(info))

    '''
       三：保存内容
    '''
    page = 1
    with open('cnblogs.txt','a+',encoding='utf-8') as file:


        file.write(title+'\n')
        file.write(info[0]+'\n')
        file.write('='*80 +'\n')
        # print('第{0}页第{1}篇帖子'.format(page,num))
        time.sleep(0.5)
        num+=1



    if nextPage[0] == 'next >':
        starUrl= 'https://www.cnblogs.com/'+nextPageUrl[0]
        page+=1
        time.sleep(1)
    else:
        break
