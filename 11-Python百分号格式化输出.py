#   基本语法：
#   print(变量名称)
#   print('字符串%格式' %（变量名称))
#   print('字符串 %格式 %格式' %（变量名称1,变量名称,变量名称3))
  

#   %格式常见如下：              
#   %s  字符串格式化
#   %d  整数格式化
#   %f  浮点数格式化          


#   案例一；
#   定义两个变量，name = 'Brad',age = 18,按照如下格式进行输出：
#   我的名字是Brad,今年18岁。
name = 'Brad'
age = 18
print('我的名字叫%s,今年%d岁' %(name,age))  #  注意：前面有几个%，后面就应该有几个变量，并且要一一对应，顺序不能颠倒




#   案例二：格式化输出："今天蔬菜特价了，大白菜只要3.5元/斤"
title = '大白菜'
price = 3.5
print('今天蔬菜特价了，%s只要%f元/斤' %(title,price))
print('今天蔬菜特价了，%s只要%.2f元/斤' %(title,price)) #  %.2f表示保留两位小数



#   案例三：定义两个变量 id = 1,name = 'Brad',按照如下格式进行输出：
#   姓名：Brad,学号：00001
id = 1
name = 'Brad'
print("姓名：%s,学号：%d" %(name,id))
print("姓名：%s,学号：%05d" %(name,id)) #  %05d表示前面补0，后面补5个0
print("姓名：%s,学号：%.5d" %(name,id)) #  %.5d表示保留5位



