'''
filter 将函数作用于每一个元素，
根据返回值True 还是False判断是否保留该元素
filter 的作用是筛选
'''
def is_odd(n):
    return n%2==1
print(list(filter(is_odd,[1,2,3,4,5,6])))  #删除偶数

c='123.456'
def is_num(n):
    return n.isdigit()  #判断是否为数字字符
print(''.join(list(filter(is_num,c)))) #删除非数字字符
#‘’.join(list)将list转化为字符串
'''
素数序列
'''
def _odd_iter():  #返回一个奇数序列
    n=1
    while True:
        n=n+2
        yield n
'''
filter 使用的函数只能一次次的传入迭代器，并不能传入别的参数
使用lambda可以传入多个参数
例如：
def action(x):
    return lambda y:x+y
a=action(2)  给x传入2
a(22)
'''
'''
素数
'''
def _not_divisible(n):
    return lambda x:x%n >0
def primes():
    yield 2
    it =_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)
for n in primes():
    if n<100:
        print(n)
    else:
        break

def is_palidrome(n):
    st=str(n) #也可以这么写st='%d'%n
    return st!=st[::-1]
output=filter(is_palidrome,range(1,100))
print(list(output))
