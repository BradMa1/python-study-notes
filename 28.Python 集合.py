# 一、集合的定义
"""
集合(set)是一个无序的不重复序列
特点：
    自动去重，无序
"""
"""
基本语法：
可以使用'{}'或'set()'方法来定义集合,但是如果要创建空集合只能使用'set()',因为'{}'创建的是空字典。
"""

# 定义一个集合
s1 = {10,20,30,40,50}  # 使用花括号定义集合，元素之间用逗号隔开
print(s1)
print(type(s1))  # 输出集合的类型，应该为<class 'set'>

# 定义一个集合：集合中存在相同的数据
s2 = {'刘备','曹操','孙权','刘备'}
print(s2)  # 输出集合，重复的数据只打印一个（具有自动去重）

# 定义空集合
s3 = {}
s4 = set()
print(type(s3))     # 打印<class 'dict'>，说明{}定义的是一个字典，而不是集合。
print(type(s4))     # 打印<class 'set'>


# 二、集合操作的相关方法（增删改查）
# 1. 集合的增操作
# 1.1 add()方法：向集合中增加一个元素（单一）
students = set()
students.add('小明')
students.add('小红')
students.add('小明')    # 集合会自动去重
print(students)

# 1.2 update()方法：向集合中增加序列类型的数据（字符串、列表、元组、字典）
students = set()
list1 = ['刘备','关羽','赵云']
students.update(list1)
print(students) 

# 2. 集合的删操作
# 2.1 remove()方法：删除集合中的指定数据，如果数据不存在则报错
# 2.2 discard()方法：删除集合中的指定数据，即使数据不存在也不会报错
# 2.3 pop()方法：随机删除集合中的某个数据，并返回这个数据

# 1. 定义一个集合
products = {'萝卜','白菜','水蜜桃','奥利奥'}
# 2.使用remove方法删除白菜这个元素
products.remove('白菜')  # 如果集合中没有这个元素，会报错
print(products)
# 3. 使用discard方法删除未知元素
products.discard('未知元素')  # 如果集合中没有这个元素，不会报错，直接跳过
print(products)
# 4. 使用pop方法随机删除某个元素
del_product = products.pop()
print(del_product)

# 3. 集合的查操作
# 3.1 in：判断某个元素是否在集合中，在则返回True，否则返回False
# 3.2 not in ：判断某个元素不在集合中，不在则返回True，否则返回False

# 定义一个set集合
s1 = {'小明','小红','小东'}
# 判断小明是否在s1集合中
if '小明' in s1:
    print('小明有在s1集合中')
else:
    print('小明不在s1集合中')

# 4.集合的遍历操作
"""
for i in 集合：
"""
s1 = {'小明','小红','小东'}
for i in s1:
    print(i)


# 三、集合中的交集、并集与差集特性
""" 在Python中，可以使用&或itersection()来求两个集合的交集 """
