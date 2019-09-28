# 1.餐馆：创建一个名为Restaurant的类，其方法__init__()设置两个属性：
# restaurant_name 和 cuisine_type(烹饪)。
# 创建一个名为 describe_restaurant()方法和一个名为open_restaurant ()方法,
# 其中前者打印前述两项信息，而后者打印一条消息,指出餐馆正在营业。
# 根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。

# 就餐人数：在为完成练习1而编写的程序中,添加一个名为number_served的属性,并将其默认值设置为0。
# 打印有多少人在这家餐馆就餐过,然后修改这个值并再次打印它。
# 添加一个名为set_number_max()的方法,它让你能够设置最大就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为increment_number_served()的方法,它让你能够将就餐人数递增.调用这个方法并向它传递一个这样的值：
# 你认为这家餐馆每天可能接待的就餐人数。


class Restaurant():
    number_served = 0 #历史总就餐人数
    def __init__(self, restaurant_name, cuisine_type): #构造化方法
        self.restaurant_name = restaurant_name #实例化属性
        self.cuisine_type = cuisine_type
        self.now_number = 0  #当前就餐人数

    def describe_restaurant(self): #实例化方法
        print('%s主要做%s' % (self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print('%s正在营业' % self.restaurant_name)

    def set_number_max(self,max_number):
        self.max_number = max_number  #最大就餐人数
        print('最大就餐人数为%s'%max_number)

    def increment_number_served(self,come_number):
        if self.now_number+come_number<=self.max_number:
            self.now_number += come_number
            Restaurant.number_served += come_number
            print('请就餐,当前店内就餐人数为%s,历史总就餐人数为%s'%(self.now_number,Restaurant.number_served))
        else:
            print('当前空余座位%s个，餐位不足，请等待'%(self.max_number-self.now_number))


restaurant = Restaurant('老陈饭店', '粤菜')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_max(100)
restaurant.increment_number_served(10)
restaurant.increment_number_served(20)
restaurant.increment_number_served(80)


# restaurant2 = Restaurant('小陈饭店', '台湾菜')
# restaurant2.describe_restaurant()
# restaurant2.open_restaurant()




# 5.冰淇淋小店：冰其淋小店是一种特殊的餐馆。编写一个名为IceCreamStand的类，
# # 让它继承你为完成练习1或练习4而编写的Restaurant类。这两个版本Restaurant类都可以，
# # 挑选你更喜欢的那个即可。添加一个名为flavors的属性,用于存储一个由各种口味的冰淇淋组成的列表。
# # 编写一个显示这些冰淇淋的方法。创建一IceCreamStand实例,并调用这个方法。

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name, type,flavors):
        super().__init__(restaurant_name,type)
        self.flavors = flavors

    def show_type(self):
        print('%s店内的冰淇淋口味有%s'%(self.restaurant_name,self.flavors))


iceCreamStand = IceCreamStand('清凉夏日', '冰淇淋',['香草','巧克力','榴莲'])
iceCreamStand.describe_restaurant()
iceCreamStand.show_type()
iceCreamStand.open_restaurant()
iceCreamStand.set_number_max(20)
iceCreamStand.increment_number_served(2)
iceCreamStand.increment_number_served(10)
iceCreamStand.increment_number_served(10)