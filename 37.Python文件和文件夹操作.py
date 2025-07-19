# 1、os模块
'''在Python中文件和文件夹的操作要借助os模块相关功能，具体步骤如下：'''

# （1）导入os模块：
import os

# （2）调用os模块的相关功能
'''
os.函数（）
'''

# 2.与文件操作相关方法
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


