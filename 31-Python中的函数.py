# 作业回顾

# 需求：编写一段Python代码，生成一个随机的4位验证码
# 提前：定义一个字符串
str1="234567689abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"

# 编写Python代码：
"""
1.思考：如果只生成4个字符的验证码，如何保证从字符串中只读取4次（while循环、for循环）
2.如果随机的从str1字符中读取4个字符串？ random.choice() 生成随机数
3.如何从字符串中提取出某个字符 使用索引下标，str1[索引下标]
"""

import random


# 1.定义一个字符串
str1="234567689abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"
code = ""
# 2.编写循坏，只循环4次
for i in range(4):  # 0 1 2 3
    # 3.随机获取str1中的某个字符
    index = random.randint(0,len(str1)-1)   # 索引下标不能超过字符串的长度
    # 4.将随机获取的字符拼接到code中
    code += str1[index]     # code = code1 + code2
# 5.打印4位随机验证码
print(code)



# 一、函数的作用及其使用步骤
# 1.函数的作用：封装代码，提高代码的复用性

# 2.函数的主要作用：
"""
1.模块化编程：将复杂的程序分解为多个小的函数，每个函数只做一件事情
2.提高代码的复用性
"""
# 3.函数的定义：
"""函数是一个被命名的、独立的、完成特定功能的代码块，其可能给调用它的程序一个返回值"""
"""
def 函数名(参数):
    函数体
    ...
    return 返回值
"""
# 函数的调用：'''函数名(参数)'''
# 注意事项：1.不同的需求，参数可有可无。2.在Python中，函数必须先定义后使用

'''
def func(name):
    ...
    函数体代码
    return 返回值


func()
'''



# 二、引入函数

# 案例1：写一个打招呼程序，用于实现向同事打招呼的功能
'''
#见到同事老张
# print('您好')
#见到同事老李
# print('您好')
#见到同事老王
# print('您好')
以上代码虽然可以完成打招呼程序，但重复性代码太多
'''

# 案例2：定义一个打招呼函数，专门用于实现向同事打招呼的功能
# 1.封装一个函数greet()
def greet():
    print('您好')

# 2.调用函数
#见到同事老张
greet()
#见到同事老李
greet()
#见到同事老王
greet()


# 案例3：升级案例2函数，可以实现向不同人打不同的招呼
# 1.封装一个函数greet()， 定义一个参数name
# 2.调用函数
def greet(name):
    print(f'{name},您好')

# 2.调用函数
#见到同事老张
greet('老张')
#见到同事老李
greet('老李')
#见到同事老王
greet('老王')


# 案例4：函数的设计原则“高内聚、低耦合”，函数执行完毕后，应该主动把函数返回给调用处，而不应该都交由print()等函数直接输出

# 1.封装一个函数greet()
def greet(name):
    return name + ',您好'
# 2.调用函数
#见到同事老张
print(greet('老张'))
#见到同事老李
print("\033[0;31;40m\t" + greet('老李') + "\033[0m")    # 使用ANSI转义序列设置文本颜色和样式，这里设置为红色文本，黑色背景
#见到同事老王
print("\033[0;36;40m\t" + greet('老王') + "\033[0m")



# 三、函数的return返回值

# 思考1：如果一个函数有两个return(如下所示)，程序如何执行？
def return_num():
    # 注意：在函数内部，当代码执行到return时，系统会自动认为函数到此执行结束
    return 1
    # 后续代码不会再次执行
    return 2


result = return_num()
print(result)   # 1
"""只执行了第一个return，原因是return可以推出当前函数，导致return后面的代码不再执行"""

# 思考2：如果一个函数有多个返回值，程序如何执行？
"""在Python中，理论上一个函数只能返回一个结果。如果要让一个函数返回多个结果，可以使用 return元组 的形式"""

# 案例1：一个函数同时返回多个值
def return_num():
    return 1,2


result = return_num()
print(result)   # (1, 2)
print(type(result)) # <class 'tuple'>

# 思考3：封装一个函数，参数有两个num1,num2,求两个数的四则运算结果（加减乘除）
def size(num1,num2):
    a = num1 + num2
    b = num1 - num2
    c = num1 * num2
    d = num1 / num2
    return a,b,c,d


# 调用size方法
print(size(20,5))



# 四、Python函数中的说明文档

# 1.定义函数的说明文档
def 函数名(参数):
    """说明文档的位置"""
    '''代码'''
    ...

# 2.查看函数的说明文档
help(函数名)

# 3.案例演示1：
def sum_num(a,b):
    """"求和函数"""
    return a + b

help(sum_num)


# 案例2：定义函数的说明文档
# 1.定义一个menu菜单函数
def menu():
    ...

# 2.定义增加通讯录信息操作方法
def add_students():
    """函数的说明文档：add_students()方法不需要传递任何参数，其功能就是实现对通讯录的增加操作"""
    pass    # 占位符（代码运行到此会自动跳过）

# 3.定义通讯录的修改操作方法
def modify_students():
    pass

# 4.定义通讯录的删除操作方法
def delete_students():
    pass

# 5.定义通讯录的查询操作方法
def find_students():
    pass

# 6.调用函数add_students()
help(add_students)


# 五、函数的嵌套
# 1.函数嵌套的定义：
"""函数嵌套调用指的是一个函数里面又调用了另外一个函数"""

# 2.函数嵌套的基本语法：
def testB():
    print('----testB start----')
    print('这里是testB函数执行的代码...(省略)...')
    print('----testB end----')

def testA():   
    print('----testA start----')
    testB()    # 在testA函数中调用了testB函数
    print('----testA end----')

testA()    # 调用testA函数  

# 3.嵌套函数的执行流程
'''
第一步：Python代码遵循一个“顺序原则”,从上往下，从左往右一行一行执行。
       当代码执行到第1行时，则在计算机内存中定义一个testB()函数，但是其内部的代码并没有执行，跳过第2行继续向下执行
       
第二步：代码执行到第6行时，发现又声明了一个testA()函数，根据函数的定义原则，定义就是在内存中声明有这样一个函数，但是没有真正的调用和执行

第三步：代码继续向下执行，到第11行，发现testA() ，函数体()就代表调用testA() 函数并执行其内部的代码。程序返回到第7行，然后一行一行向下执行，
        执行到第8行，发现testB()，就开始执行testB()函数，原程序处于等待状态

第四步：进入testB()函数，执行输出testB()函数的函数体部分...，当代码完毕后，程序返回到testA()函数中的testB()位置，继续向下执行

最终程序执行完毕！
'''

# 六、函数应用案例：
# 案例1：使用print方法打印一条横线
print('-' *40)

# 案例2：对案例1进行升级，可以根据输入的num数值，生成指定数量的横线
def print_lines(num,length):
    """print_lines()函数的功能是打印指定数量的横线,num为打印的横线数量，length为打印的横线长度"""
    for i in range(num):
        print('-' *length)

# 调用函数
# help(print_lines))
print_lines(4,40)

# 案例3：封装一个函数，用于求3个数的平均值
def average_num(num1,num2,num3):
    """average_num()函数主要用于生成3个数的平均值，一共有3个参数，num1,num2,num3"""
    sum = num1 + num2 + num3
    return sum / 3 

# 调用函数
# help(average_num)
print(average_num(10,20,30))

# 练习题：编写一个函数，有一个参数str1，输入信息如'1.2.3.4.5',使用函数对其进行处理，要求最终返回的结果为'5-4-3-2-1'
def func(str1):
    """str_reverse()函数的功能是反转字符串，str1为输入的字符串"""
    # 方法一：对字符串进行反转操作（切片）
    str1 = str1[::-1]
    return str1.replace('.','-')
    # 方法二：使用split切割，然后reverse进行翻转
    list1 = str1.split('.')
    list1.reverse()
    return '-'.join(list1)
   

# 调用函数
str1 = '1.2.3.4.5'
print(func(str1))   # 5-4-3-2-1




