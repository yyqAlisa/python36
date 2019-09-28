import re

'''
   正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定的字符、
   及这些特定字符的组合，组成一个"规则字符串"，
   这个"规则字符串"用来表达对字符串的一种过滤逻辑
'''

# 正则表达式进行格式验证
# 字母开头、字母数字下划线  6 18
# 用户名：
# 密码：6-18  规则字符串

#正则表达式如何制定规则


'''
   compile
'''

# pattern = re.compile('\W?')
# print(type(pattern))

'''
   match  只匹配开头
'''
# pattern =re.compile('\d')  #1个数字
# strs = '1abc'
# print(re.match(pattern,strs).group())  #查看匹配结果需要使用 group
# #如果符合条件使用group 返回匹配结果

# pattern =re.compile('(\d)[a-z]+(\d)')
# strs = '1abc2fsfs'
# print(re.match(pattern,strs).group(0))  #返回完整的正则表达式的匹配结果
# print(re.match(pattern,strs).group(1))  #返回第一个分组的匹配的结果
# print(re.match(pattern,strs).group(2))  #返回第二个分组的匹配结果

'''
   search  
'''
# pattern =re.compile('(\d)[a-z]+(\d)')
# strs = 'MMMfdfdsga1abc2fsfsNNN3abc4KK'
#使用match  match只匹配开头部分
# print(re.match(pattern,strs))

#使用search 只匹配一次成功则停止匹配
# print(re.search(pattern,strs).group(0))  #返回完整的正则表达式的匹配结果
# print(re.search(pattern,strs).group(1))  #返回第一个分组的匹配的结果
# print(re.search(pattern,strs).group(2))

'''
   findall  遍历匹配
'''
# pattern =re.compile('\d[a-z]+\d')
# strs = 'MMMfdfdsga1abc2fsfsNNN3abc4KK'
# #findall
# print(re.findall(pattern,strs))  #返回符合条件的所有内容 保存在列表中
#
#
# pattern =re.compile('(\d)[a-z]+(\d)')
# strs = 'MMMfdfdsga1abc2fsfsNNN3abc4KK'
# #findall
# print(re.findall(pattern,strs))  #findall 如果规则中有分组则只返回分组匹配的结果


'''
   finditer  查看完整匹配结果的迭代器
'''
# pattern =re.compile('(\d)[a-z]+(\d)')
# strs = 'MMMfdfdsga1abc2fsfsNNN3abc4KK'
#
# for i in re.finditer(pattern,strs):
#     print(i.group(0))
#     print(i.group(1))
#     print(i.group(2))


'''
   split   返回一个切割后的列表 按照符合正则表达式的字符串进行切割
'''

# print(re.split('\d','a1b2c3d4e'))

'''
   sub 进行替换 将符合规则的内容替换成你想替换的结果
'''

# print(re.sub('\d','0','a1b2c3d4e'))
# print(re.sub('[a-z]','M','a1b2c3d4e'))

'''
   subn 返回替换结果以及替换掉的次数的元组
'''

# print(re.subn('[a-z]','M','a1b2c3d4e'))
#
# pattern = re.compile('[a-z]')
# strs = 'a1b2c3d4e'
# print(pattern.subn('M',strs))

#引用分组
# pattern =re.compile('(\d)([a-z]+)(\d)')
# strs = 'MMMM1abc2NNNN3abc4KKKK'

# for i in re.finditer(pattern,strs):
#     print(i.group(0))  # 1 3
#     print(i.group(1))  # abc abc
#     print(i.group(2))  # 2 4

# print(pattern.sub(r'\2 \1 \3',strs))
# print(pattern.sub(r'\1---\3',strs))


'''
   贪婪与非贪婪
'''
#贪婪
# strs = "<a>nnn</a><p>abc</p><script>alert('hahaha')</script>" \
#        "<p>efg</p><span>bbb</span>"
#
# pattern = re.compile("<p>[a-z]+</p>")
# print(pattern.findall(strs))
#
# pattern = re.compile("<p>.*</p>")  #在符合规则的前提下尽可能多的匹配
# print(pattern.findall(strs))
#
# #非贪婪
# pattern = re.compile("<p>.*?</p>")  #在符合规则的前提下尽可能少的匹配
# print(pattern.findall(strs))

'''
   匹配中文字符串
'''
# strs = '你好，靓仔，靓妹，lucy'
# pattern = re.compile("\w+")
# print(pattern.findall(strs))
#
# #专门使用匹配中文的正则
# pattern = re.compile("[\u4e00-\u9fa5]+")
# print(pattern.findall(strs))

'''
   练习
'''
#1.将以下字符串中所有的Url匹配出来
# str = '''
#       313156566@qq.com
#       hjsad@163.com
#       http://www.abc.com.cn
#       http://www.sae.com
#       ftp://www.nnn.org
#       ftp://www.jksad.net
#       '''
#
# pattern = re.compile("[a-z]+://www(\.[a-z]+)(\.[a-z]){1,2}")
# for i in pattern.finditer(str):
#     print(i)

#2.判断以下字符串是否全是中文（中文正则模式[\u4e00-\u9fa5]）
# str = "广东省广州市"
#
# pattern = re.compile("[\u4e00-\u9fa5]+$")  #开头和结尾都是中文
# print(pattern.findall(str))
# if pattern.findall(str):
#     print('是全部是中文')
# else:
#     print('不全部是中文')

#3.写出一个正则表达式，过滤网页上的所有JS脚本（即把script标记及其内容去掉）
# script = "以下内容不显示：<script>language='javascript'>alert('cc'); \</script>" \
#          "<p>fdgfgdgsdg</p><script>alert('dd')</script>"
#
# pattern = re.compile('<script>.*?</script>')
# print(pattern.findall(script))
# print(pattern.sub('',script))


#4.通过正则表达式把img标签中的src路径匹配出来
# str = '''
#       <img name="photo" src="../piblic/img/img1.png" />
#       <img name='news' src='xxx.jpg' title='news' />
#       '''
# pattern = re.compile("src=[\'\"](.*?)[\'\"]")
# print(pattern.findall(str))

#5.将电话号码13811119999变成138****9999
phone = '13811119999'

pattern = re.compile('^(1[3578]\d)(\d{4})(\d{4})$')
for i in pattern.finditer(phone):
    print(i.group())

print(pattern.sub(r'\1****\3',phone))