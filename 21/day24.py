# #
# # class Animal():
# #     def __init__(self,name,food):
# #         print(self)
# #         self.name = name
# #         self.food = food
# #     def eat(self):
# #         print('%s喜欢吃%s'%(self.name,self.food))
# #
# # class Dog(Animal):
# #     def __init__(self,name,food,hoby):
# #         # super().__init__(name,food)
# #         Animal.__init__(self,name,food)
# #
# # class Cat(Animal):
# #     def __init__(self,name,food,hoby):
# #         # super().__init__(name,food)
# #         Animal.__init__(self,name,food)
# #
# # dog = Dog('小黑','骨头','奔跑')
# # dog.eat()
# # cat = Cat('小花','鱼','毛线球')
# # cat.eat()
#
# # 1.餐馆：创建一个名为Restaurant的类，其方法__init__()设置两个属性：
# # restaurant_name 和 cuisine_type(烹饪)。
# # 创建一个名为 describe_restaurant()方法和一个名为open_restaurant ()方法,
# # 其中前者打印前述两项信息，而后者打印一条消息,指出餐馆正在营业。
# # 根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。
#
#
# class Restaurant():
#     # __a = 1  #私有属性  只能在类内部调用，不能再外部访问
#     nums = 0   #类属性 能通过实例化对象 或 类名  直接调用
#     def __init__(self, restaurant_name, cuisine_type): #构造化方法
#         self.restaurant_name = restaurant_name #实例化属性
#         self.cuisine_type = cuisine_type
#         # print(Restaurant.__a)
#     def describe_restaurant(self): #实例化方法
#         print('%s主要做%s' % (self.restaurant_name, self.cuisine_type))
#
#     def open_restaurant(self):
#         print('%s正在营业' % self.restaurant_name)
#
#     def p(self,nums_come):
#         self.nums+=nums_come
#         Restaurant.nums+=nums_come



#
#     @classmethod
#     def k(cls): #类方法 能通过实例化对象 或 类名  直接调用
#         print(cls.nums)
#
#     @staticmethod
#     def g():#静态方法 能通过实例化对象 或 类名  直接调用
#         print(Restaurant.nums)
#
#

# restaurant = Restaurant('老陈饭店', '粤菜')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# restaurant.p(10)
# print(restaurant.nums)
#
# restaurant2 = Restaurant('小陈饭店', '台湾菜')
# restaurant2.describe_restaurant()
# restaurant2.open_restaurant()
# restaurant2.p(20)
# print(restaurant2.nums)
# print(Restaurant.nums)
# restaurant2.k()
#
# print(getattr(Restaurant,'nums')) #获得类属性 或者 数理化属性
# print(Restaurant.__dict__)
# print(Restaurant.__bases__)

# print(Restaurant._Restaurant__a) #不建议
# 类名._类名__属性名

# print(restaurant2.restaurant_name)


# 就餐人数：在为完成练习1而编写的程序中,添加一个名为number_served的属性,并将其默认值设置为0。打印有多少人在这家餐馆就餐过,然后修改这个值并再次打印它。
# 添加一个名为set_number_max()的方法,它让你能够设置最大就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为increment_number_served()的方法,它让你能够将就餐人数递增.调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。

class Restaurant():
    number_served = 0
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print('%s主要做%s'%(self.restaurant_name,self.cuisine_type))
    def open_restaurant(self):
        print('%s正在营业'%self.restaurant_name)
    def set_number_max(self,maxValue):
        print()

    def people(self,nums):
        self.number_served += nums


restaurant = Restaurant('老陈饭店','粤菜')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.people(10)
print(Restaurant.number_served)
print(restaurant)

restaurant2 = Restaurant('小陈饭店','台湾菜')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()


# 5.冰淇淋小店：冰其淋小店是一种特殊的餐馆。编写一个名为IceCreamStand的类，
# # 让它继承你为完成练习1或练习4而编写的Restaurant类。这两个版本Restaurant类都可以，
# # 挑选你更喜欢的那个即可。添加一个名为flavors的属性,用于存储一个由各种口味的冰淇淋组成的列表。
# # 编写一个显示这些冰淇淋的方法。创建一IceCreamStand实例,并调用这个方法。

# class IceCreamStand:
#     list =[]
#     def __init__(self,flavors):
#         self.flavors = flavors
#         self.list.append(flavors)
#
#     def show(self):
#         print(self.list)
#
#
# i = IceCreamStand("q")
# i.show()