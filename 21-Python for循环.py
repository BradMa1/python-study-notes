# 一、for循环基本语法及其运用
# 1. for循环基本语法
'''
for循环结构主要用于序列（字符串、列表、元组、集合以及字典）类型数据的遍历（循环）操作
当循环此时未知时，建议使用for循环
'''

'''for 临时变量 in 序列:
    重复执行的代码1
    重复执行的代码2
'''

'''
for循环功能非常强大，可以自动判断序列的长度。长度为多少，则for循环就循环多少次。每次循环，系统会自动将序列中的每个元素赋值给变量 i，
赋值完成后，for循环内部会自动更新计数器，向后移动一位，继续循环，直至元素全部循环结束
'''
# 案例：使用for循环遍历字符串"Brad"
str1 = "Brad"
for i in str1:
    print(i)
    
# 案例：使用for循环遍历列表[1,2,3,4,5]
list1 = [1,2,3,4,5]
for i in list1:
    print(i)



# 2. range()函数
# 主要作用：用于生成一段连续的内容
# 基本语法：
'''
range(stop)
range(start, stop[, Step])
'''

'''
start：计数从start开始，默认是从0开始。例如：range (5 )等价于range (0, 5)
stop：计数到 stop 结束,但不包括 stop。例如：range (0, 5) 是[0, 1, 2, 3, 4]没有5
step：步长，默认是1。例如：range (0, 5) 等价于range (0, 5, 1)

'''
# range有一个口诀：顾头不顾尾，包含头部信息，但是不包含尾部信息.如range(10)则返回0~9之间的序列，又比如range(0,5)代表返回0~4之间的序列

# 案例：for循环与range方法，使用for循环，循环5次
for i in range(5):
    print(i)


# 3. for循环案例
# 案例1：使用for循环，求1~100之间的所有整数之和
sum = 0
for i in range(1,101):
    sum += i
print(f'1~100的和为：{sum}')

# 案例2：使用for循环，求1~100之间的所有偶数之和
# 方法一：偶数：i %2 == 0
sum = 0
for i in range(1,101):
    if i % 2 == 0:
        sum += i
print(f'1~100之间的所有偶数之和为：{sum}')

# 方法二：
sum = 0
for i in range(2,101,2):
    sum += i
print(f'1~100之间的所有偶数之和为：{sum}')


# 4. 循环中的两大关键字
'''
在循环结构中 存在两个关键字：break和continue
break:主要功能是终止整个循环
continue：主要功能是终止本次循环，继续下一次循环
'''
# 案例：遇到字符'w',则终止整个循环
str1 = "abcdefghijklmnopqrstuvwxyz"
for i in str1:
    if i == 'w':
        break
    print(i,end=' ')

# 案例：遇到字符'w',则跳过循环，继续下一次循环
str1 = "abcdefghijklmnopqrstuvwxyz"
for i in str1:
    if i == 'w':
        continue
    print(i,end=' ')

# 5. 综合案例：使用for循环实现用户名 + 密码认证
'''
输入用户名和密码
判断用户名和密码是否正确（username ='admin',password='admin123456'）
登录仅有3次机会，超过3次会报错
'''
'''
分析：用户登录情况有3种：
1. 用户名错误（此时便无需判断密码是否正确）--登录失败
2. 用户名正确，密码错误--登录失败
3. 用户名正确，密码正确--登录成功
'''

# 定义变量，用于记录登录次数
trycount = 0
# 循环3次，因为超过3次就会报错
for i in range(3):
    # 更新登陆次数
    trycount += 1 
    #提示用户输入账号与密码
    username = input("请输入您的登录账号：")
    password = input("请输入您的登录密码：") 
    # 判断用户名与密码是否正确
    if username == "admin":
        # 判断密码是否正确
        if password == "admin888":
            print("恭喜你，登录成功！")
            break 
        else:
            print("登录失败，密码错误！")
            print(f"您还有{3 - trycount}次机会")    
    else:
        print("登录失败，用户名错误！")
        print(f"您还有{3 - trycount}次机会")
        

# 6. for循环嵌套
# for循环嵌套，就是一个for循环里嵌套另一个for循环的写法
'''
基本语法：

# 外层循环
for i in 序列1：
    # 内层循环
    for j in 序列2：
        # 循环体 
'''

# 案例：使用for循环嵌套实现打印九九乘法表
'''
分析：外层循环主要用于控制循环的行数，内层循环主要用于控制循环的列数
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j} x {i} = {i * j}',end = "\t")
    print('\n') # 换行