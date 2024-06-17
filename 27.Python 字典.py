# 一、Python中字典(dict)的定义
"""
特点：
1. 符号为大括号（花括号）==> {}
2. 数据为键值对形式出现 ==> {key:value},key:键名，value：值。在同一个字典中，key必须是唯一（类似于索引下标）
3. 各个键值对之间用逗号隔开

"""
# 有数据字典
dict1 = {'name':'Tom','age':20,'gender':'男'}

# 空字典
dict2 = {}

dict3 = dict2()

# 二、字典的增操作
"""
基本语法：
        字典名称[key]=value
注：如果key存在则修改这个key对应的值;如果key不存在则新增次键值对
"""
# 案例：定义一个空字典，然后添加name、age、以及address这样的3个key
# 定义一个空字典
person = {}
# 追加键值对到字典中
person['name'] = '刘备'
person['age'] = '40'
person['address'] = '蜀国'  
# 使用print方法打印person字典
print(person)


# 三、字典的删操作
"""
del字典名称[key]:删除指定元素
clear()方法：清空字典中的所有key
"""
# 定义一个有数据的字典
person = {'name':'王大锤','age':25,'gender':'男','address':'云南昆明'}
# 删除字典中的某个元素（如gender）
del person['gender']  
# 打印字典
print(person)
# clear()方法清空字典
person.clear()
print(person)


# 四、字典的改操作
"""
基本语法：
        字典名称[key] = value
        注：如果key存在则修改这个key对应的值;如果key不存在则新增此键值对
"""
# 案例：定义一个字典，里面有name、age以及address，修改address这个key的value值
# 定义字典
person = {'name':'孙悟空','age':600,'address':'花果山'}
# 修改字典中的数据（address）
person['address'] = '东土大唐'
print(person)


# 五、字典查操作
# 1.查询方法：使用具体的某个key查询数据，如果未找到则直接报错
"""
基本语法：
        字典序列[key]
"""
# 2. 字典的相关查询方法
"""
get(key,默认值)   根据字典的key获取对应的value值，如果当前查找的key不存在则返回第二个参数（默认值），如果省略第二个参数，则返回None。
keys()            以列表返回一个字典所有的键
values()          以列表返回字典中的所有值
items()           以列表返回可遍历的（键，值）元组数组
"""
# 案例1：使用get获取字典中某个key的value值
# 定义一个字典
cat = {'name':'Tom','age':5,'address':'美国纽约'}
# 获取字典的相关信息
name = cat.get('name')
age = cat.get('age')
gender = cat.get('gender','未知')
address = cat.get('address')
print(f'姓名：{name},年龄：{age},性别：{gender},地址：{address}')  # 输出：姓名：Tom,年龄：5,性别：未知,地址：美国纽约

# 案例2：提取person字典中的所有key
# 定义一个字典
person = {'name':'貂蝉','age':'18','mobile':'18634151264'}
# 提取字典中的name、age、以及mobile属性
print(person.keys())

# 案例3：提取person字典中的所有value值
# 定义一个字典
person = {'name':'貂蝉','age':'18','mobile':'18634151264'}
# 提取字典中的'貂蝉'、'18'以及'18634151264'号码
print(person.values())

# 案例4：使用items()方法提取数据
# 定义一个字典
person = {'name':'貂蝉','age':'18','mobile':'18634151264'}
# 调用items获取数据
print(person.items())   # 打印 ([('name', '貂蝉'), ('age', '18'), ('mobile', '18634151264')])
# 结合for循环对字典中的数据进行遍历
for key,value in person.items():  # 遍历字典中的数据，并打印每个键值对
    print(f'{key}:{value}')


# 综合案例：通讯录管理系统
"""
需求：开发一个通讯录管理系统，主要用于实现存储班级中同学的信息（姓名、年龄、电话）
知识点：列表、字典
延申：在python中，可以使用字典来保存一个人的基本信息。但是如果要保存多人的信息，可以把列表和字典结合起来
"""
"""
stedents = [0,1,2]

student = [{'name':'刘备','age':'18','mobile':'10086'},{'name':'貂蝉','age':'17','mobile':'10010'},
{'name':'吕布','age':'19','mobile':'10000'}]

要求：正常情况下，通讯录应该有4个功能：增删改查
"""
# 1. 定义一个列表，将来用于存储所有同学的信息
students = []

# 2. 打印功能菜单
print('-'*40)
print('欢迎使用传智教育通讯录管理系统V1.0')
print('[1] 增加学员信息')
print('[2] 删除学员信息')
print('-'*40)

# 3.提示用户进行相关操作
user_num = int(input('请输入您要进行的操作编号：'))
if user_num == 1:
    # 4.提示用户输入学员信息
    student = {}
    student['name'] = input('请输入学员的姓名：')
    student['age'] = int(input('请输入学员的年龄：'))
    student['mobile'] = input('请输入学员的电话：')
    # 5.把学员的信息保存在列表中
    students.append(student)
    print(students)
elif user_num == 2:
    name = input('请输入要删除的学员姓名：')
    # 遍历所有学员信息
    for i in students:
        if i['name'] == name:
            # 从列表中删除整个学员信息
            students.remove(i)
            print('删除成功')
            print(students)

        else:
            print('您要删除的学员信息不存在')
            
else:
    print('输入有误，请重新输入')
    