# 一、高阶函数
# 1.定义
"""
把函数作为参数传入，这种函数称为高阶函数，高阶函数是函数式编程的体现
函数式编程就是指这种高度抽象的编程范式
"""

# 2.高阶函数的由来
'''
在Python中，abs()函数可以完成对数值取绝对值操作。
1.正数取绝对值，结果是其本身
2.负数取绝对值，结果是其相反数
'''
abs() # 返回的结果都是正数
abs(-10) # 10

"""
round()函数可以完成对数字的四舍五入计算
"""
round(10.2) # 10
round(10.5) # 11


# 需求：任意两个数字，按照指定要求（1.变成绝对值，2.四舍五入）整理数据后在进行求和运算
def fn1(num1,num2):
  return abs(num1) + abs(num2)

print(fn1(-10,10))

def fn2(num1,num2):
  return round(num1) + round(num2)

print(fn2(10.2,6.9))

# 对以上代码进行简化，然后合并为同一个函数-->高阶函数
def fn3(num1,num2,f):
    # f代表要传入的参数（参数是一个函数名，如abs或round）
  return f(num1) + f(num2)
# 绝对值求和
print(fn3(-10,10,abs))
# 四舍五入求和
print(fn3(10.2,6.9,round))


# 二、内置高阶函数

# 1.map()函数
'''
基本语法：
map(func,lst) 将传入的函数变量func作用到lst变量的每个元素中，并将结果组成新的列表(Python2)/迭代器(Python3)返回
func是函数名，lst是可迭代对象（如列表、元组、集合等）
'''
# 定义一个函数
def func(n):
    return n ** 2
# 定义一个列表
list1 = [1,2,3]
# 使用map对lst进行func操作
list2 = map(func,list1)
print(list2) # <map object at 0x000001D3E4B8E6D0> -->Python3中返回的是迭代器
print(list(list2)) # [1, 4, 9] -->Python3中需要转换成列表才能打印


# 2.reduce()函数
'''
reduce(func,lst) 其中func必须有两个参数。每次func计算的结果继续和序列的下一个元素做累加计算。
注意：reduce()传入的参数func必须接收两个参数
'''
list1 = [1,2,3,4,5]

def func(n1,n2):
    return n1 + n2
# reduce(func,lst)则把列表中的每个元素放入func中进行加工，然后进行累加操作

import functools

# 定义一个函数（求和）
def func(n1,n2):
    return n1 + n2
# 定义一个列表
list1 = [10,20,30,40,50]
# 调用reduce函数求列表中所有元素的和
sums = functools.reduce(func,list1) 
print(sums) # 150


# 3.filter()函数 
'''
filter(func,lst)函数用于过滤序列，过滤掉不符合条件的元素，返回一个filter对象。如果要转换为列表，可以使用list()来转换。
'''
# 定义一个函数（获取所有的偶数）
def func(n):
   return n % 2 == 0  #返回True或False

# 定义一个序列
list1 = [1,2,3,4,5,6,7,8,9,10]

# 调用filter函数过滤序列
result = filter(func,list1) # <filter object at 0x000001D3E4B8E6D0> -->Python3中返回的是迭代器 
print(list(result)) 


