'''
python 使用for...in 进行迭代操作
注意，python的迭代操作与C++类似，仅能读取，并不能改变数据本身
可以在list tuple 上迭代，也可以在dict(类似与map)上迭代
'''
d={'a':3,'b':2,'c':1}
for k in d:
    print(k)  #通常list 仅能迭代key值
for k,v in d.items():  #items 很重要
    print(k,'is:',v)  #同时迭代得到key 和value
for v in d.values():  #得到value 值
    print(v)

'''
判断一个对象能否被迭代，需要添加collections模块的Iterable 类型判断 
'''
from collections import Iterable
print(isinstance('abc', Iterable))
L=['A','B','C']
'''
使用enumerate 可以得到索引和值，进而改变list中的数据
但是在这里，值仅是一个拷贝，并不能改变原来的数据
for 可以引用多个变量
'''
for i,v in enumerate(L):
    L[i]=i+1
    v=5
print(L)