# 一、 定义
""" 所谓的公共方法就是支持大部分数据序列 """

# 二、常见公共方法1
"""
运算符                      描述                        支持的容器类型
+                          合并                       列表 元组 字符串
*                          复制                       列表 元组 字符串
in                       元素是否存在                     列表 元组 字符串 字典
not in                   元素不存在                       列表 元组 字符串 字典

"""
# 案例：
# 1. +加号，代表两个序列之间的连接与整合
str1 = "hello"
str2 = "world"
print(str1 + str2)  # 输出：helloworld

# 定义两个列表对其数据进行整合
list1 = ['刘备','关羽','张飞']
list2 = ['赵云','黄忠','魏延']
print(list1 + list2)  # 输出：['刘备', '关羽', '张飞', '赵云', '黄忠', '魏延']

# 定义两个元组对其数据进行整合
tuple1 = (10,20)
tuple2 = (30,40)
print(tuple1 + tuple2)  # 输出：(10, 20, 30, 40)


# 2. *乘号，代表重复次数
str1 = "hello"
print(str1 * 3)  # 输出：hellohellohello

# 字符串与*乘号的关系
print("-" * 40)
print('欢迎使用传智教育通讯录管理系统V1.0')
print("-" * 40)

# 列表与*乘号的关系
list1 = ['*']
print(list1 * 10)

# 元组与*乘号的关系
tuple1 = (10,)
print(tuple1 * 10)


# 3. in 判断元素是否存在与 not in 判断元素不存在
ips = ['192.168.1.1','192.168.1.2','192.168.1.3']
if '192.168.1.1' in ips:
    print('列表中元素已存在')
else:
    print('列表中元素不存在')



# 三、常见的公共方法2
"""
函数                                                                        描述

len()                                                                  计算容器中元素个数

del或del()                                                             根据索引下标删除指定元素

max()                                                                   返回容器中元素最大值

min()                                                                   返回容器中元素最小值

range(start,end,step)                                              生成从start到end(不包含)的数字，步长为step，供for循环使用

enumerate()        函数用于将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，同时列出数据和数据下标，一般用在for循环当中
"""
# 案例1：len()获取字符串、列表、元组、字典、集合的长度
# 定义一个字符串
str1 = 'Hello World!'
print(f'字符串的长度为：{len(str1)}')

# 定义一个列表
list1 = [10,20,30,40,50]
print(f'列表的长度为：{len(list1)}')

# 定义一个字典
dict1 = {'name':'哆啦A梦','gender':'male','address':'东京'}
print(f'字典的长度为：{len(dict1)}')  # 输出：字典的长度为：3，因为字典的键值对个数为3个，所以字典的长度为3个。


# 案例2：del方法，用于删除序列中指定的元素（根据索引下标）
# 定义一个列表
list1 = ['吕布','董卓','貂蝉']
    # 使用del方法删除"董卓"
del list1[1]
print(list1)  # 输出：['吕布', '貂蝉']，因为索引为1的元素被删除了

# 定义一个字典
dict1 = {'name':'悟空','gender':'male','address':'花果山'}
    # 使用del方法删除"address"
del dict1['address']  # 注意：字典的删除操作是按照键来删除的，而不是按照索引下标来删除
print(dict1)  # 输出：{'name': '悟空', 'gender': 'male'}

# 案例3：求某个序列中元素的最大值和最小值
num1 = int(input('请输入第一个数：'))
num2 = int(input('请输入第二个数：'))
num3 = int(input('请输入第三个数：'))
list1 = [num1,num2,num3]
# max_num = max(list1)
# min_num = min(list1)
print(f'最大值为：{max(list1)}')
print(f'最小值为：{min(list1)}')

# 案例3：enumerate(),把一个序列类型的数据构造成key:value键值对的数据结构,然后结合for循环进行遍历
list1 = [10,20,30,40,50]
n = 1
for i in list1:
    print(f'第{n}个数是：{i}')
    n += 1
print('-' * 40)

for key,value in enumerate(list1):
    print(key,value)
    print(f'第{key+1}个数是：{value}')



# 四、序列数据类型之间的相互转换

# 1. list()方法：把某个序列类型的数据转化为列表
# 1.1 元组
tuple1 = (10, 20, 30, 40, 50)
print(list(tuple1))
# 1.2 集合
set1 = {10, 20, 30, 40, 50}
print(list(set1))
# 1.3. 字典
dict1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
print(list(dict1))

# 2. tuple()方法：把某个序列类型的数据转化为元组
# 2.1 定义一个列表类型的数据
list1 = ['a', 'b', 'c', 'd', 'e']
print(tuple(list1))
# 2.2 定义一个集合类型的数据
set1 = {10, 20, 30, 40, 50}
print(tuple(set1))

# 3. set()方法：将某个序列转化为集合(注意：集合可以快速完成数据去重，集合不支持下标)
# 3.1 定义一个列表类型的数据
list1 = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']  
print(set(list1))
# 3.2 定义一个元组类型的数据
tuple1 = (10,20,30,40,50,10,20,30,40,50)
print(set(tuple1))

