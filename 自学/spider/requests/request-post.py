import requests

#post 提交参数
# data = {'user':'joe','id':'007'}
# result = requests.post('http://httpbin.org/post',data = data)
# print(result.text)

#session
# s = requests.sessions()
# res = requests.get('http://www.mywbs.com/setcookie')
# print(res.text)

#刚刚设置好了cookie，现在看看它设置的是什么
# res = requests.get('http://www.mywbs.com/cookie')
# print(res.text)

#这是两个独立的请求

#代理