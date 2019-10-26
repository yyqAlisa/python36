import requests

#GET请求  参数会显示在URL地址当中

# result = requests.get('http://httpbin.org/get')  #测试get请求的网站
# print(result.text)

# par = {'name':'joe','pwd':'123'}
# result = requests.get('http://httpbin.org/get',params= par)  #测试get请求的网站
# print(result.text)


# {
#   "args": {}, #参数
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.22.0"  #身份信息
#   },
#   "origin": "116.226.240.25, 116.226.240.25",
#   "url": "https://httpbin.org/get"
# }

#GET请求添加头文件伪装浏览器
# headers = {
#     # 'referer':''  表示这个请求从哪里来
#     'host'
#     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
# }
#
# result = requests.get('http://httpbin.org/get',headers = headers)  #测试get请求的网站
# print(result.text)

#请求知乎网站
# headers = {
#     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
# }
#
# result = requests.get('http://www.zhihu.com')
# print(result.text)

#解析json数据
# result = requests.get('http://github.com/timeline.json')
# print(result.text)
# print(type(result.text))
# print(result.json())  #将json字符串解析成字典dic
# print(type(result.json()))

#GET请求，获取原始响应内容
#下载音乐
# result = requests.get('http://isure.stream.qqmusic.qq.com/C400003mAan70zUy5O.m4a?guid=8026769632&vkey=EFCB8A0846FCDDC4E506B1AECB8A45BBE33D83181137E484651504F43553955011D424FCBE388B5B9F8A1926A8E2823792CA6FC86DB04513&uin=0&fromtag=3&r=8358679870719936',stream = True).raw.read()
# r1='https://y.qq.com/portal/player.html'
# result = requests.get(r1,stream = True).raw.read()
# with open('aaa.mp3','wb') as file:
#     file.write(result)
#
##下载图片
# result = requests.get('https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3567862917,3810861202&fm=15&gp=0.jpg',stream = True).raw.read()
# with open('aaa.jpg','wb') as file:
#     file.write(result)

#发送cookie
# headers = {
#     'cookie':'id:007'
# }
# result = requests.get('http://httpbin.org/cookies',headers = headers)
# print(result.text)