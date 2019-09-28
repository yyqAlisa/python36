import requests
starUrl = 'https://www.runoob.com/python/python-100-examples.html'
headers = {
          "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}

#请求入口地址，获取100个a链接的href
response = requests.get(starUrl,headers = headers).content.decode('utf-8')
print(response)
