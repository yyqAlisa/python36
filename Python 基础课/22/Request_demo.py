import requests


r = requests.get('http://2.python-requests.org/zh_CN/latest/user/quickstart.html')

t = r.status_code

print(t)

print(r.text)

