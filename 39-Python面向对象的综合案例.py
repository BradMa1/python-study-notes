# 案例1:学员成绩案例

"""需求：定义学员信息类，包含姓名、成绩属性，定义成绩打印方法（90分及以上显示优秀，80分及以上显示良好，
70 分及以上显示中等，60分及以上显示合格，60分以下显示不及格)"""

# 1、定义学员信息类
class Student:
  # 2、定义学员对象属性
  def __init__(self, name, score):
    self.name = name
    self.score = score

  # 3、定义一个方法，用于打印学员的成绩等级
  def print_grade(self):
    if self.score >= 90:
      print(f"学员姓名：{self.name}，学员成绩：{self.score},优秀")
    elif self.score >= 80:
      print(f"学员姓名：{self.name}，学员成绩：{self.score},良好")
    elif self.score >= 70:  
      print(f"学员姓名：{self.name}，学员成绩：{self.score},中等")
    elif self.score >= 60:
      print(f"学员姓名：{self.name}，学员成绩：{self.score},合格")
    else:
      print(f"学员姓名：{self.name}，学员成绩：{self.score},不及格")

# 4、实例化对象
Tom = Student("Tom", 85)
Tom.print_grade()

Jerry = Student("Jerry", 95)
Jerry.print_grade()


# 案例2:小明爱跑步
"""
需求：小明体重75.0公斤，小明每次跑步会减掉0.50公斤，小明每次吃东西体重增加1公斤
分析：①对象：小明   ②属性：姓名、体重   ③方法：跑步、吃东西
"""
# 1、定义Person类
class Person():
  # 2、初始化对象属性，name和weight
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  # 3、定义一个__str__方法打印对象的信息
  def __str__(self):
    return f"姓名：{self.name}，目前体重：{self.weight}KG"
  
  # 4、定义一个run方法代表跑步
  def run(self):
    self.weighet -= 0.5


  # 5、定义一个eat方法代表吃东西
  def eat(self):
    self.weight += 1

# 6、实例化对象
xiao_ming = Person("小明", 75.0)
print(xiao_ming)

# 7、调用方法（吃饭）
xiao_ming.eat()
print(xiao_ming)