#  在Python中，如果想让Python程序接受用户的输入信息，可以使用`input()`函数。该函数会提示用户输入信息，并将输入的信息作为字符串返回。

#  基本语法：

input()



#  但往往只有input()方法，其意义不大，我们还应该使用一个变量来临时接受用户的输入，以方便后期的操作。

变量名称 = input('提示信息：')



#  案例：银行系统中的，输入密码过程
password = input('请输入您的密码：')
print(f'您输入的密码为：{password}')



#  所有由input()返回的值都是字符串类型
#  如果需要将其转换为其他类型，可以使用int()、float()等函数进行类型转换
name = input('请输入您的姓名：')
age = input('请输入您的年龄：')
print(type(name))   # <class 'str'>
print(type(age))    # <class 'str'>

#  转换为整数类型
age = int(input('请输入您的年龄：'))