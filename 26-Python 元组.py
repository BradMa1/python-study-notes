# 一、元组的定义与使用
"""元组可以存储多个数据，且元组内的数据是不能修改的"""

# 1. 元组的定义
""" 元组特点：定义元组使用小括号，且使用逗号隔开各数据，数据可以是不同的数据类型 """
"""
基本语法：
       
        tuple1 = (10,20,30)  # 多个数据元组
        tuple1 = (10,)      # 单个数据元组     注意：单个数据元组定义时，需要在数据后面加上逗号，否则会被认为是数值本身而不是元组
"""
# 1.1 定义多个数据元组
tuple1 = (10,20,30)
print(tuple1)
print(type(tuple1))  # 输出<class 'tuple'>

# 1.2 定义单个数据元组
tuple2 = (10)
print(type(tuple2))  # 输出<class 'int'>，因为单个数据元组定义时，没有加上逗号，所以被解释器认为是数值本身而不是元组，所以输出int类型
tuple2 = (10,)
print(type(tuple2))  # 输出<class 'tuple'>

# 2. 元组的相关操作方法
"""由于元组中的数据不允许直接修改，所以其操作方法大部分为查询方法"""
"""
元组[索引]            根据索引下标查找元素
index()               查找某个数据，如果数据存在返回对应的下标，否则报错。语法和列表、字符串的index方法相同
count()               统计某个数据在当前元组中出现的次数
len()                 统计元组中数据的个数，即元组的长度
"""
# 案例1：访问元组中的某个元素
nums = (10,20,30,40,50,60,70,80,90,100)  # 定义一个元组
print(nums[2])

# 案例2：查找某个元素在元组中出现的位置，存在则返回索引下标，不存在则直接报错
nums = (10,20,30,40,50,60,70,80,90,100)
print(nums.index(20))

# 案例3：统计某个元素在元组中出现的次数
nums = (10,20,30,40,30,30)
print(nums.count(30))

# 案例4：求元组的长度
nums = (10,20,30,40,50,60,70,80,90,100) 
print(len(nums))

