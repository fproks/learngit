'''
generator 能够根据算法不断生成列表，但是不会保存该列表。这就保证了不会占用过多内存
最简单的generator就是把列表生成式的[]改成()
'''
L=[x*x for x in range(10)]
g=(x*x for x in range(10))
'''
generator 因为没有一次性算出所以数据，因此不能直接输出
但是可以使用for循环或者next(g)一个一个输出
'''
print(L)
for n in g:
    print(n)
'''
generator 实际上是一组算法，在普通算法中使用yield 就可以得到generator
'''
'''
斐波那契数列
这并不是一个函数，而是generator数列，通过调用该算法得到一个generator数列
'''
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b =b,a+b
        n+=1

p=fib(5)
for n in p:
    print(n)
'''
杨辉三角
'''
def tr(max):
    n=1
    b=[1]
    while n<=max:
        yield b
        b=[1]+[b[m]+b[m+1] for m in range(len(b)-1)]+[1]
        n+=1
p=tr(5)
for n in p:
    print(n)