'''
python 接收一个关键字参赛作为扩展
'''
#默认参数

def pwer(x): # 只有一个参数的平方算法，默认
    return x*x

print(pwer(5))
def pwer(x,y):
    if(y<=0):
        return 1
    else:  
        return x*pwer(x,y-1)
print(pwer(5,3))
#print(pwer(5)) 不能再进行调用，因为需要俩参数
def pwer(x,y=2):  #调用默认参数
    if(y<=0):
        return 1
    else:  
        return x*pwer(x,y-1)
print(pwer(5))
print(pwer(5,4))
'''
可变参数，通过*添加一个list进去，调用所以参数
'''
def sum(*number):
    sum=0
    for n in number:
        sum=sum+n
    return sum
L=range(10)
print(sum(*L))  #直接调用一个list
print(sum(1,2,3,4))  #可变参数可以直接调用而不需要构成list或者tuple
'''
关键字参数 定义一个关键字，从中找到想要的参数
关键词参数，接收的是一个dict
可变参数接收的是一个list或者tuple
'''
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('Michael',30)
extra={'city': 'Beiging','job':'Engineer'}
person('Michael',30,**extra)
def person(name,age,*,city):  #通过×号隔开，确定只接收city这个关键词参数，如果已经有了可变参数，就不需要这个*了
    print(name,age,city)
person('Michael',30,city='Beijing')
'''
参数定义的顺序必须是:
必选参数、默认参数、可变参数、命名关键字参数和关键字参数
'''