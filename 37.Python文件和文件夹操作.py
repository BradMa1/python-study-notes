# 一、os模块
'''在Python中文件和文件夹的操作要借助os模块相关功能，具体步骤如下：'''

# （1）导入os模块：
import os

# （2）调用os模块的相关功能
'''
os.函数（）
'''



# 二、与文件操作相关方法
"""
os.rename(目标文件名称,新文件名称) # 对文件进行重命名操作
os.remove(要删除的文件名称) # 对文件进行删除操作

"""

# 案例：把Python项目目录下的python.txt文件，重命名为linux.txt,休眠20s，查看效果，对文件进行删除操作

# 第一步：导入os模块
import os
# 第三步：导入time模块
import time


# 第二步：使用os.rename()方法对python.txt进行重命名操作
os.rename("python.txt", "linux.txt")

# 第四步：休眠20s
time.sleep(20)

# 第五步：删除文件（linux.txt）
os.remove("linux.txt")



# 三、文件夹相关操作
"""
函数                                                作用

os.mkdir(文件夹名称)                      创建一个指定名称的文件夹
os.getcwd()                              获取当前工作目录 current work directory
os.chdir(目标文件夹路径)                  切换目录 change directory
os.listdir(目标目录)                      获取指定目录下的文件信息，返回列表
os.rmdir(目标目录)                        用于删除一个指定名称的“空”文件夹(无法删除非空文件夹)

"""



# 四、路径小知识
"""
绝对路径：从根目录开始的路径
D:\python\static

相对路径：
  在文件操作中，经常要切换路径，在Python中常见路径一共有三情况：
(1).同级路径：都在同一个文件夹中，兄弟关系，如static目录下有file1.txt和file2.txt，则file1.txt和file2.txt就是同级关系，
    同级访问直接使用名称即可。

(2).下一级路径：文件与另一个文件存在上下级关系，如images文件夹中存在一个avatar文件夹，则images是上级目录，avatar是下级目录。
    则我们访问avatar可以通过  images/avatar来实现（“文件夹名/文件名”的方式）。

(3).上一级路径：从当前目录下，跳出到外一层路径，可以使用../来实现（“../文件名”的方式）。

"""


# 案例1：使用mkdir方法创建一个images目录，

import os #导入os模块


# 1.使用os.mkdir()方法创建一个images目录
os.mkdir("images")
os.mkdir("images/avatar")

# 2.使用os.getcwd()方法获取当前工作目录
print(os.getcwd()) # 获取当前工作目录

# 3.切换目录
os.chdir('images/avatar')
print(os.getcwd())

os.chdir("../../") # 切换到上一级目录
print(os.getcwd())

# 4.使用os.listdir()打印当前所在目录下的所有文件，返回列表
print(os.listdir())

# 5.使用os.rmdir()删除空目录
os.rmdir("images/avatar")



# 案例2：准备一个static文件夹以及、file2.txt和file3.txt，三个文件
"""
(1).在程序中，将当前目录切换到static文件夹
(2).创建一个新images文件夹以及test文件夹
(3).获取目录下的所有文件
(4).移除test文件夹
"""


# 导入os模块
import os


# (1).在程序中，将当前目录切换到static文件夹
os.chdir("static")
print(os.getcwd())

# (2).创建一个新images文件夹以及test文件夹
os.mkdir("images")
os.mkdir("test")

# (3).获取目录下的所有文件
print(os.listdir())
for file in os.listdir():
    print(file)

# (4).移除test文件夹
os.rmdir('test')


# 五、文件夹删除补充（递归删除、慎重）

"""
递归删除文件夹的原理：
  理论上，在其删除过程中，如果文件夹非空，则自动切换到文件夹的内部，然后把其内部的文件，
  一个一个删除，当所有文件删除完毕后，返回到上一级目录，删除文件夹本身。
"""

# 导入shutil模块
import shutil


# 递归删除非空目录
shutil.rmtree("要删除文件夹的路径")




# 六、文件操作综合案例

# 1、需求分析
"""
需求：批量修改文件名，既可添加指定字符串，也可删除指定字符串。

python-file1.txt  
python-file2.txt  
python-file3.txt

"""

# 2、步骤
"""
(1).设置添加删除字符串的标识
(2).获取指定目录下的所有文件
(3).将原有文件名添加/删除指定字符串，构造新名字
(4).使用os模块的os.rename（）方法，对文件进行重命名操作
"""

# 3、编写实例代码

# 1、导入os模块
import os


# 2、定义要重命名的目录
path = "./static"

# 3、切换到上面指定的目录中
os.chdir(path)
print(os.getcwd())

# 5、定义一个标识，用于确认是添加字符还是删除字符
flag = int(input('请输入要执行的操作（1-添加字符，2-删除字符）：'))

# 4、对目录中的所有文件进行遍历输出
for file in os.listdir():
    # 5、判断我们要执行的操作（1-添加字符，2-删除字符）
    if flag == 1:
        # 01.txt => python-01.txt
        newname = "python-" + file
        # 重命名操作
        os.rename(file,newname)
        print('文件批量命名成功')

    elif flag == 2:
        # python-01.txt => 01.txt
        index = len('python-')
        newname = file[index:]
        # 重命名操作
        os.rename(file,newname)
        print('文件批量命名成功')
    else:
        print("输入错误，请重新输入")
  

