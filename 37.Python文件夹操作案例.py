# 案例二：准备一个static文件夹以及file1.txt、 file2.txt、file3.txt三个文件，
"""
1、在程序中，将当前目录切到static文件夹下
2、创建一个新images文件夹以及test文件夹
3、获取目录下的所有文件
4、移除test文件夹
"""

"""
绝对路径：从根目录开始的路径
D:\python\static

相对路径：
1.同级路径，都在同一个文件夹中，兄弟关系，如static目录下有file1.txt和file2.txt，
  则file1.txt和file2.txt就是同级关系，同级访问直接使用名称即可

2.下一级路径，文件与另一个文件存在上下级关系，如images文件夹中存在一个avatar文件夹，
  则images是上级目录，avatar是下级目录。则我们访问avatar文件夹可以通过images/avatar来实现（“文件夹名/文件名”的方式）

3.上一级路径，如果某些时候，想从当前文件，跳出到外一层路径，可以使用../来实现（“../文件名”的方式）
"""

# 导入os模块(os模块的主要功能：系统相关、目录及文件操作、执行命令和管理进程)
import os

# 在程序中，将当前目录切到static文件夹下
os.chdir('static')  # os.chdir()函数用于改变当前工作目录到指定的路径
print(os.getcwd())  # os.getcwd()函数用于获取当前工作目录

# 创建一个新images文件夹以及test文件夹
os.mkdir('images')  # os.mkdir()函数用于创建一个新目录
os.mkdir('test')

# 获取目录下的所有文件
print(os.listdir())  # os.listdir()函数用于列出指定目录下的所有文件和子目录
for file in os.listdir():
    print(file)

# 移除test文件夹
os.rmdir('test')  # os.rmdir()函数用于删除指定目录
