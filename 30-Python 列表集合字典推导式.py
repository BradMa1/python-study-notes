"""
推导式（又称解析式），是Python的一种独有特性。
推导式是可以从一个数据序列构建另一个新的数据序列（一个有规律的列表或控制一个有规律列表）的结构体
共有三种推到：列表推导式、集合推导式、字典推导式
"""
# [1,2,3] 推导式 [1,4,9]

# 案例：创建一个0-9的列表

# while循环：
# 初始化计数器
i= 0
list1 = []
# 编写循环条件
while i <= 9:
    list1.append(i)
    # 更新计数器
    i += 1
print(list1)

# for循环
list1 = []
# 编写for循环
for i in range(1,10):
    list1.append(i)
print(list1)

# 一、列表推导式
"""
基本语法：
变量名 = [表达式 for 变量 in 列表 for 变量 in 列表]
变量名 = [表达式 for 变量 in 列表 if 条件]
"""

# 案例：定义0-9之间的列表
list1 = []
for i in range(10):
    list1.append(i)
print(list1)

# 列表推导式
list1 = [i for i in range(10)]
print(list1)

# 执行原理：[i for i in range(10)]
"""列表推导式先运行表达式右边的内容，当第一次遍历时：
i = 0
"""
