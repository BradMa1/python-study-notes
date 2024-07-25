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

# 1、列表推导式
list1 = [i for i in range(10)]
print(list1)

# 执行原理：[i for i in range(10)]
"""列表推导式先运行表达式右边的内容:
当第一次遍历时：i = 0，其得到变量i的结果后，会放入最左侧的变量i中，这个时候列表中就是[0]
当第一次遍历时：i = 1，其得到变量i的结果后，会追加到最左侧的变量i中，这个时候列表中就是[0,1]

...

当最后一次遍历时：i = 9，其得到变量i的结果后，会追加到最左侧的变量i中，这个时候列表中就是[0,1,2,3,4,5,6,7,8,9] 
"""

# 2、带if的列表推导式(列表推导式+if条件判断)
"""在使用列表推导式时，除了可以使用for循环，还可以在其遍历的过程中引入if条件判断"""

'''
变量 = [表达式 for 变量 in 序列 if 条件判断]

等价于

for 零时变量 in 序列:
    if 条件判断:
'''

# 案例：生成一个0-9之间的偶数（i % 2 == 0）序列
# 方法一：range()步长实现
list1 =[i for i in range(0,10,2)]
print(list1)

# 方法二：if条件实现
list1 = [ i for i in range(10) if i % 2 == 0]
print(list1)

# 3、for循环嵌套列表推导式
"""
基本语法：
变量 = [表达式 for 零时变量 in 序列 for 零时变量 in 序列]

"""
# 案例：创建列表 => [(1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
(1,0) (1,0-2)
(1,1) (1,0-2)
(1,2) (1,0-2)
# ------------------
(2,0) (2,0-2)
(2,1) (2,0-2)
(2,2) (2,0-2)

# 原生代码：for循环嵌套
list1 = []
# 外层循环
for i in range(1,3):
    # 内层循环
    for j in range(0,3):
        tuple1 = (i,j)
        list1.append(tuple1)
print(list1)

# 列表推导式：
list1 = [(i,j) for i in range(1,3) for j in range(0,3)]
print(list1)


# 二、字典推导式
'''思考：有如下两个列表，如何快速给合并为一个字典'''
list1 = ['name','age','gender']
list2 = ['小明','18','男']

person = {'name':'小明','age':'18','gender':'男'}
print(person)

"""使用字典推导式"""
'''
基本语法：
字典推导式是列表推导式思想的延续，语法差不多，只不过产生的是字典而已。
字典推导式格式：

变量 = {key:value for key,value in 序列}    

等价于

for key,value in 序列:
    key = key
    value = value
'''
# 字典推导式作用:快速合并列表为字典或提取字典中目标数据

# 案例1：创建一个字典：字典key是1-5数字，value是这个数字的2次方
dict1 = {i : i**2 for i in range(1,6)}
print(dict1)

# 案例2：将两个列表合并为一个字典
list1 = ['name','age','gender']
list2 = ['小明','18','男']
 
person = {list1[i]:list2[i] for i in range(len(list1))}
print(person)

# 案例3：提取字典中目标数据
counts = {'MBP':268,'HP':125,'DELL':201,'Lenovo':199,'ACER':99}

# 需求：提取上述字典中电脑数量大于等于200的数据(键值对)
counts = {key:value for key,value in counts.items() if value >= 200}
print(counts)


# 三、集合推导式
"""集合最大的特点是去重"""

# 需求：创建一个集合，数据为下方列表的2次方
list1 = [1,1,2]
set1 = (1,4)

# 推导式：
list1 = [1,1,2]
set1 = {i **2 for i in list1}
print(set1)
