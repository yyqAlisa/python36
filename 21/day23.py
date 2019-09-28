# class Pets:
#     a = 1 #类属性  能通过实例化对象 或 类名  直接调用
#     def dogs(self,name): #实例化方法  只能通过实例化对象调用
#         print(name,1)
#     def cats(self,name):
#         print(name,2)
#     def pigs(self,name):
#         print(name,3)
#
# class Cars:
#     def bmw(self,money):
#         print(money)
#
# pets = Pets()  #实例化
# pets.dogs('小黑')  #通过实例化对象调用方法
# pets.cats('小白')
# print(Pets.a)


# class Person:
#     def __init__(self,name,age,sex):  #构造化方法  在实例化的时候自动执行
#         # self 不是关键字， 它指向实例化对象
#         self.name = name  #实例化属性
#         self.sex =sex
#         self.age = age
#
#     def eat(self,food):  #实例化方法  只能通过实例化对象调用
#         print('%s喜欢吃%s'%(self.name,food))
#
#     def info(self):
#         print('%s是一名%s性,今年%s岁'%(self.name,self.sex,self.age))
#
#     def sleep(self,time):
#         print('%s每天睡%s小时'%(self.name,time))
#
# person = Person('小明',11,'男') #实例化
# person.eat('红烧排骨') #通过实例化对象调用实例化方法
# person.info()
# person.sleep(8)
#
# person2 = Person('小红',22,'女')
# person2.info()

# 1.餐馆：创建一个名为Restaurant的类，其方法__init__()设置两个属性：
# restaurant_name 和 cuisine_type(烹饪)。
# 创建一个名为 describe_restaurant()方法和一个名为open_restaurant ()方法,
# 其中前者打印前述两项信息，而后者打印一条消息,指出餐馆正在营业。
# 根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。

# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#     def describe_restaurant(self):
#         print('%s主要做%s'%(self.restaurant_name,self.cuisine_type))
#     def open_restaurant(self):
#         print('%s正在营业'%self.restaurant_name)
# restaurant = Restaurant('老陈饭店','粤菜')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
#
# restaurant2 = Restaurant('小陈饭店','台湾菜')
# restaurant2.describe_restaurant()
# restaurant2.open_restaurant()

# 2.用户：创建一个名为User的类，其中包含属性first_name和last_name,
# 还有用户简介通常会存储的其他几个属性。在类User中定义一个名为describe_user()的方法，它打印用户信息摘要；
# 再定义一个名为greet_user()的方法，它向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法.

class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print('%s打印%s的摘要'%(self.first_name,self.last_name))
    def greet_user(self):
        print('%s用户你好'%(self.first_name))

user = User('陈','明明')
user.describe_user()
user.greet_user()








