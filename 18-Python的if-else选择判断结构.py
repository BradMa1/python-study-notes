# 1.if选择判断结构的的基本语法
"""
if 条件判断:
    如果条件为True，则执行某段代码...
    如果条件为True，则执行某段代码...

print() # if结构以外的代码，不受if结构的限制

"""

# 案例代码：
if True:
    print('条件成立执行的代码1')
    print('条件成立执行的代码2')

#下方的代码没有缩进到if语句块中，所以和if条件无关

print('无论条件是否成立都要执行的程序')



# 2.if选择性结构安案例
# 需求：定义一个变量age =18，判断这个变量是否大于或等于18岁，如果满足条件，则输出“成年人”，否则输出“未成年人”

# 案例1；直接定义，进行条件判断
age = 18
if age >= 18:
    print('成年人')

# 案例2: 网吧上网
age =int(input('请输入您的年龄：'))
if age >= 18:
    print('满足18岁要求，可以上网')

    

# 3. if...else...选择判断结构

'''
基本语法：
if  条件判断:
    如果条件为True，则执行某段代码...
else:
    如果条件为False，则执行另一段代码...
'''

# 案例3: 网吧上网升级版，引入else
age = int(input('请输入您的年龄：'))
if age >=18:
    print('满足18岁要求，可以上网')
else:
    print('不满足18岁要求，不能上网')

    
# 4. if...elif...else多条件判断结构
"""
if 条件判断1：
    如果此条件为True，则执行此段代码...
elif 条件判断1：
    如果此条件为True，则执行此段代码...
elif ...
    ...
else:
    如果以上所有条件判断都不满足时，则执行此段代码...

"""



# 案例：

'''
中国合法工作年龄为18-60岁，即如果年龄小于18的情况为童工，不合法：
如果年龄在18-60岁之间为合法工龄
大于60岁为法定退休年龄

'''
# 定义一个变量，接收用户输入的年龄
age = int(input('请输入您的年龄：'))
if age < 18:
    print('童工')
elif age >= 18 and age <= 60:
    print('合法工龄')
elif age >60:
    print('法定退休年龄')
else:
    print('信息输入有误，请重新输入')

# 5. and 表示范围的简写形式

age >= 18 and age <= 60
#可以简写为
18 <= age <= 60 


# 5. if 嵌套语句
"""
基本语法：

if 外层条件判断：
    
    如果条件为True，则执行以下语句

    if 内层条件判断：
        
        如果内层条件为True，则执行以下语句
else:
    如果条件为False，则执行以下语句

"""
# 嵌套结构编写时，先编写外层判断，所有语句编写完成后，再编写内层条件判断结构

# 案例: 外层条件：是否有钱，有钱可以上车。内层条件：判断是否有空座位，如果有则可以坐下
'''
根据条件（是否有钱）判断是否可以上车
money = 0 没钱
money = 1 有钱

'''
money = 1
seat = 1
if money == 1:
    print('有钱，可以上车')
    if seat == 1:
        print('有座位，可以坐下')
    else:
        print('没有座位，只能站着回家了')
else:
    print('没钱，只能走路回家')

