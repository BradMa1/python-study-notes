#  基本语法：
#  print('字符串{}'.format(变量名称1))
#  print('{}字符串{}'.format(变量名称1, 变量名称2))

#  案例：定义两个变量，name ='孙悟空'，mobile ='13812345678'，按照以下格式进行输出"姓名：孙悟空，联系方式：13812345678"
name ='孙悟空'
mobile = '13812345678'
print('姓名：{}，联系方式：{}'.format(name,mobile))


#  format简写形式(推荐)：
#  print(f'{变量名称1}字符串{变量名称2}')

name ='孙悟空'
mobile = '13812345678'
print(f'姓名：{name}，联系方式：{mobile}')
