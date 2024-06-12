"""
变量的数据类型
1.数值 int(整型)
      float(浮点型)
2.布尔型 True(真)
        False(假)
3.str（字符串）
4.list（列表）
5.tuple（元组）
6.set（集合）
7.dict（字典）
"""


# 案例一： 定义一个人的信息
name = 'Tom'
age = 18
print(name,age)


#  案例二：定义一个超市收银系统，写入一个名称：大白菜 ，价格：3.5
name = "大白菜"
price = 3.5
print(name,price)



'''
如何判断一个变量到底是什么类型：
1.使用type(变量名称)，返回变量的数据类型
2.isinstance(变量名称，数据类型)，只能返回True(真)或False(假)
'''
name = 'Tom'
age = 18
print(type(age))

name = "大白菜"
price = 3.5
print(isinstance(price,float))




