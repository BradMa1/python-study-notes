# 面向对象的三大特性：封装、继承、多态

# 一、Python中的封装
"""
再Python代码中，封装有两层含义：
1. 将属性和方法封装到一个类中
  class Person():
      # 封装属性
      # 封装方法

2. 封装可以为属性和方法添加私有权限


"""
# 1、封装中的私有属性和私有方法
"""
在面向对象代码中，可以把属性和方法分为两大类：公有（属性、方法）、私有（属性、方法）

(1)、公有属性和公有方法：无论是在类的内部还是在类的外部，都可以对属性和方法进行操作。但是有些情况下，
                  我们不希望某些属性和方法被外部访问，这时就可以将属性和方法封装为私有形式。

(2)、私有属性和私有方法：只能在类的内部进行访问和操作，类的外部无法直接访问。
"""

# 2、私有属性的访问限制
"""
设置私有属性或私有方法很简单：只需要在属性名或方法名前增加两个下划线"--"即可。

类中的私有属性和私有方法，不能被其子类继承
"""
# 基本语法：
class Girl():
    def __init__(self, name):
        self.name = name
        self.__age = 18

xiaomei = Girl("小美")
print(xiaomei.name)
print(xiaomei.__age)  # 报错，提示：'Girl' object has no attribute '__age'（Girl对象没有 __age 属性）

"""
由以上代码运行可知，私有属性不能在类的外部被直接访问。
但是想在外部对私有属性进行访问--> 可以定义一个统计的访问"接口"函数，专门用于实现私有属性的访问
"""

# 3、私有属性设置与访问接口
"""
在Python中，一般定义函数名''get_xx()''用来获取私有属性，定义''set_xx()''用来修改私有属性值。
"""
class Girl():
    def __init__(self,name):
        self.name = name
        self.__age = 18

    # 公共方法：提供给外部的访问接口
    def get_age(self):
        # 本人访问：允许直接访问
        # 外人访问：加上限制条件
        return self.__age

    # 公共方法：提供给外部的设置接口
    def set_age(self, age):
        self.__age = age


girl = Girl('小美')
girl.set_age(19)
print(girl.get_age())


# 4、私有方法
"""
私有方法的定义方式与私有属性基本一致，在方法名前加上两个下划线" --方法名() "即可。
"""

# 5、封装性的意义
"""
(1)、以面向对象的思想进行项目开发
(2)、封装数据属性：明确的区分内外，控制外部对隐藏属性的操作行为（过滤异常数据）
"""
class People():
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def tell_info(self):
        print("Name:<%s> Age:<%s>" % (self.__name,self.__age))


    # 对私有属性的访问接口
    def set_info(self,name,age):
        if not isinstance(name,str):
            print("姓名必须是字符串类型")
            return
        if not isinstance(age,int):
            print("年龄必须是整数类型")
            return
        self.__name = name
        self.__age = age


p = People('jack',38)
p.tell_info()


p.set_info('jennifer',18)
p.tell_info()


p.set_info(123,35)
p.tell_info()