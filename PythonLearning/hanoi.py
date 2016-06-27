# -*- coding : utf-8 -*-
'''
汉诺塔问题
'''
def move(n,a,b,c):
    if(n==1):
        print(a,'->>',c)
    else:
        move(n-1,a,c,b)  #将前n-1个移动到b塔。
        print(a,'->>',c)  #将最后一个移动到c塔
        move(n-1,b,a,c)   #将剩下的n-1个移动到c塔
move(3,'A','B','C')

step=1
def hmove(n,a,c):
    global step
    print('第%d步，将%d号盘由%s移动到%s' %(step,n,a,c))
    step+=1
def hanoi(n,a,b,c):
    if(n==1):
        hmove(1,a,c)
    else:
        hanoi(n-1, a, c, b)
        hmove(n, a, c)
        hanoi(n-1, b, c, a)
hanoi(3, 'A', 'B', 'C')
        