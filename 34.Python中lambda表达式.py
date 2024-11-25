# 一、lambda表达式：

# 1.普通函数与匿名函数
"""
在Python中，函数是一个被命名的、独立的完成特定功能的一段代码，并可能给调用它的函数一个返回值。所以在Python中，函数大数是有名函数 =>普通函数。
但是有些情况下，我们为了简化程序代码，也可以定义匿名函数 => lambda表达式。
"""

# 2.lambda表达式应用场景
"""如果一个函数有一个返回值，并且只有一句代码，可以使用lambda表达式简化。"""

# 3.lambda表达式基本语法
"""
变量 =  lambda 函数参数：表达式（函数代码 + return返回值）

# 调用函数
变量（函数参数） # 注意：lambda表达式只能写一行代码，并且不能写return
"""
# 注意：lambda表达式的参数可有可无，函数的参数在lambda表达式中完全适用
      # lambda表达式能接收任何数量的参数但只能返回一个表达式的值

# 4.编写lambda表达式
def fn1():
  return 100

# 调用fn1函数
print(fn1)  # 返回fn1函数在内存中的地址
print(fn1())  # 代表找到fn1函数的地址并立即执行

# lambda表达式进行简化：
fn2 = lambda: 100

print(fn2)  # 返回fn2函数在内存中的地址
print(fn2())  

# 5.编写带参数的lambda表达式
# 编写一个函数求两个数的和
def fun1(num1,num2):
    return num1 + num2

print(fun1(10,20))

# lambda表达式进行简化：
fn2 = lambda num1,num2: num1 + num2

print(fn2(10,20))


# 6.lambda表达式相关应用

# 1.无参数：
fn1 = lambda: 100
print(fn1())

# 2.一个参数：
fn2 = lambda num1: num1 + 100
print(fn2(10))

# 3.默认参数：
fn3 = lambda a,b,c=10: a + b + c
print(fn3(10,20))

# 4.可变参数：*args
fn4 = lambda *args: args
print(fn4(10,20,30,40,50))  # 返回值为元组

# 5.可变参数：**kwargs
fn5 = lambda **kwargs: kwargs
print(fn5(name='张三',age=18))  # 返回值为字典

# 6.带if判断的lambda表达式
fn6 = lambda num1,num2: num1 if num1 > num2 else num2 # 结合三目运算符使用
print(fn6(10,20))

# 7.列表数据 + 字典数据排序（重点）
students = [
    {'name': 'Tom', 'age': 20},
    {'name': 'Rose', 'age': 19},
    {'name': 'Jack', 'age': 22},
]

# 按name值升序排序
students.sort(key=lambda x: x['name'])
print(students)

# 按age值降序排序
students.sort(key=lambda x: x['age'])
print(students)

# 按name值降序排序
students.sort(key=lambda x: x['name'],reverse=True)
print(students)

# 按age值降序排序
students.sort(key=lambda x: x['age'],reverse=True)
print(students)

