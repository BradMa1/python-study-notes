# 字符串：split()方法
"""作用：根据指定字符对字符串进行分割操作，其返回一个列表"""
fruit = 'apple-banana-orange'
print(fruit.split('-'))     # 输出：['apple', 'banana', 'orange']

# 字符串：join()方法
"""作用：和split()方法正好相反，其主要功能是把序列拼接为字符串"""
''' 字符串.join(数据序列) '''
# 案例：把水果列表['apple','banana','orange']拼接成'apple-banana-orange'
list1 = ['apple','banana','orange']  # 定义列表
print('--'.join(list1))