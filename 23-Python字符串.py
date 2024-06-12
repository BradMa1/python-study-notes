# 一. 字符串的定义：
'''字符串是Python中常用的数据类型，一般使用引号来创建字符串。创建字符串很简单，只需为变量分配一个值即可。'''

# 案例1：使用单引号或双引号定义字符串变量
str1 = 'abcdefg'
str2 = "Hello World"

print(type(str1))  # 输出：<class 'str'>
print(type(str2))    # 输出：<class 'str'>


# 案例2：使用三个引号定义字符串变量
name3 = '''Tom'''
name4 = """Rose"""

a = '''I am Tom,
    nice to meet you!'''

b = """I am Rose,
    nice to meet you too!"""
# 注意：三引号的字符串支持换行操作


# 案例3：思考如何使用字符串定义“ I'm Tom ”
# 使用单引号情况：
str1 = 'I\'m Tom '  
print(str1)  # 输出：I'm Tom

"""
单引号在字符串定义中必须成对出现，而且Python解析器在解析代码时，会自动认定第一个单引号和最近的一个单引号是一对
如果一定要在单引号中使用单引号，可以使用转义字符'\'（转义）来完成
"""

# 使用双引号情况:
str2 = """ I'm Tom """
print(str2)  # 输出：I'm Tom
# 注：在Python中，如果存在多个引号，建议单引号放在双引号中，双引号放在单引号中




# 二、 字符串的输入
'''在Python中, 可以使用input()函数来获取用户输入的信息
input()函数返回的结果是一个 字符串类型 的数据
'''
name = input("请输入您的姓名：")
age = input("请输入您的年龄：")
address = input("请输入您的地址：")
print(name, age, address)





# 三、字符串的输出
# 1. 普通输出：
'''
print(变量名称)
print(变量名称1, 变量名称2, 变量名称3, ...)
'''
# 2. 格式化输出：
# 2.1 百分号
name = input("请输入您的姓名：")
age = int(input("请输入您的年龄："))
address = input("请输入您的地址：")

print('我的名字是：%s 我今年岁:%d 我住在：%s...'%(name, age, address))

# 2.2 format方法：
name = input("请输入您的姓名：")
age = int(input("请输入您的年龄："))
address = input("请输入您的地址：")

print('我的名字是：{} 我今年岁:{} 我住在：{}...'.format(name, age, address))

# 2.3 f形式：
name = input("请输入您的姓名：")
age = int(input("请输入您的年龄："))
address = input("请输入您的地址：")

print(f'我的名字是：{name} 我今年岁:{age} 我住在：{address}...')

# 2.3.1 延申：
name = input('请输入您购买商品的名称：')
price = float(input('请输入您购买商品的价格：'))
print(f'购买商品名称为：{name}，购买商品价格为：{price:.2f}')




# 四、字符串在计算机底层的存储形式
'''
在计算机中，Python中的字符串属于序列结构。所以其底层存储占用一段连续的内存空间
'''
# 1. 索引下标：就是编号，通过下标快速找到对应的数据
# 1.1 例子：
str1 = 'abcdefg'
print(str1[0])  # 输出：a   
print(str1[3])  # 输出：d

print(str1[6])  # 输出：g
print(str1[-1])  # 输出：g





# 五、字符串切片
'''
切片是指对操作的对象截取其中一部分的操作，字符串、列表、元组都支持切片操作
'''
# 1. 字符串切片基本语法
'''
序列名称[开始位置下标：结束位置下标：步长]

1. 不包含结束位置下标对应的数据，正负数均可
2. 步长是选取间隔，正负数均可，默认步长是1（正数是从左往右截取，负数反之）
'''
# 2. 例子：对numstr字符串进行切片
numser = '0123456789'
'''
正索引   0     1    2    3    4    5    6    7    8    9 
负索引  -10   -9   -8   -7   -6   -5   -4   -3   -2   -1
值       0     1    2    3    4    5    6    7    8    9    
'''
# 3. 字符串切片小口诀
'''顾头不顾尾，步长为正则正向移动，步长为负则逆向移动
'''

# 4. 字符串切片练习1
numstr = '0123456789'
# 4.1 从2到5开始切片，步长为1
print(numstr[2:5:1])
print(numstr[2:5])

# 4.2 只有结尾的字符串切片:代表从索引为 0 开始，截取到结尾字符 -1 位置
print(numstr[:5])   # 01234

# 4.3 只有开头的字符串切片：代表从起始位置开始，一直截取到字符串的结尾
print(numstr[1:])

# 4.4 获取或拷贝整个字符串
print(numstr[:])

# 4.5 调整步阶
print(numstr[::2])

# 4.6 把步阶设置为负整数（类似字符串翻转）
print(numstr[::-1])

# 4.7 起始位置与结束位置都是负数（遵循一个原则：必须是从左向右截取）
print(numstr[-4:-1])

# 4.8 结束字符为负数，如截取0123456789
print(numstr[:-1])

# 4. 字符串切片练习2
'''给定一个图片的名称为"avatar.png"，使用Python方法获取整个图片的名称（avatar）以及这个图片的后缀（.png）'''

filename = "avatar.png"
index = 6   # 获取点号的索引下标

name = filename[:index]  # 使用切片获取文件的名称
print(f'上传文件的名称为：{name}')

postfix = filename[index:]  # 使用切片获取文件的后缀
print(f'上传文件的后缀为：{postfix}')





# 六、字符串的操作方法（内置）
# 1. 字符串中的查找方法
'''查找某个子符串在字符串中的位置或出现的次数'''
# 1.1 find()方法
"基本语法：字符串.find('要查找的字符或者子串')"

'''检测某个子串是否包含在这个字符串中，如果在则返回这个子串开始的位置下标，否则则返回-1'''

str1 = 'hello word hello linux hello python'
print(str1.find('linux'))   # 查找linux子串是否出现在字符串中
print(str1.find('and'))   # 在str1中查找不存在的子串（不存在返回：-1）

# 案例：使用input方法输入任意一个文件名称，求点号的索引下标
filename = input('请输入上传文件名称：')
index = filename.find('.')
print(index)
print(filename[:index]) # 求文件名称
print(filename[index:])  # 求文件后缀

# 1.2 index()方法
'''index方法其功能与find方法完全一致，唯一的区别在于当要查找的子串不存在时，find()方法返回-1，而index()方法会报错'''
str1 = 'apple,banana,orange'
# 判断apple是否出现在字符串str1中
print(str1.index('apple'))
print(str1.index('pear'))  # 报错

# 1.3 rfind()方法与rindex()方法
'''r = right,代表从右开始查找'''

"""
字符串序列.rfind(子串)
字符串序列.rindex(子串)
"""
# 强调：rfind()方法与rindex()方法适合于查找子串在字符串中出现多次的情况

# 案例：有一个文件名称叫20210310axvu.avatar.png,其中点号出现了2次,需要获取文件后缀.png
filename = '20210310axvu.avatar.png'
index = filename.find('.')    # 求出点号在字符串中第一次出现的位置
print(index) 

index = filename.rfind('.')     # 求出点号在字符串中最后一次出现的位置
print(index) 
 
# 1.4 count()方法
'''
主要功能：统计某个子串在字符串中出现的次数
基本语法：
字符串.count('子串'，开始位置下标，结束位置下标)
'''
# 案例：获取字符串中and关键字出现的次数
str1 = 'hello world and hello linux and hello python'
ands = str1.count('and')
print(f'and出现的次数为：{ands}')

# 练习：使用循环嵌套打印正等腰三角形
i= 1
while i <= 6:
    print(' '*(6 - i),end = '')     # 打印空行 
    j = 1
    while j <= (2 * i - 1):
       
        print('*', end='')
        j += 1  
    print('')
    i += 1  




# 2. 字符串的修改方法
''''指通过函数（方法）的形式修改字符串中的数据'''
# 2.1 replace()方法
'''
基本语法：
字符串.replace(旧子串（要替换的内容），新子串（替换后的内容），次数（默认替换所有）)
'''
# 案例：编写一个字符串，然后把字符串中的里的linux替换成python
str1 = 'hello linux and hello linux '
print(str1.replace('linux', 'python'))  # 替换所有linux子串
print(str1.replace('linux', 'python', 1))   # 替换第一个linux子串

'''目前工作中，replace()方法主要用于实现关键字替换或过滤功能。  北京--> BJ,  敏感词过滤:共产党-->***** '''


# 2.2 split()切割方法
'''
作用：对字符串进行切割操作，返回一个list()列表类型的数据
'''
# 定义一个要切割的字符串
str1 = 'apple-banana-orange'
# 使用split()方法切割字符串
print(str1.split('-'))


# 2.3 capitalize()方法
'''
作用：将字符串的首字母转换为大写（其余字符都为小写）
'''
str1 = 'myName'
print(str1.capitalize())    # 把str1变成首字符大写字符串


# 2.4 title()方法
'''
作用：将字符串中所有单词的首字母转换为大写，组成大驼峰
'''
str1 = 'student_manager'

print(str1.title())     # 把str1变成大驼峰 
print(str1.title().replace('_', '\t',1))  


# 2.5  upper()与lower()方法
'''
upper()：把字符串全部转换为大写形式
lower()：把字符串全部转换为小写形式
'''
# 案例：用户名以及密码验证案例
username = input('请输入您的账号：')
password = input('请输入您的密码：')

# 把username或password全部转换为大写或小写
print(username.upper())
print(password.lower())


# 2.6 lstrip()、rstrip()方法与strip()方法
'''
lstrip()：删除字符串左侧的空白字符
rstrip()：删除字符串右侧的空白字符
strip()： 删除字符串两侧的空白字符（如空格）
'''
username = input('请输入您的账号：')
password = input('请输入您的密码：')

# 去除字符串两侧的空格
print(len(username))    # len()函数:输出字符串长度
print(username.strip())
print(len(username))


# 2.7 ljust()、rjust()、center()
'''
作用：返回原字符串左对齐、右对齐以及居中对齐

基本语法：
字符串序列.ljust(长度,填充字符)
'''
# 案例：定义一个字符串，要求返回长度为10个字符，不足的使用.（点号）进行填充
str1 = 'python'
print(str1.ljust(10,'.'))   # 左对齐 python....
print(str1.rjust(10,'.'))   # 右对齐 ....python
print(str1.center(10,'.'))   # 居中对齐 .python.



# 3. 字符串的判断方法
''' 所谓判断即是判断真假，返回的结果是布尔类型数据：True或False '''  
# 3.1 startswith()
'''
作用：检查字符串是否以指定子串开头，是则返回True，否则返回False。
      如果设置开始和结束位置下标，则在指定范围内检查
'''
str1 = 'python program'
print(str1.startswith('python'))

# 3.2 endswith() 
'''
作用：检查字符串是否以指定子串结尾，是则返回True，否则返回False。
      如果设置开始和结束位置下标，则在指定范围内检查
'''
str2 = 'avatar.png'
print(str2.endswith('.png'))

if str2.endswith('.png') or str2.endswith('.jpg') or str2.endswith('gif'):
    print('是一张图片格式的图片')
else:
    print('您上传的文件格式异常')

# 3.3 isalpha()
'''
作用：判断字符串是否只由字母组成，如果字符串中所有字符都是字母则返回True，否则返回False
'''
str1 = 'admin'
str2 = 'admin123'

print(str1.isalpha())   # True
print(str2.isalpha())   # False

# 3.4 isdigit()
'''
作用：如果字符串只包含数字则返回True，否则返回False
'''
password = input('请输入您的账户密码：')
if len(password) == 6 and password.isdigit():
    print('密码输入正确,正在验证...')
else:
    print('密码输入错误，请重新输入')

# 3.5 isalnum()
'''
作用：判断字符串是否由字母和数字组成，如果字符串中所有字符都是字母或数字则返回True，否则返回False
'''
username = input('请输入您的用户名（只能为字母+数字形式）：')
if username.isalnum():
    print('用户名输入正确，正在登陆...')
else:
    print('输入的用户名有误，请重新输入')


# 3.6 isspace()
''' 作用：如果字符串中只包含空白，则返回True，否则返回False（逆向思维）'''
str1 = ''   # 至少要包含一个空白字符
print(str1.isspace())

username = input('请输入您的用户名：')
if len(username) == 0 or username.isspace():
    print('您没有输入任何字符...')
else:
    print(f'您输入的用户名是：{username}')



