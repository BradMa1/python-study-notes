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