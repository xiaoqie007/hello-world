###函数练习
# 解一元二次方程

#**编写函数的注意事项**

#编写函数，在开发实践中是非常必要和常见的，一般情况，你写的函数应该是：
#- 尽量不要使用全局变量。
#- 如果参数是可变类型数据，在函数内，不要修改它。
#- 每个函数的功能和目标要单纯，不要试图一个函数做很多事情。
#- 函数的代码行数尽量少。
#- 函数的独立性越强越好，不要跟其它的外部东西产生关联。


##统计考试成绩

###找素数

###zip()补充
#### 内建函数zip()
##**zip(*iterables)** zip()的参数是可迭代对象

colors = ['red', 'green', 'bule']
values = [234, 12,89,65]
for col, val in zip(colors, values):
    print(col, val)

#class

#!/usr/bin/env python
# coding=utf-8

__metaclass__ = type #意味着下面的类是新式类

class Person: #声明创建了一个名为“Person”的类，类的名称一般用大写字母开头，如果名称是两个字母，那么两个字母的首字母都要大写
               #例如 class HotPerson"驼峰式命名"
              #类中的函数(方法)de 参数跟以往的参数样式有区别，那么就是每个函数必须包含“self”参数，
                #并且作为默认的第一参数。

    def __init__(self, name):# 初始化函数“__init__” ; 就是在这个类被实例化的同时，通过name参数传一个值，
                             #这个值被一开始就写入了类和实例中，成为类和实例的一个属性
                              # 例如：girl = Person('canglaoshi'),girl是一个实例对象，它通过上面的方式实例化后，就自动
                              #执行了初始化函数，让实例girl就具有了name属性。>>>print(girl.name)>>>canglaoshi
        self.name = name       

    def getName(self):
        return self.name

    def color(self, color):
        print("%s is %s"% (self.name, color))



#初始化的功能，简而言之，通过初始化函数，确定了这个实例(类)的“基本属性“(实例是什么样子的)。比如上面的实例化之后，就确立了实例girl
        #的name是”canglaoshi“
        




class Person:
    def __init__(self, name, lang= "golong", website= "www.google.com"):
        self.name= name
        self.lang= lang
        self.website= website
        self.email= 'qiwsir@gmail.com'

laoqi= Person('LaoQi')
info= Person('qiwsir', lang= 'python', website= 'qiwsir.github.io')

print('laoqi.name= ', laoqi.name)
print('info.name= ', info.name)
print('------')

print('laoqi.lang= ', laoqi.lang)
print('info.lang= ', info.lang)
print('------')

print('laoqi.website= ', laoqi.website)
print('info.website= ', info.website)

#!/usr/bin/env python
# coding=utf-8

__metaclass__ = type             #新式类

class Person:                    #创建类
    def __init__(self, name):    #构造函数
        self.name = name

    def getName(self):           #类中的方法（函数）
        return self.name

    def color(self, color):
        print ("%s is %s" % (self.name, color))

girl = Person('canglaoshi')      #实例化
name = girl.getName()            #调用方法（函数） 
print ("the person's name is: ", name)
girl.color("white")              #调用方法（函数）

print ("------")
print (girl.name)               #实例的属性

