#  在字符串中，如果出现了 \t 和 \n ，其代表的含义就是两个转义字符
#  \t ：制表符，一个tab键（4个空格）的距离 
#  \n ：换行符


print('****')
print('*\t*\t*\t*')
print('hello\nworld')


#  在默认情况下，每个print()语句都会自动换行(\n)
#  如果不想换行，可以在print()语句的末尾加上end参数，并设置为空字符串(end = '')

print('*', end ='')
print('*', end ='')
print('*', end ='')
