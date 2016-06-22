L=list(range(100))
print(L[:10])#输出前10个
print(L[:10:2]) #输出前10个，每两个输出一个
name = ['Adam','Alex','Amy','Bob','Boom','Candy','Chris','David','Jason','Jasonstatham','Bill']
i_name = input("please input name : ").title()
wname = []
for n in name:
	if(n.startswith(i_name)):
		wname.append(n)
if(len(wname)!=0):
	print("do you want print %s?"%wname)
else:
	print('couldn`t find')

for i in L:
	i+=1 #无法自增
print(L)
'''
#Python内置的enumerate函数可以把一个list变成索引-元素对，
这样就可以在for循环中同时迭代索引和元素本身：
'''
for i,c in enumerate(L):  
	L[i]+=1
print(L)
