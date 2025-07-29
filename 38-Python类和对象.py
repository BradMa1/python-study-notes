# 一、类的定义
"""
在Python中，有两种类的定义方式：Python2(经典类)和Python3(新式类)

"""

# 经典类：不由任意内置类型派生出的类，称之为经典类（在Python2中，类默认都是经典类）
"""
class 类名:
  # 属性
  # 方法

  """

#  新式类：
"""
class 类名():
  # 属性
  # 方法

"""

# 基本语法
class Person():
  # 属性
  # 方法（函数）
  def eat(self):
    print("我喜欢吃零食")
  def drink(self):
    print("我喜欢喝可乐")



# 二、类的实例化（创建对象）
"""
在Python中，类通过实例化来创建对象，即：类名()，创建对象的过程称之为实例化

"""

# 基本语法：
"""
对象名 = 类名()
"""


# 案例：把Person实例化为对象p1

# 1、定义一个类
class Person():
  # 定义相关方法
  def eat(self):
    print("我喜欢吃零食")
  def drink(self):
    print("我喜欢喝可乐")

# 2、实例化对象
p1 = Person()

# 3、调用类中的属性和方法
p1.eat()
p1.drink()


# 三、类中的self关键字
"""
self也是Python内置的关键字之一，其指向了类实例对象本身
"""
# 1、定义一个类
class Person():
  # 定义一个方法
  def speak(self):
    print(self)
    print("Nice to meet you!")
# 2、类的实例化（生成对象）
p1 = Person()
print(p1)

"""总结：类中的self就是谁实例化了这个类，self就指向谁"""


# 四、对象的属性添加与获取
"""
在Python中，任何一个对象都应该由两部分组成：属性 + 方法

属性即是特征，比如：人的姓名、年龄、性别、身高、体重...都是对象的属性

对象属性既可以在类外面添加和获取，也能在类里面添加和获取
"""

# 五、在类的外面添加和获取属性

#####设置
"""
对象名.属性名 = 属性值
"""
# 案例：
# 1、定义一个Person类
class Person():
  pass
# 2、实例化Person类，生成p1对象
p1 = Person()
# 3、给p1对象添加属性
p1.name = "张三"
p1.age = 18
p1.address = "北京"

######获取
"""
获取对象属性的方法可以通过 对象名.属性 来获取
"""
# 案例：
# 1、定义一个Person类
class Person():
  pass
# 2、实例化Person类，生成p1对象
p1 = Person()
# 3、给p1对象添加属性
p1.name = "张三"
p1.age = 18
p1.address = "北京顺义区xxxxx99号"

# 4、获取p1对象的属性
print(f'我的姓名：{p1.name}')
print(f'我的年龄：{p1.age}')
print(f'我的地址：{p1.address}')


# 六、在类的内部获取外部定义的属性
# 1、定义一个Person类
class Person():
  def speak(self):
    print(f'我的姓名：{self.name}，我的年龄：{self.age}，我的住址：{self.address}')

# 2、实例化Person类，生成p1对象
p1 = Person()
# 3、给p1对象添加属性
p1.name = "孙悟空"
p1.age = 500
p1.address = "花果山"
# 4、调用speak方法
p1.speak()


# 七、类中的__init__初始化方法（魔术方法）
"""
在Python中，__xxx__()，的函数叫魔法方法，指的是具有特殊功能的函数。

"""

# 1、__init__()方法 (初始化方法或构造方法)
"""
使用__init__()方法，其作用：实例化对象时，连带其中的参数，会一并传给__init__()函数并自动执行它，__init__()函数的参数列表会在开头多出一项，
它永远指代新建的那个实例对象，Python语法要求这个参数必须要有，名称为self。

"""

# 1.定义一个类
class person():
  # 初始化实例对象属性
  def __init__(self,name,age):
    # 赋予name属性、age属性给实例化对象本身
    # self.实例化对象属性 = 参数
    self.name = name
    self.age = age
    
# 2、实例化对象并传入初始化属性值
p1 = person("孙悟空",500)
# 3.调用p1对象自身属性name与age
print(p1.name)
print(p1.age)

"""
总结：
__init__()方法，在创建一个对象时默认被调用，不需要手动调用。
__init__(self)中的self参数，不需要开发者传递，Python解释器会自动把当前的对象引用传递过去。
"""


# 2、__str__()方法
"""
(1)、当使用print输出对象时，默认打印对象的内存地址.如果类定义了__str__()方法，那么就会打印__str__()中return的结果
(2)、__str__()在类的外部，使用print()时，自动被调用
(3)、在类的内部定义__str__()方法时，必须使用return 返回一个字符串类型的数据

"""

# 没有使用__str__()方法的类：
# 1、定义一个类
class Car():
  # 首先定义一个__init__方法，用于初始化实例对象属性
  def __init__ (self,brand,model,color):
    self.brand = brand
    self.model = model
    self.color = color

  # # 为了得到汽车的相关信息，定义一个方法，用于信息输出
  # def print_info(self):
  #   print(f"汽车品牌：{self.brand}，汽车型号：{self.model}，汽车颜色：{self.color}")

  # 定义一个__str__()方法,用于输出相关信息
  def __str__(self):
    # return "当在外部使用print方法打印对象时，我会自动被调用。。。"
    return f"汽车品牌：{self.brand}，汽车型号：{self.model}，汽车颜色：{self.color}"

# 2、实例化对象c1
c1 = Car("奔驰","S600","黑色")
print() # <__main__.Car object at 0x000002B711EE9DD0> 默认打印对象的内存地址
# c1.print_info()
print(c1) 



# 3、__del__()方法   (删除方法或析构方法)
"""
当删除对象时，python解释器也会默认调用__del__()方法

__del__()方法主要用于：当删除一个对象时，做一些善后处理工作，比如：关闭文件夹操作、释放内存、关闭数据库连接等
"""
class Person():
  # 构造函数__init__
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # 析构函数__del__
  def __del__(self):
    print(f"对象{self.name}已经被删除") 
  
# 实例化对象
p1 = Person("张三",180)
# 删除对象p1
del p1 