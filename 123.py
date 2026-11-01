#1  python基础
"""print('Hellow Word1')
print('Hellow Word2')
print('Hellow Word3')
print('Hellow Word4')
print('Hellow Word5')

print(123)
int
float
bool
complex(复数，实数虚部)
print('dashazi','daeri',sep='\n')
print('dashazi')
print(type(True))
a = 3.123456789
a = 3.123456789
b = "dawdawdadaw"
print("%.5f" % a )
print("%d"% a )
print("%s"% b )
name = "xiaohua"
age = 18
print(f'我名字是{name},年龄{age}')
input()
"""
import text

#2 语法
#if else
'''cj = int(input('cj:'))
if cj>=60:

    print('成绩合格')
else:
    print('成绩不合格')'''
'''cj = input('cj:') 如果是100会报错askm
if cj>='60':

    print('成绩合格')
if cj<'60':
    print('成绩不合格')'''

# if elif  elif
'''a = 95
if 100>= a >=80:
    print('ky')
elif 80> a >=60:
    print("haix")
elif 60> a:
    print("bx")'''
#if if else else 嵌套
#循环语法
'''i = 1
s = 0
while i<=100:
    s += i
    i+=1
    #s += i
print(s)'''
# for

'''for i in range(5):
    print('123')'''
'''s = 0
for i in range(1,101):
    s+=i
    i+=1
    print(s)
print(s)'''
#猜字小游戏
'''import random
a= random.randint(1,100)
i = 0
while i<10:
    i+=1
    Gruss = int(input('你猜一个数字：'))
    if Gruss > a:
        print('有点大了')
    elif Gruss < a:
        print('有点小了')
    elif Gruss == a:
        print('猜对了')
        print('y/n')
        b = input('')
        if b=="n":
            print('hb')
            break
        else:
            i =0
            continue
'''

#列表
#li = [1,2,3]
#li.append(4),直接添加
#li.extend([2,5,4])只能是可迭代对象，超级拆分
#li.insert(0,5)第一个是选择位置 第二个是插入元素
#print(li)

'''li = ['1','2','3']
while True:
    a = input('请输入名字')
    if a in li:
        print(f'不行{a}')
    else:
        print(f'可以{a}')
        li.append(a)
        print(li)
        break'''
#增删查改


'''print('=====昵称管理系统=====1. 新增昵称\n2. 查询昵称（查看全部 / 搜索单个昵称）\n3. 删除昵称\n4. 修改昵称\n0. 退出系统\n请输入功能编号：')
i = ["张力", '王五']
while True:
    a = int(input(':'))

    if a ==1:
        b = input("添加名字")
        if b  in i:
            print('有了换一个')
        else:
            i.append(b)
           

    elif a ==2:
        print(i)
        
    elif a == 3:
        print(f"选择删除谁{i}")
        c = int(input())
        if 0<= c< len(i):
            print('删除成功')
            i.pop(c)
        else:
            print('my')



        
    elif a ==4:
        print(f'修改sm{i}')
        d = int(input())
        if 0<= d< len(i):
            f = input('修改成什么')
            print("修改成功")
            i[d] = f

        else:
            print('失败')



        c
    elif a==0:
        break
'''


#元组 tua不能增删改。只能查询  但是可以是不用种类的（类型）

#######字典
# 创建字典
'''dict1 = {"name":"小华", "age":18, "gender":"男"}
print(dict1['name'])
print(stu["name"])'''
'''stu = {"name":"小华"}
stu["age"] = 18   # key不存在，新增
stu["name"] = "小明" # key存在，修改
print(stu)'''
'''stu = {"name":"小华", "age":18, "gender":"男"}
# pop(key) 指定键删除，返回删掉的值
stu.pop("gender")

# popitem() 删除最后一组键值对
stu.popitem()

# clear() 清空字典，变成空字典
stu.clear()

# del 删除整个字典
del stu
'''

#函数 def 函数名 （）,形参和实参
'''def logion ():
    print("欢迎登入")
    return 20
logion()
print(logion())'''
'''def funa (a=0):
    print(a)
funa()'''
'''def funa(*args):
    print(args)
funa(1,2,3,4,5,6)'''
import requests


'''def x():
    global name 变成了全局变量
    name = 'asd'
    print(name)
x()
print(name)

# 普通函数
def add(a, b):
    return a + b

# 等价 lambda->匿名函数
add_lambda = lambda a, b: a + b
print(add_lambda(2, 3))  # 输出 5

'''


#处理异常
'''try:
    print(a)
except :
    print('baocuo')'''
'''try:
    print(a)
except NameError as e:
    print(e)
    '''
# 万能捕获try:
#    print(a)
#except Exception :#except Exception as e:
 #   print('my')

#try finally
 #raise Exception  主动抛出异常raise


 #import导入模块
 #import  模块名       运用就是  模块名.功能名
from text import funa,name
#funa()
#print(text.name)

'''from text import funa as f,funa2 as f2
f()
f2()'''        #放在__init__.py（类似头文件不要放太多文件）  __all__ = ['导入对应的模块，其他可以直接使用']   其他模块使用：from 包名 import *   (*就是全部导入，否则一个一个导入)

#递归 100+100-1,100+(99+99-1)......
'''def add(a):
    if a==1:
        return 1
    return a +add(a-1)
print(add(100))'''
#1,1,2,3,5,8,13 斐波那契数列
'''def add(n):
    if n<=1:
        return n
    return add(n-2)+add(n-1)   #4.5-3.4.2.3.1.2.0.1
print(add(6))'''

#装饰器
'可以直接@使用其中的所有的代码'

#类似闭包
'低级的'
'''def funa(funb):
    def func(*args):
        print('123')
        #funb()注意错误点
        funb(*args)
    return func

def add(x,y):
    print(f'{x}+{y}={x+y}')

#调用装饰器
a = funa(add)
#funa(10,20)注意错误点
a(10,20)'''



'高级的可以直接使用add了，@一下'
'''def funa(funb):
    def func(*args):
        print('123')
        #funb()注意错误点
        funb(*args)
    return func
@funa
def add(x,y):
    print(f'{x}+{y}={x+y}')

add(10,20)
'''





