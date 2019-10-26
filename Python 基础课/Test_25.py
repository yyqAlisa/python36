# class Person: #创建类
#     def __init__(self,name,age,sex,country):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.country = country
#
#     def sheep(self):
#         print(self.name + "上床睡觉啦。。。。 晚安")
#
#     def eat(self):
#         print(self.name + "在吃饭。。。")
#
#     def work(self):
#         print(self.name + "在工作中。。。")
#
#
# class Student(Person):
#     def __init__(self,name,age,sex,country,school,number):
#         super().__init__(name,age,sex,country) #调用父类
#         self.school = school
#         self.number = number
#
#     def work(self):
#         print(self.name + "努力学习，报效祖国！！！")
#
#
#
# class StudentManager(Student):
#     def __init__(self,name,age,sex,country,school,number,job):
#         super().__init__(name,age,sex,country,school,number)
#         self.job = job
#     def work(self):
#         print(self.name + self.job+ "进行中。。。。")
#
#
#
# p1 = Person("小明","21","女","中国")
# p1.sheep()
# p1.eat()
# p1.work()
#
# s1 = Student("小花","16","男","美国","耶鲁大学","91000012")
# s1.sheep()
# s1.eat()
# s1.work()
#
# b1 = StudentManager("小李","26","女","英国","伦敦大学","11020086","写程序")
# b1.sheep()
# b1.eat()
# b1.work()
#
# tmp_set=set()
#
# list1 = [1,1,1,2,3,4,5,6,1,7,1]
#
# # 遍历list1 ，把元素都放在tmp_set集合中 ,达到去重的目的
# for i in list1:
#     tmp_set.add(i)
#
# # 从tmp_set中移除一个元素 1
#
# tmp_set.remove(1)
#
# # 打印tmp_set
# print(list(tmp_set))


# 平衡点：比如int[] numbers = {1,3,5,7,8,25,4,20}; 25前面的总和为24，25后面的总和也是24，
# 25这个点就是平衡点；假如一个数组中的元素，其前面的部分等于后面的部分，那么这个点的位序就是平衡点
# # 要求：返回任何一个平衡点

from __future__ import division

def find_balance_point(numbers):
    total = sum(numbers)
    fore = 0
    for number in numbers:
        if fore < (total - number) / 2:
            fore += number
        else:
            break
    if fore == (total - number) / 2:
        print(number)
    else:
        print(r'not found')


def split_list(num_list):
    '''
    输入一个列表，判断是否可以划分为大小相等的两个子列表，可以返回True不可以返回False
    '''
    total = sum(num_list)
    half = total / 2
    if int(half) != half:
        return False
    else:
        all_sub_list = get_list_all_sub_list(num_list)
        i = 0
        flag = False
        while i < len(all_sub_list):
            one_list = all_sub_list[i]
            two_list = [one for one in num_list if one not in one_list]
            if sum(one_list) == sum(two_list):
                flag = True
                break
            else:
                i += 1
        if flag:
            return True
        else:
            return False


def main_func(num_list):
    '''
    输入一个列表判断是否存在平衡点
    '''
    res = False
    for i in range(len(num_list)):
        temp_list = num_list[:]
        flag = temp_list.pop(i)
        if split_list(temp_list):
            res = True
            print('平衡点为：', flag)
    if not res:
        print('不存在平衡点!!!')


def get_list_all_sub_list(num_list):
    '''
    输入一个列表，返回该列表所有的子列表，这里定义的空列表不属于子列表，故：子列表最小长度为1
    '''
    if len(num_list) == 1:
        return [num_list]
    sub_list = get_list_all_sub_list(num_list[:-1])
    extra = num_list[-1:]
    temp_list = []
    for one in sub_list:
        temp_list.append(one + extra)
    return sub_list + temp_list


if __name__ == '__main__':
    num_list = [1, 3, 5, 7, 8, 25, 4, 20]

print(find_balance_point(num_list))
print(main_func(num_list))
