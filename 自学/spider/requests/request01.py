import requests

#请求北风网
result = requests.get('http://www.beifeng.com')
# print(type(result))
# print(result.status_code)  #查看返回的状态码 200 表示请求成功
# print(result.encoding)     #网站编码
# print(result.cookies)
print(result.text)  #网站源代码
# print(result.content.decode('utf-8'))

