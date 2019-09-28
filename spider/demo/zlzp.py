import requests
from lxml import etree
import  time

'''
   1.需求分析
       title gsmc gz address jy xl fuli
       入口地址：https://www.zhaopin.com/
       
   2.源码分析
       获取所有的职位分类标签：入口地址：//div[@class='zp-jobNavigater__pop--list']/a
       职位详细列表：https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&at=0a113b3ab5e942f5a3feff8e843271f2&rt=ceb33e3f374a40ad84a1dc8123c43dcc&_v=0.30592667&userCode=693340701&x-zp-page-request-id=2cfd0f173f9b46daa1c48224f58be4fd-1569571179550-639696&x-zp-client-id=472f0165-584c-46e4-bf61-408b0da0dbac

   3.代码实现
'''


#1.获取职位标签
def get_job_tag(url):

    headers = {
        #浏览器的信息  身份信息
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }

    response = requests.get(startUrl,headers=headers).text

    #解析源码
    html = etree.HTML(response)

    #获取所有的职位分类标签
    job_tag = html.xpath("//div[@class='zp-jobNavigater__pop--list']/a/text()")
    return job_tag

#2.获取职位信息
def get_job_info(url,start,kw):
    headers = {
        # 浏览器的信息  身份信息
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }

    info_html = requests.get(infoUrl, format(start,kw), headers=headers).text.json()
    print(type(info_html))

    job_Dic = {}

    for i in info_html['data']['result']:
        job_Dic['city'] = i['city']['items'][0]['name']
        job_Dic['companyName'] = i['company']['name']
        job_Dic['companySize'] = i['company']['size']['name']
        job_Dic['companyType'] = i['company']['type']['name']
        job_Dic['emplType'] = i['emplType']
        job_Dic['jobName'] = i['jobName']
        job_Dic['jobType'] = i['jobType']['dispaly']
        job_Dic['salary'] = i['salary']
        job_Dic['welfare'] = i['welfare']
        job_Dic['updateDate'] = i['updateDate']
        job_Dic['workingExp'] = i['workingExp']['name']

        #保存数据
        if unique_data(job_Dic):
            job_Dic = clearn_data(job_Dic)
            save_data(job_Dic)
            time.sleep(0.5)


    return print(info_html['data']['numFound'])


#过滤重复数据
companyList = []
jobNameList =[]
def unique_data(data):
    if (data['jobName'] in jobNameList) & (data['companyName'] in companyList):
        return False
    else:
        companyList.append(data['companyName'])
        jobNameList.append(data['jobName'])
        return data

#数据清洗
def clearn_data(data):
    #welfare
    data['welfare']='/'.join([str(i) for i in data['welfare']])

    #companySize
    data['companySize']=data['companySize'].strip('人')
    return  data


#保存数据
def save_data(data):
    data = '::'.join([str(i) for i in data.values()])
    print(data)

    with open('zlzp.text','a+',encoding='utf-8') as file:
        file.write(data+'\n')

if __name__ == '__main__':

    '''
       一：请求首页 
    '''

    startUrl = 'https://www.zhaopin.com/'
    job_tag_list = get_job_tag(startUrl)

    print(job_tag_list)

    '''
       二：获取职位详细列表页面
    '''
    start = 0
    page = 1
    while True:
        infoUrl = "https://fe-api.zhaopin.com/c/i/sou?star={0}pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw={01}&kt=3"
        numFound = get_job_info(infoUrl,start,job_tag_list[0])

        print('第{0}页'.format(page))

        if start < numFound:
            start+=60
            page+=1
            time.sleep(1)
        else:
            break











# "https://fe-api.zhaopin.com/c/i/sou?" \
# "pageSize=90&cityId=538&salary=0,0&workExperience=-1" \
# "&education=-1&companyType=-1&employmentType=-1&" \
# "jobWelfareTag=-1&kw=%E5%A4%96%E8%B4%B8%E4%B8%9A%E5%8A%A1%E5%91%98&" \
# "kt=3&=0&at=0a113b3ab5e942f5a3feff8e843271f2&" \
# "rt=ceb33e3f374a40ad84a1dc8123c43dcc&_v=0.36979582&userCode=693340701&" \
# "x-zp-page-request-id=c088f8da95b34fc9911476d126bdf7db-1569571881519-247334&" \
# "x-zp-client-id=472f0165-584c-46e4-bf61-408b0da0dbac"

# pageSize: 90
# cityId: 538
# salary: 0,0
# workExperience: -1
# education: -1
# companyType: -1
# employmentType: -1
# jobWelfareTag: -1
# kw: 外贸业务员
# kt: 3
# at: 0a113b3ab5e942f5a3feff8e843271f2
# rt: ceb33e3f374a40ad84a1dc8123c43dcc
# _v: 0.36979582
# userCode: 693340701
# x-zp-page-request-id: c088f8da95b34fc9911476d126bdf7db-1569571881519-247334
# x-zp-client-id: 472f0165-584c-46e4-bf61-408b0da0dbac