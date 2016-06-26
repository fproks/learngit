import numpy as np
'''
矩阵乘法
'''

a=np.array([[1,0],[0,1]])
b=np.array([[4,1],[2,2]])
print(a @ b)

'''
解包
'''
a,b =range(2)
print(a,b)
c, d, *rest=range(10)
print(c,d)
c, *rest,d =range(10) #中间的*rest 代表了数组中间的一长串数字，c 为数组的开头，d 为数组的结尾
print(c,d)
print(rest)
with open("character.py")as f:
    first, *_,last=f.readlines()
print(first, last)

def sum(a,b,biteme=False):
    if(biteme):
        shutil.rmtree('/')
    else:
        return a+b
print(sum(1,2))
#print(sum(1,2,3)) 会产生错误，因为多了一个参数

