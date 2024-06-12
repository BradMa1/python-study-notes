# 1.需求分析：
"""
参与游戏的角色有两个（电脑和玩家），玩家手工出拳，电脑随机出拳，根据石头剪刀布判断输赢

玩家：player（玩家要手动输入 石头、剪刀、布）
电脑：computer（随机出拳）

输赢结果有三种情况：
1.玩家赢
player：石头    computer：剪刀
player：剪刀    computer：布
player：布      computer：石头

2.平局
只要player和computer出拳一样，就代表平局

3.电脑赢
如果不满足以上两个条件，则电脑获胜！
"""

# 2.代码实现
# 第一步：提示用户输入石头剪刀布，0代表石头，1代表剪刀，2代表布
player = int(input('请输入您的出拳0代表石头，1代表剪刀，2代表布：'))
# 第二步：电脑随机出拳(后续完善)
computer = 1
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0) :
    print('恭喜你赢了！')
elif player == computer:
    print("平局")
else :
    print('很遗憾，你输了！')



# 2.电脑随机出拳实现方法(使用random模块)
# Python其中有很多模块（module），这些模块可以帮我们实现很多功能，我们直接导入到程序中即可使用
'''
import 导入模块
通过模块.方法(参数) 调用相关功能

'''
# 导入模块（后面一般空两行）
import random


# 生成0-2之间的随机数
print(random.randint(0,2))


# 改进猜拳代码
import random


player = int(input('请输入您的出拳0代表石头，1代表剪刀，2代表布：'))
computer = random.randint(0,2)
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0) :
    print('恭喜你赢了！')
elif player == computer:
    print("平局")
else :
    print('很遗憾，你输了！')




# 三目运算符:
# 在Python中，三目运算符也叫三元运算符，其主要作用：就是用于简化if...else...语句

# 基本语法:
'''
if 条件判断：
    语句段1
else:
    语句段2
    '''
# 转换为三目运算符：
""" 语句段1 if 条件判断 else 语句段2 """

# 案例：输入两个数值，返回最大值
num1 = 10
num2 = 20
if num1 > num2:
    print(f'最大值为：{num1}')
else :
    print(f'最大值为：{num2}')
# 简化：三目运算符
mum1 = 10
num2 = 20
max = num1 if num1 > num2 else num2
print(f'最大值为：{max}')

