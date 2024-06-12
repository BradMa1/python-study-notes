# 一. while循环中else的基本语法
# 1. 循环可以和else配合使用，else下方缩进的代码指的是当循环正常结束之后要执行的代码
'''
需求：女朋友生气了，要惩罚：连续说5遍“我错了”，如果道歉正常完毕后女朋友就原谅我了，这个程序怎么写？
'''
# 初始化计数器
i = 0
# 编写循环条件
while i < 5:
    print('我错了')
    # 更新计数器
    i += 1
print('好开心，女朋友原谅我了...')  # 这个print没有循环也能执行，可以用while...else结构优化

# 改进：
i = 0
while i < 5:
    print('我错了')
    i += 1
else:
    print('好开心，女朋友原谅我了...') 


# 2. break关键字对while...else结构的影响 
i = 0
while i < 5:
    if i == 2:
       print('这遍说的不够真诚')
       break      # break跳出循环，不再执行else语句块
    print('我错了')
    i += 1
else:
    print('好开心，女朋友原谅我了...') 

# 3. continue关键字对while...else结构的影响 
i = 0
while i < 5:
    if i == 2:
       i += 1
       print('这遍说的不够真诚')
       continue      
    print('我错了')
    i += 1
else:
    print('好开心，女朋友原谅我了...') 


# 二、for循环中else的基本语法
# 1. 基本语法
'''
for 零时变量 in 序列：
    循环体
else：
    当for循环正常结束之后，要执行的代码
'''

# 2. break关键字对for...else结构的影响
str1 = 'abcdefghijklmnopqrstuvwxyz'
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        break
    print(i)
else:
    print('循环正常结束之后执行的代码')

# 3. continue关键字对for...else结构的影响
str1 = 'abcdefghijklmnopqrstuvwxyz'
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        continue
    print(i)
else:
    print('循环正常结束之后执行的代码')




# 案例：小海龟会画画
# 1. 小海龟模块：
'''
在Python3版本中，新增了了一个模块叫turtle(海龟)模块，专门用于绘制图形图像
'''
# 2. turtle模块使用

# 导入turtle模块
import turtle


# 使用turtle模块中已经定义好的方法
'''
turtle.forward(数值)  # 从左向右绘制一条指定长度的横线（像素）
turtle.backward(数值)  # 从右向左绘制一条指定长度为数值的直线
turtle.left(数值)  # 旋转小海龟左转数值度
turtle.right(数值)  # 旋转小海龟右转数值度
turtle.penup()  # 提笔
turtle.pendown()  # 下笔
turtle.color(颜色)  # 设置海龟的颜色
turtle.pensize(数值)  # 设置海龟的画笔大小
turtle.speed(数值)  # 设置海龟的移动速度
turtle.done()  # 显示海龟绘图窗口
turtle.exitonclick()  # 关闭绘图窗口
turtle.clear()  # 清除绘图窗口
turtle.reset()  # 重置绘图窗口
'''
# 3. 手绘一条直线
import turtle
import time


turtle.forward(100) # 从左向右绘制一条100像素的横线
# 休眠10秒
time.sleep(10)
# turtle.done()

# 4. 使用turtle模块 + for循环绘制五角星
import turtle
import time

turtle.pencolor("red")  # 设置画笔的颜色
for i in range(5):  # 循环五次
    turtle.forward(100)  # 向前移动100像素
    turtle.right(144)   # 向右旋转144度
time.sleep(10)


# 作业：
'''
有一物，不知其数，三三数之余二，五五数之余三，七七数之余二，问物几何？
白话文：有一个数字，不知道具体是多少，用3去除剩2，用5去除剩3，用7去除剩2，问这个数字是多少？100以内的整数
'''
# while循环:
i = 1
while i < 100:
    if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
        print(f'这个数字是：{i}')
    i += 1

# for循环：
for i in range(1, 100):
    if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
        print(f'这个数字是：{i}')


'''
报数字（数7）：
从1开始报数，当需要报出的数字尾数是7或该数字是7的倍数时，则跳过这个数字，不进行报数。所有人都参与报数后，游戏结束。
如输入人数为50，游戏结束，报数的人数为39

分析：
1. 如何判断数字尾数为7，      (i % 10 == 7)
2. 如何判断数字是7的倍数，    (i% 7 == 0)

'''
# 定义一个变量n,用于获取报数人数
n = int(input('请输入报数人数：'))
#开始循环
count = 0
for i in range(1, n+1):
    # 判断数字尾数为7
    if i % 10 == 7:
        continue
    if i % 7 == 0:
        continue
    count += 1

print(f'参与人数为{n}，报数人数为：{count}')


