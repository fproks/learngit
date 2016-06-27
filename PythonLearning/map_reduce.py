'''
map 和reduce 的用法
map调用一个函数和一个迭代器，并将这个函数作用于这个迭代器上
'''
from functools import reduce
def normalize(name):
    return name.capitalize()  #将字符串的第一个字母大写，其他字母小写
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

'''
reduce 会将得到的作用结果与之后的迭代器进行运算
'''
def ps(x,y):
    return x*y
def prod(L):
    return reduce(ps,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


c='123.456'
print(c.find('.'))
print(len(c)-c.find('.'))
def num(x,y):
    if(y==None):
        return x
    else:
        return x*10+y
def normal(L):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    if(L!='.'):
        return  char2num(L)

p=list(map(normal,c))
print(reduce(num,p)/(pow(10, len(c)-c.find('.')-1)))
