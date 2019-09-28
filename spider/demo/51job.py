import requests
from lxml import etree
import time

'''
   1.需求分析
      获取详细的招聘内容
           职位名 公司名 工作地点 薪资 发布时间
           入口地址：https://search.51job.com/
   2.源码分析
      1)获取所有行的数据：//div[@class='el'] 
      2)职位名：//div[@class='el']/p/span/a
      3)公司名：//div[@class='el']/span/a
      4)工作地点：//div[@class='el']/span[@class='t3']
      5)薪资：//div[@class='el']/span[@class='t4']
      6)发布时间：//div[@class='el']/span[@class='t5']
      7)获取下一页://div[@class='p_in']/ul/li[@class='on']
   3.代码实现
'''

'''
   一：请求入口地址
'''
starUrl = 'https://search.51job.com/'

headers = {
          "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}

page=1

while True:
    num=1
    response = requests.get(starUrl,headers = headers).text

    '''
       提取内容
    '''
    #解析源码
    html = etree.HTML(response)

    #获取所有行
    contents = html.xpath("//div[@class='el']")

    #获取下一页
    nextPage = html.xpth("//div[@class='dw_page']")

    #遍历获取每一行的内容
    jobDic = {}
    for i in contents:
        jobDic['title']=i.xpth("//div[@class='el']/p/span/a")
        jobDic['company'] = i.xpth("//div[@class='el']/span/a")
        jobDic['address'] = i.xpth("//div[@class='el']/span[@class='t3']")
        jobDic['salary'] = i.xpth("//div[@class='el']/span[@class='t4']")
        jobDic['date'] = i.xpth("//div[@class='el']/span[@class='t5']")

        print('第{0}页第{1}条信息'.format(page,num))

        num+=1


        with open('51job.text','a+',encoding='utf-8') as file:
            file.write(jobDic['title']+'::')
            file.write(jobDic['company']+'::')
            file.write(jobDic['address']+'::')
            file.write(jobDic['salary']+'::')
            file.write(jobDic['date']+'\n')

        time.sleep(0.5)

    # 翻页 获取下一页信息
    if nextPage[0] == 'on':
        break
    else:
        starUrl = 'https://search.51job.com/' + nextPage[0]
        page += 1
