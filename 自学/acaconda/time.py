import time
# print(time.altzone)
#
# print(time.asctime())  #可以传递时间元组
#
# print(time.clock())

# for i in range(100000):
#     pass
#
# print(time.clock())
#
# print(time.ctime())  #返回可读形式的时间

#时间戳 1970 1 1 0 0 0
# print(time.gmtime())  #返回一个时间元组

#接收时间戳返回当地时间的时间元组
# print(time.localtime())

#接收时间元组，返回时间戳，可以将时间戳转换为时间元组
# tup_time = time.localtime()
# print(tup_time)

#可以将时间元组转换成时间戳
# print(time.mktime(tup_time))  #传递时间元组，返回时间戳

#接收时间元组，将时间元组转换为自定义的可读形式时间字符串
# tup_time = time.localtime()
# print(tup_time)
# print(time.strftime('%Y-%m-%d %H:%M:%S'))

#将字符串时间转换为时间元组
# time_str = '2019-09-23 12:04:36'
# print(time.strptime(time_str,'%Y-%m-%d %H:%M:%S'))
# tup_time = time.strptime(time_str,'%Y-%m-%d %H:%M:%S')
# print(time.mktime(tup_time))

#获取时间戳
# print(time.time())


# for i in range(1,5):
#     print('第%d颗子弹'%i)
#     time.sleep(3)



