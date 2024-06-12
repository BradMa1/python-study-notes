# 使用Python实现超市收银系统

name = input("请输入商品名称：")
id = input("请输入商品编号：")
price = (input("请输入商品价格："))      
print(type(price))
print('您购买了{}，商品编号为{}，商品价格为{}元，欢迎下次光临'.format(name, id, price))

# print(price * 8)  #上述价格为字符串类型，无法进行数学运算，需要将其转换为浮点数类型



# 上述代码中，price = input()返回的是字符串类型，因此price变量无法进行数学运算，因此需要将price变量进行数据类型转换转
"""
常见的数据类型转换：

int(x[base])    # 将x转换为整数，base指定转换的进制，默认为十进制

float(x)        # 将x转换为浮点数

str(x)          # 将x转换为字符串

eval(x)         # 将x转换为表达式,用来计算在字符串中有效Python表达式，并返回一个对象
"""


# 案例一：把用户输入的幸运数字，转换为整数类型

number = input("请输入您的幸运数字：")
print(type(number))
# 数据类型转换，把str字符串类型转换为int整数类型
print('-' * 20)
number = int(number)
print(type(number)) # 还可以简写为：number = int(input("请输入您的幸运数字："))


# 案例二：多种数据类型转换
# 1.整型转浮点类型 int -> float
number1 = 10
print(number1)
print(type(number1))

print(float(number1))
print(type(float(number1)))


# 2.浮点类型转换为整型 float -> int
number2 = 18.88
print(int(number2)) # 将浮点类型转换为整型，小数部分会被截掉（丢失）


# 3.字符串类型转换为整型或浮点型 str -> int/float
str1 = '20'
str2 = '10.88'
print(int(str1))
print(float(str2))



# 案例三：eval()函数的使用，把字符串中的数字转换为原始数据类型
print(input('请输入您购买商品的价格：'))
print(eval(price))
print(type(eval(price)))


type(eval(price))



