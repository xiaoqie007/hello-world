
#### **Inheritance** 继承
对继承的认识会更深刻。好友令狐虫曾经这样总结继承：

> 从技术上说，OOP里，继承最主要的用途是实现多态。对于多态而言，重要的是接口继承性，属性和行为是否存在继承性，这是不一定的。事实上，大量工程实践表明，重度的行为继承会导致系统过度复杂和臃肿，反而会降低灵活性。因此现在比较提倡的是基于接口的轻度继承理念。这种模型里因为父类（接口类）完全没有代码，因此根本谈不上什么代码复用了。

在Python里，因为存在Duck Type，接口定义的重要性大大的降低，继承的作用也进一步的被削弱了。

另外，从逻辑上说，继承的目的也不是为了复用代码，而是为了理顺关系。

```python
__metaclass__ = type

class Person:
    def speak(self):
        print("I love you.")

    def setHeight(self):
        print('The height is: 1.60m.')

    def breast(self, n):
        print('My breast is:', n)


class Girl(Person):
    def setHeight(self):
        print('The height is:1.70m.')


if __name__ == "__main__":
    Cang = Girl()
    Cang.setHeight()
    Cang.speak()
    Cang.breast(80)
```

#### 多重继承

所谓多重继承，就是只某一个类的父类，不止一个，而是多个。比如：
```python
class Person:
    def eye(self):
        print("two eyes")

    def breast(self, n):
        print("The breast is:", n)

class Girl:
    age = 28
    def color(self):
        print('The girl is white')

class HotGirl(Person, Girl):
    pass


if __name__ == "__main__":
    kong = HotGirl()
    kong.eye()
    kong.breast(80)
    kong.color()
    print(kong.age)#在对HotGirl实例化之后，因为继承的原因，这个类属性也被继承到HotGirl中，因此通过实例属性kong.age一样能够得到该数据。
```

```python
class K1(object):
    def foo(self):
        print('K1-foo')

class K2(object):
    def foo(self):
        print('K2-foo')
    def bar(self):
        print("K2-bar")

class J1(K1, K2):
    pass

class J2(K1, K2):
    def bar(self):
        print('J2-bar')

class C(J1,J2):
    pass

if __name__ == '__main__':
    print(C.__mro__) # 要打印出类的继承顺序
    m = C()
    m.foo()
    m.bar()
#即C==>J1==>J2==>K1；bar()也是按照这个顺序，在J2中就找到了一个。这种对继承属性和方法搜索的顺序称之为“广度优先”。
>>>
(<class '__main__.C'>, <class '__main__.J1'>, <class '__main__.J2'>, <class '__main__.K1'>, <class '__main__.K2'>, <class 'object'>)
K1-foo
J2-bar

```

#### **super函数**

```python

__metaclass__ = type

class Person:
    def __init__(self):
        self.height = 160

    def about(self, name):
        print("{} is about {}".format(name, self.height))

class Girl(Person):
    def __init__(self):
        #super(Girl, self).__init__()
        self.breast = 90

    def about(self, name):
        #super(Girl, self).about(name)
        print("{} is a hot girl, she is about {}, and her breast is {}".format(name, self.height, self.breast))
        #super(Girl, self).about(name)
if __name__ == "__main__":
    cang = Girl()
    cang.about("canglaoshi")
```
不存在super的运行结果情况如下：(报错)
```
Traceback (most recent call last):
  File "/Users/liwei/Documents/Others/class_super.py", line 20, in <module>
    cang.about("canglaoshi")
  File "/Users/liwei/Documents/Others/class_super.py", line 16, in about
    print("{} is a hot girl, she is about {}, and her breast is {]".format(name, self.height, self.breast))
AttributeError: 'Girl' object has no attribute 'height'
>>> 
```
- Girl（） 中 __init__(self) 和 about(self, name) 重写覆盖了 Person中的对应，为了再此显示出来需用 super 调用父类同方法
- 格式：super函数的参数，第一个是当前子类的类名字，第二个是self，然后是点号，点号后面是所要调用的父类的方法。同样在子类重写的about方法中，也可以调用父类的about方法。


用super后解决如下：
```
>>>canglaoshi is about 160
>>>canglaoshi is a hot girl, she is about 160, and her breast is 90
```


#### **类**
在前面几节讨论类的时候，经常要将类实例化，然后通过实例来调用类的方法（函数）。在此，把前面经常做的这类事情概括一下：

- **方法是类内部定义函数，只不过这个函数的第一个参数是self。（可以认为方法是类属性，但不是实例属性）**

- **必须将类实例化之后，才能通过实例调用该类的方法。调用的时候在方法后面要跟括号（括号中默认有self参数，但是不写出来。）**



**静态方法和类方法**

```python
__metaclass__ = type

class StaticMethod:
    @staticmethod
    def foo():
        print('This is static method foo().')


class ClassMethod:
    @classmethod
    def bar(cls):
        print('This is class method bar().')
        print("bar() is part of class:", cls.__name__)

if __name__ == "__main__":
    static_foo = StaticMethod()
    static_foo.foo()
    StaticMethod.foo()
    print("**********")
    class_bar = ClassMethod()
    class_bar.bar()
    ClassMethod.bar()


#@staticmethod 表示下面的方法是静态方法
#@classmethod 表示下面的方法是类方法
```


**静态方法和类方法   ????**

已知，类的方法第一个参数必须是self，并且如果要调用类的方法，必须将通过类的实例，即方法绑定实例后才能由实例调用。如果不绑定，一般在继承关系的类之间，可以用super函数等方法调用。

这里再介绍一种方法，这种方法的调用方式跟上述的都不同，这就是：静态方法和类方法
先看静态方法，虽然名为静态方法，但也是方法，所以，依然用def语句来定义。需要注意的是文件名后面的括号内，没有self，这和前面定义的类中的方法是不同的，也正是因着这个不同，才给它另外取了一个名字叫做静态方法，否则不就“泯然众人矣”。如果没有self，那么也就无法访问实例变量、类和实例的属性了，因为它们都是借助self来传递数据的。

在看类方法，同样也具有一般方法的特点，区别也在参数上。类方法的参数也没有self，但是必须有**cls这个参数**。在类方法中，能够方法类属性，但是不能访问实例属性（读者可以自行设计代码检验之）。

简要明确两种方法。下面看调用方法。两种方法都可以通过实例调用，即绑定实例。也可以通过类来调用，即StaticMethod.foo()这样的形式，这也是区别一般方法的地方，一般方法必须用通过绑定实例调用。