# 一、 列表的定义：
'''
基本语法：
列表序列名称 = [元素1，元素2，元素3，...]
''' 
# 注：列表可以一次存储多个数据且可以为不同的数据类型
    
# 案例：定义一个列表，用于保存苹果，香蕉，菠萝
list1 = ['apple','banana','pineapple']
# 列表类型支持直接打印
print(list1)
# 打印列表的数据类型
print(type(list1))

# 二、 列表的相关操作
'''列表的作用是一次存储多个数据，可以对这些数据进行的操作有：增、删、改、查'''
# 1. 查操作
'''
列表在计算机中的底层存储形式，列表和字符串一样，在计算机内存中都占用一段连续的内存地址
我们想访问列表中的每个元素，都可以通过"索引下标"的方式进行获取
'''
# 如果我们想获取列表中的某个元素，直接索引下标：
list = ['apple','banana','pineapple']
# 获取列表中的banana
print(list[1])

# 1.1 查操作的相关方法：
'''
2.2.1. index()    指定数据所在位置的下标
2.2.2  count()    统计指定数据在当前列表中出现的次数
2.2.3  in         判断指定数据是否 在列表序列，如果在返回True，否则返回Fales
2.2.4  not in     判断指定数据是否 不在列表序列，如果不在返回True，否则返回Fales
'''
# 1.2 案例：
# 1.2.1 查找某个元素在列表中出现的位置（索引下标）
list1 = ['apple','banana','pineapple'] 
print(list1.index('apple'))     # 0
print(list1.index('peach'))     # 报错

# 1.2.2 count方法；统计元素在列表中出现的次数
list2 = ['刘备','关羽','张飞','关羽','赵云']  
# 统计关羽这个元素在列表中出现的次数
print(list2.count('关羽'))

# 1.2.3 in 和not in 方法（黑名单）
list3 = ['192.168.1.5','10.1.1.100','172.35.46.128']
if '10.1.1.100' in list3:   # 判断10.1.1.100是否在列表中，如果在返回True，否则返回False
    print('黑名单IP，禁止访问')
else:
    print('白名单IP，允许访问')


# 2. 增操作
'''
append()        增加指定数据到列表中
extend()        列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表
insert()        指定位置新增数据
'''
# 2.1 append()
# append():在列表的尾部追加元素
'''
注意：列表追加数据的时候，直接在原列表里面追加了指定数据，即修改了原列表，故列表为可变类型数据
'''
names = ['孙悟空','唐僧','猪八戒']  
# 在列表的尾部追加一个元素"沙僧"
names.append('沙僧')  # 注意：append()方法返回的是None，所以不能直接赋值给变量，而是通过列表名进行追加操作。
# 打印列表
print(names)

# 2.2 extend()方法：(建议可以使用此方法对两个列表进行合并)
"""
列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表
"""
# 案例：
list1 = ['Tom','Rose','Jack']
# 使用extend()方法追加元素
names.extend('Jennify')  # ['Tom', 'Rose', 'Jack', 'J', 'e', 'n', 'n', 'i', 'f', 'y']  
print(list1)
"""
注意：字符串'Jennify'会被拆分为列表['J', 'e', 'n', 'n', 'i', 'f', 'y']，逐一添加到列表中
"""
list2 = ['Hack','Jennify']
# 使用extend()方法对两个列表进行合并
list1.extend(list2)
print(list1)    # ['Tom', 'Rose', 'Jack', 'Hack', 'Jennify']

# 2.3 insert()方法：指定位置新增元素（插入数据）
"""列表序列.insert(位置下标，数据)"""
names = ['薛宝钗','林黛玉']
# 在薛宝钗和林黛玉之间，插入一个新元素'贾宝玉'
names.insert(1,'贾宝玉')
print(names)

# 3. 删操作
"""
del列表[索引]        删除列表中的某一个元素
pop()                删除指定下标的数据（默认为最后一个），并返回该数据
remove()             移除列表中某个数据的第一个匹配额
clear()              清空列表，删除列表中的所有元素，返回空列表
"""
# 3.1 del()方法： 删除指定的列表元素
# 基本语法：
names = ['Tom','Rose','Jack','Jennify']
# 删除Rose
del names[1]
# 打印列表，验证删除操作是否成功
print(names)

# 3.2 pop()方法：
"""删除指定下标的元素，如果不填写下标，默认删除最后一个。其返回结果就是删除的这个元素"""
names = ['貂蝉','吕布','董卓']
del_name = names.pop()  # 删除'董卓'

del_name = names.pop(2)
print(del_name)
print(names)

# 3.3 remove()方法：
"""作用：删除匹配的元素（删除指定元素）"""
fruit = ['apple','banana','pineapple']
fruit.remove('banana')     # 删除指定元素'banana'，返回删除后的列表
print(fruit)  # 输出['apple', 'pineapple']  

# 3.4 clear()： 清空列表
names = ['貂蝉','吕布','董卓']
names.clear()
print(names)

# 4. 改操作：
"""
列表[索引] = 修改后的值         修改列表中的某个元素
reverse()                      将数据序列进行倒序排序
sort()                         对列表序列进行排序   
copy()                         对列表序列进行拷贝
"""
# 4.1 列表[索引] = 修改后的值 
list1 = ['貂蝉','大乔','小乔','八戒']  
# 修改列表中的元素
list1 [3] = '周瑜'
print(list1)  # 打印['貂蝉', '大乔', '小乔', '周瑜'] 

# 4.2 reverse()方法： 
list2 = [1,2,3,4,5,6,7,8,9]
list2.reverse()
print(list2)  # 打印[9, 8, 7, 6, 5, 4, 3, 2, 1]，倒序排列，返回倒序排列后的列表

# 4.3 sort()方法： 
""" 列表序列.sort(key=None,reverse=False) """
"""
注意： key = None表示是否指定排序规则（默认为None），按照元素本身进行排序，key = 函数 表示按照函数的返回值进行排序。
       reverse表示排序规则，reverse = True降序，reverse = False升序（默认）  
"""
list3 = [1,2,3,4,5,6,7,8,9]  
list3.sort()  # 升序排列（从小到大），默认参数reverse = False，key = None，按照元素本身进行排序
list3.sort(reverse=True)  # 降序排列（从大到小），参数reverse = True，key = None，按照元素本身进行排序  
print(list3)

# 4.4 copy() 方法：
list4 = list3.copy()  # 复制列表list3
print(list4)


# 三、列表的循环遍历
"""循环遍历就是使用while或for循环对列表中的每个数据进行打印输出"""
# 1. while循环遍历
list1 = ['貂蝉','大乔','小乔']  
i = 0
while i  < len(list1):
    print(list1[i])  # 打印列表中的每个元素
    i += 1

# 2. for循环遍历
list1 = ['貂蝉','大乔','小乔']
for i in list1:  
    print(i)


# 四、列表的嵌套
""" 列表嵌套：列表中又有一个列表，我们把这种情况就称之为列表嵌套 """
students = [['张三','李四'],['王五','赵六'],['田七','孙八']]
print(students[0][1])   # 打印李四
for i in students:
    print(i)  # 打印列表中的每个列表元素





# 作业：
# 1. 幸运数字6（只要是6的倍数）：输入任意数字，如数字8，生成nums列表，元素值为1~8，从中选取幸运数字移动到新列表lucky，打印nums与luck

# 第一步：定义二个空列表
nums = []
lucky = []
# 第一步：提示用户输入数字
num = int(input('请输入任意数字：'))
# 第三步：生成nums列表（把1~num）所有数据都追加到nums列表中
for i in range(1, num + 1):
    nums.append(i)

# 第四步：对nums进行遍历操作，获取幸运数字
for i in nums:
    if i % 6 == 0:
        # 幸运数字从nums中删除
        nums.remove(i)
        # 把幸运数字写入到lucky列表中
        lucky.append(i)
# 第五步：打印nums和lucky
print(nums)  # 打印nums列表中不包含幸运数字
print(lucky)    # 打印幸运数字

# 2. 列表嵌套：有2个教室[],[],[]，8名讲师，['A','B','C','D','E','F','G','H']，将8名讲师随机分配讲师到3个教室中
import random

# 定义3间教室以及8名讲师
rooms = [[],[],[]]
teachers = ['A','B','C','D','E','F','G','H']
# 对所有讲师进行遍历操作
for i in teachers:
    # 生成随机数
    index = random.randint(0, 2) 
    rooms[index].append(i)
# 输出每个教室的讲师信息
print(rooms)
i = 1
for room in rooms:
    print(f'教室{i}的讲师是：{room}')  # 打印每个教室的讲师信息，i是教室的编号
    i += 1
   