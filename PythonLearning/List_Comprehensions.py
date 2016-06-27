'''
列表生成式能够快度的创建list 生成式
'''

from numpy.core.fromnumeric import size
L=list(range(15,20))
print(L)
L=list(x*x for x in range(1,11))# 输出1到10的平方
print(L)
L=[x*x for x in range(1,11) if x%2 ==0] #输出1到10偶数的平方
print(L)
L=[m*n for m in range(1,11) for n in range(11,21) if m%2==0 and n%2!=0 ] #双重循环
print(L)
print(size(L))
import os
print([d for d in os.listdir('.')])  #输出当前目录下的文件和目录
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[x for x in L1 if isinstance(x, str)]  #判断是不是字符串
print(L2)