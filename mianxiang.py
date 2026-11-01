#面向对象
'''class Mianxiang:  #类
    hight = 800   #类的属性
    def f(self):
        print('123')

m = Mianxiang()   #实例化一个对象，使用函数
m2 = Mianxiang()
m.f()'''


#m.white = 18
#m2.white = 19

#######区别
#print(m.white)->实例化可以用实例化的属性
#print(Mianxiang.white)->类不能用实例化的属性类


#print(Mianxiang.hight)->类的属性都可以访问
#print(m.hight)->类的属性都可以访问

#print(m2.white)######这个是因为只有类的属性是共享的，实例化的属性不是共享的，
'''print(Mianxiang.hight)

print(Mianxiang.f)#类里函数的地址

print(m.f)#实例化对象的地址'''

#######构造函数
'''class Abc:
    name = "bb"
    def __init__(self):
        self.name = 'bb'
        self.age = 18

abc = Abc()
abc'''

'''class Abc:
    name = "bb"
    def __init__(self):
        self.name = 'bb'

        self.age = 18
    def func(self):
        print(f'123{self.name}\t456{self.age}\n')

abc = Abc()
abc.func()
abc2 = Abc()

abc2.func()'''


class Abc:

    name = "bb"
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def func(self):
        print(f'123{self.name}456{self.age}')

abc = Abc("xx",18)#####构造函数在实例化对象的时候调用  __init__

abc.func()
