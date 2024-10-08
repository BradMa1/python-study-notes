# 一、变量的作用域
# 1.变量的作用域
"""变量的作用域指的是变量的作用范围（变量在哪里可用，在哪里不可用），主要分为两类：局部变量、全局变量"""

# 2.局部变量与全局变量
"""在Python中，定义在函数外部的变量就称之为全局变量;而定义在函数内部的变量就称之为局部变量"""
# 定义在函数外部的变量(全局变量)
num = 10
# 定义一个函数
def func():
    # 函数体代码
    # 定义在函数内部的变量（局部变量）
    i = 1


# 3.变量作用域的作用范围
"""
全局变量：在整个程序范围内都可以使用
局部变量:在函数的调用过程中，开始定义，函数运行过程中生效，函数执行完毕后小销毁
"""
# 3.1全局变量
str1 = 'hello'
# 定义一个函数
def func():
    # 在函数内部调用全局变量str1
    print(f'在局部作用域中调用str1变量：{str1}')


# 直接调用全局变量str1
print(f'在全局作用域中调用str1变量：{str1}')
# 调用func函数
func()


# 3.2局部变量
# 定义一个函数
def func():
    # 在函数内部定义一个局部变量
    num = 10
    print(f'在局部作用域中调用num局部变量：{num}')


# 调用func函数
func()

# 在全局作用域中调用num局部变量
print(f'在全局作用域中调用num局部变量：{num}')  #   NameError: name 'num' is not defined（计算机的垃圾回收机制）
                                              #   在函数内部定义的局部变量，在函数执行完毕后，自动销毁，所以无法在函数外部调用


# 4.global 关键字
# 思考：如果一个数据，在函数A和函数B中都要使用，那么如何解决？----可以将这个数据储存在全局变量里

# 定义全局变量
info = []
# 定义funcA函数
def funcA():
    # 向info全局变量中添加数据
    info.append({...})


# 定义funcB函数
def funcB():
    # 共享全局作用域中的全局变量info
    for i in info:
        ...

# 问题：能否在局部作用域中对全局变量进行修改？----可以

# 定义全局变量num = 10
num = 10
# 定义一个函数func
def func():
    # 尝试在局部作用域中修改全局变量num的值
    num = 20


# 调用函数func
func()
# 尝试访问全局变量num
print(f'全局变量num的值：{num}')    # 输出：全局变量num的值：10

# 最终结果：由运行结果可知，在函数体内部，理论上无法对全局变量进行修改，如果一定要修改，必须使用global关键字。

"""global关键字的作用：将局部变量变成全局变量"""

# 定义全局变量num = 10
num = 10
# 定义一个函数func
def func():
    # 尝试在局部作用域中修改全局变量num的值
    global num
    num = 20


# 调用函数func
func()
# 尝试访问全局变量num
print(f'全局变量num的值：{num}')    # 输出：全局变量num的值：20


# 二、多函数之间数据的共享
# 定义全局变量
info = []

# 定义funcA函数：向全局变量中添加信息
def funcA():
    # 使用gglobal声明全局变量
    global  info
    # 向info全局变量中添加数据
    info.append({...})


# 定义funcB函数：查询功能，需要共享全局作用域中的通讯录讯息
def funcB():
    # 共享全局作用域中的全局变量info
    for i in info:
        ...


# 三、把函数的返回值作为另外一个函数的参数
def test1():
    return 50


def test2(num):
    print(num)


# 1.保存函数test1的返回值
result = test1()


# 2.将函数返回值所在变量作为参数传递到test2函数
test2(result)   # 50


# 四、函数的参数进阶
# 1.函数的参数
""""
在函数定义与调用时，可以根据需求来实现参数的传递。在Python中，函数的参数一共有两种形式：形参、实参

形参：在函数定义时，所编写的参数就称之为形式参数
实参：在函数调用时，所传递的参数就称之为实际参数
"""
def greet(name):        #   name就是在函数greet定义时所编写的参数(形参)
    return name + ',您好'


# 调用函数
name = '老王'
greet(name)   #   '老王'就是在函数greet调用时传递的参数(实参)  

"""
注意：虽然在函数传递时，喜欢使用相同的函数名称作为参数名称，但是两者的作用范围是不同的。
      name = '老王'，代表实参。其是全局变量；而greet(name)函数中的name实际是在函数定义时才声明的变量，所以其实一个局部变量
"""

# 2.函数的参数类型
# 2.1位置参数
""""理论上，在函数定义时可以为其定义多个参数。但是在函数调用时，我们也应该传递多个参数，而且正常情况下，其要一一对应"""
def user_info(name, age, address):
    print(f'我的名字叫{name}，今年{age}岁了，住在{address}')


# 调用函数
user_info('Tom', 23, '云南') 

# 注意：位置参数强调的是参数传递的位置必须一一对应，不能颠倒


# 2.2 关键字参数（Python特有）
"""函数调用，通过“键=值”形式加以指定。可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求"""
def user_info(name, age, address):
    print(f'我的名字叫{name}，今年{age}岁了，住在{address}')


# 调用函数(使用关键字参数)
user_info(name='Tom', address='云南', age=23)   # 注意：顺序可以颠倒


# 2.3 缺省参数（默认值）
"""
缺省参数也叫默认值参数，用于定义函数，为参数提供默认值，调用函数时可不传递该默认参数的值
（注意：所有位置参数必须出现在默认参数前，包括函数定义和调用）
"""
def user_info(name, age,gender='男'):
    print(f'我的名字叫{name}，今年{age}岁了，性别是{gender}')

user_info('李林',25)  
user_info('正华',28)   
user_info('婉儿',18,'女')

# 注意：定义缺省参数时，一定要把其写在参数列表的最右侧

# 2.4 不定长参数
"""
不定长参数也叫可变参数。用在不确定调用时会传递多少个参数（不传参也可以）的场景。
此时，可用 包裹(packing)位置参数，或者 包裹关键字参数，来进行参数传递，从而实现参数的传递。
"""
# 2.4.1 包裹(packing)位置参数
def user_info(*args):   # arguments参数
    # print(args)
    print(f'我的名字叫{args[0]}，今年{args[1]}岁了，住在{args[2]}')


# 调用函数，传递参数
user_info('Tom',23,'美国纽约')

# 注意：传进的所有参数都会被args变量收集，它会根据传递参数的位置进行打包，形成一个元组(tuple)，args是元组类型，这就是包裹位置传递。

# 2.4.2 包裹关键字传递
'''基本语法：'''
def user_info(**kwargs):   # keyword arguments参数
    print(kwargs)   # 字典类型数据，对传递参数没有顺序要求，格式要求key = value
    print(f'我的名字叫{kwargs["name"]}，今年{kwargs["age"]}岁了，住在{kwargs["address"]}')


# 调用函数，传递参数
user_info(name='Tom',age=23,address='美国纽约')

# 注意：传进的所有参数都会被kwargs变量收集，它会根据传递参数的键进行打包，形成一个字典(dict)，kwargs是字典类型

# 综上：无论是包裹位置传递还是包裹关键字传递，都是一个组包的过程
# 组包：就是把多个数据组成元组或者字典的过程


# 五、Python拆包(元组和字典)

"""Python拆包：就是把元组或字典中的数据单独的拆分出来，然后赋予给其它的变量"""
'''拆包：对于函数中的多个返回数据，去掉元组，列表或者字典直接获取里面数据的过程'''

# 1.元组的拆包过程
def func():
    # 经过一系列操作返回一个元组
    return 100,200  #  tuple元组类型的数据


# 定义量两个变量接收元组中的每个数据（拆包）
num1, num2 = func()
# 打印num1和num2的值
print(f'num1的值：{num1}')  # 输出：num1的值：100
print(f'num2的值：{num2}')  # 输出：num2的值：200

# 2.字典的拆包过程(只能把每个元素的key拆出来)
dict1 = {'name':'Tom','age':23}
#拆包的过程（字典）
a, b = dict1
print(a)   # 输出：name
print(b)   # 输出：age
#获取字典中的数据
print(dict1[a])   # 输出：Tom
print(dict1[b])   # 输出：23

# 3.拆包的应用案例

# 案例1：使用至少三种方式交换两个变量的值
# 第一种方式：引入一个临时变量
c1 = 10
c2 = 2
# 引入：临时变量temp
temp = c2
c2 = c1
c1= temp
print(c1,c2)  # 输出：c1的值：2 ,c2的值：10

# 第二种方式：使用加法与减法运算交换两个变量的值（不需要引入临时变量）
c1 = 10
c2 = 2

c1 = c1 + c2
c2 = c1 - c2
c1 = c1 - c2
print(c1,c2)    # 输出：c1的值：2, c2的值：10

# 第三种方法：只有Python才具有的特性，叫做拆包
c1 = 10
c2 = 2

c1,c2 = c2,c1
print(c1,c2)
"""
原理：
第一步：把c2和c1组成一个元组(c2,c1)
第二步：使用拆包特性，把元组中的两个元素分别赋值给c1和c2
"""

# 案例2：Python中数据的传递案例
def func(*args, **kwargs):
    print(args)
    print(kwargs)


#   定义一个元组
tuple1 = (10,20,30)
#   定义一个字典
dict1 = {'first':40,'second':50,'third':60}
#   需求：把元组中的数据传递给*args,字典数据传递给**kwargs
#   如果想把元组传递给*args，必须在tuple1的前面加上一个*号
#   如果想把字典传递给**kwargs，必须在dict1的前面加上两个**号
func(*tuple1, **dict1)


# 六、使用Python函数编写通讯录系统
# 1、通讯录系统最终效果
""" 
    学生管理系统 v1.0
1.添加学生的信息
2.删除学生的信息
3.修改学生的信息
4.查询学生的信息
5.遍历所有学生的信息
6.退出录系统
"""
# 2、功能实现步骤
""""
1.显示功能界面
2.用户输入功能序号
3.根据用户输入的功能序号，执行不同的功能（函数）
4.定义函数
5.调用函数
"""

# 1.封装一个menu函数，用于显示功能界面
def menu():
    print('-' *40)
    print('传智教育学生通讯录管理系统 v1.0')
    print('1.添加学生的信息')
    print('2.删除学生的信息')
    print('3.修改学生的信息')
    print('4.查询学生的信息')
    print('5.遍历所有学生的信息')
    print('6.退出录系统')
    print('-' *40)

# 6.定义一个全局变量
info =[]

# 5.定义add_student函数，用于添加学生信息
def add_student():
    #  定义一个空字典，接受name、age、mobile
    info_dict = {}
    #  提示用户输入学生信息：name、age、mobiole
    info_dict['name'] =input('请输入学生姓名：')
    info_dict['age'] = int(input('请输入学生年龄：'))
    info_dict['mobile'] = input('请输入学生手机号：')
    #  声明全局变量info
    global info
    #  追加数据到info列表中
    info.append(info_dict)
    print('学生信息添加成功！')
    print(info)

# 7.定义del_student函数，用于删除学生信息
def del_student():
    #  提示用户输入要删除的学生信息
    name = input('请输入要删除的学生姓名：')
    global info
    #  遍历info列表，查找name
    for i in info:
        if i['name'] == name:
            info.remove(i)
            print('学生信息删除成功！')
            print(info)
            break    
    else:
        print('学生信息不存在！')

# 8.定义mod_student函数，用于修改学生信息
def mod_student():
    #  提示用户输入要修改的学生信息 
    name = input('请输入要修改的学生姓名：')
    global info
    #  遍历info列表，查找name
    for i in info:
        if i['name'] == name:
           i['name'] = input('请输入修改后的学生姓名：')
           i['age'] = int(input('请输入修改后的学生年龄：'))
           i['mobile'] = input('请输入修改后的学生手机号：')
           print('学生信息修改成功！')
           print(info)
           break
    else:
        print('学生信息不存在！')

# 9.定义show_student函数，用于查询学生信息
def show_student():
   #  提示用户输入要查询的学生信息 
   name = input('请输入要查询的学生姓名：')
   #  遍历info列表，查找name
   for i in info:
       if i['name'] == name:
           print(f'学生姓名：{i["name"]}, 学生年龄：{i["age"]}, 学生手机号：{i["mobile"]}')  
           break
   else:
       print('学生信息不存在！')

# 10.定义show_all函数，用于遍历所有学生信息
def show_all():
    #  直接对info进行遍历操作
    for i in info:
        print(f'学生姓名：{i["name"]}, 学生年龄：{i["age"]}, 学生手机号：{i["mobile"]}')

                  
# 4.编写死循环，让程序可以一直执行下去
menu()
while True:
    # 2.使用input函数接收用户的输入信息
    user_num = int(input('请输入您要操作的功能序号：'))

    # 3.根据用户输入的功能序号，执行相关的功能（使用if多分支条件实现不同的功能）
    if user_num == 1:
        #  添加学生信息
        add_student()
    elif user_num == 2:
        #  删除学生信息
        del_student()
    elif user_num == 3:
        #  修改学生信息
        mod_student()
    elif user_num ==4:
        #  查询学生信息
        show_student()  
    elif user_num == 5:
        #  遍历所有学生信息
        show_all()
    elif user_num == 6:
        #  退出系统
        print('感谢使用传智教育学生通讯录管理系统')
        break
    else:
        print('输入有误，请重新输入...')

