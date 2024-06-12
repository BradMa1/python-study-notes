# 1.算数运算符
"""
+   加              1+1         输出结果为2

-   减              1-1         输出结果为0

*   乘              2*2         输出结果为4

/   除              10/2        输出结果为5

//  整除            9//4        输出结果为2（取商）

%   取余（取模）    9 % 4        输出结果为1

**  幂指数          2**4         输出结果为16，即2的4次方（2 * 2 * 2 * 2）

()  小括号 小括号用来提高运算优先级，比如 （1 + 2）* 3，先计算 1 + 2，所以输出结果为9

"""

# 案例一：四则运算 + - * /
number1 = 10
number2 = 2

print(f'加：{number1 + number2}')   
print(f'减：{number1 - number2}')
print(f'乘：{number1 * number2}')
print(f'除：{number1 / number2}')

# 案例二：Python中的特殊运算符
number1 = 20
number2 = 5
number3 = 6

print(f'整除：{number1 // number2}')
print(f'余数：{number1 % number3}')
print(f'幂指数：{number2 ** 3}')
print(f'优先级:{(number1 + number2)* number3}')

# 案例三：算数运算符案例（求梯形的面积）
a = float(input('请输入上底：'))
b = float(input('请输入下底：'))
h = float(input('请输入高：'))
s = (a + b) * h / 2     #求梯形的面积为：(上底 + 下底) * 高 / 2
print(f'梯形的面积为：{s}')



# 2.赋值运算符
"""

   = 赋值运算符将 = 右侧的结果赋值给等号左侧的变量

"""
# 案例一：把某个值赋给某个变量
num = 100

# 案例二：多个变量同时进行赋值操作
n = 5
f = 10.88
s = 'hello world'

n, f, s = 10, 20.5, 'hello world' #多个变量同时进行赋值操作可简写成这样

# 案例三：多个变量赋予相同的值
a = 10
b = 10

# 简写为：
a = b = 10



# 3.复合赋值运算符
# 复合赋值运算符 = 算数运算符 + 赋值运算符
# 复合赋值运算符的计算顺序 = 先执行算数运算符，执行完毕后，把结果再赋值给左边的变量
"""       
+=      加法赋值运算符      c += a 等价于c = c + a

-=      减法赋值运算符      c -= a 等价于c = c - a

*=      乘法赋值运算符      c *= a 等价于c = c * a

/=      除法赋值运算符      c /= a 等价于c = c / a

//=     整除赋值运算符      c //= a 等价于c = c // a

%=      取余赋值运算符      c %= a 等价于c = c % a

**=     幂赋值运算符        c **= a 等价于c = c ** a

"""

# 综合案例：

i = 1
# += 相加并赋值运算，先加1，再再把值赋给左边的变量
i += 1  # 等价于 i = i + 1
print(f'更新后，i的值为：{i}')  

num1 = 9
# 取模并赋值，先求余数，然后再把结果赋值给左边的变量
num1 %= 2
print(f'更新后，num1的值为：{num1}')

num2 = 2
# 幂指数并赋值，先求幂指数，然后再把结果赋值给左边的变量
num2 **= 2
print(f'更新后，num2的值为：{num2}')


# 4.比较运算符：
# 当使用比较运算符对两个变量进行比较时，其返回的值为布尔类型，其结果为True或False
"""
==       判断相等。如果两个操作数的结果相等，则条件结果为真（True），否则条件结果为假（False）  如a=3，b=3，则（a==b）的结果为True

!=       判断不相等。如果两个操作数的结果不相等，则条件结果为真（True），否则条件结果为假（False）  如a=3，b=3，则（a==b）的结果为True,如a=1，b=3，则（a!=b）的结果为True

>       判断运算符左侧操作数结果是否大于右侧操作数结果，如果大于，则条件为真，否则为假。 如a=7，b=3，则（a>b）的结果为True

<       判断运算符左侧操作数结果是否小于右侧操作数结果，如果小于，则条件为真，否则为假。 如a=7，b=3，则（a<b）的结果为False

>=       判断运算符左侧操作数结果是否大于等于右侧操作数结果，如果大于等于，则条件为真，否则为假。 如a=7，b=3，则（a>=b）的结果为True，如a=1，b=3，则（a>=b）的结果为False

<=       判断运算符左侧操作数结果是否小于等于右侧操作数结果，如果小于等于，则条件为真，否则为假。 如a=3，b=3，则（a<=b）的结果为True

"""

# 案例一：两个数大小的比较
num1 = 10
num2 = 20

print(num1 > num2)  # 输出结果为False
print(num1 < num2)  # 输出结果为True
print(num1 >= num2)  # 输出结果为False 
print(num1 <= num2)  # 输出结果为True
print(num1 == num2)  # 输出结果为False
print(num1 != num2)  # 输出结果为True     




# 练习题1：提示用户输入圆的半径，根据公式S = πr2求圆的面积

π = 3.14
r = float(input('请输入圆的半径：'))
s = π * r ** 2
print(f"圆的面积为：{s}")




# 练习题2：赋值运算 => 输入身高，体重，求BMI = 体重（kg）/身高（m）的平方

height = float(input("请输入身高(m)："))
weight = float(input("请输入体重(kg)："))
BMI = weight / height **2
print(f'您的BMI值为：{BMI}')


# 5.逻辑运算符（与或非）
"""

    and     x and y    布尔“与”：如果 x 为False，x and y返回False，否则它返回y的值            True and False,返回False

    or      x or y     布尔“或”：如果 x 是True，它返回True，否则它返回y的值                   False or True,返回True

    not     not x      布尔“非”：如果 x 为True，返回False。如果 x 为False，它返回True         not True 返回False,not False 返回True

"""

# 表达式1 and 表达式2
# 当表达式1 为True且表达式2为True时，则整个表达式返回结果为True
# 当表达式1或表达式2中有一个表达式为假时，则整个表达式返回结果为False

# 表达式1 or 表达式2
# 当表达式1为True或表达式2为True时，则整个表达式返回结果为True
# 当表式1与表达式2都为False时，则整个表达式才会返回False

# not就是取反，只有一个表达式：not 表达式，如果表达式为True，则not后面就返回False。反之，则返回True

a = 1
b = 2
c = 3

print(a>b) and (b>c)  # False
print(a>b) or (b>c)  # False
print(a<b) or (b>c) # True
print(not (a>b))    # True



# 6.扩展：短路运算

print(3 and 4 and 5)
print(5 and 6 or 7)
4 > 3 and print('hello world') 

'''
# 在逻辑运算中，不一定逻辑运算符的两边都是纯表达式。也可以是数值类型的数据
#  Python会把0、空字符串和None看成False,其它字符和非空字符串都看成True，所以：

# 1.在计算a and b 时，如果a为False，则根据与运算法则，整个结果必定为False，因此返回a;如果a是True，则整个计算结果必定取决于b，因此返回b。
print(3 and 4)  # 4
print(0 and 1)  # 0

# 2.在计算a or b 时，如果a是True，则根据或运算法则，整个结果必定为True，因此返回a;如果a是False，则整个计算结果必定取决于b，因此返回b。
print(6 or 7)   # 6
print(6 and 7 or 8)   # 7
# 所以Python解释器在做布尔运算时，只要能提前确定计算结果，它就不需要继续运算了，直接返回结果

'''


# 7.运算符的优先级
# 先算乘除，后算加减，有括号的先算括号里面的