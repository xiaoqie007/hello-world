#### 文档字符串

在函数、类或者文件开头的部分写文档字符串说明，一般采用三重引号。这样写的最大好处是能够用help()函数看。
```python
"""This is python lesson"""

def start_func(arg):
    """This is a function."""
    pass

class MyClass:
    """Thi is my class."""
    def my_method(self,arg):
        """This is my method."""
        pass
```

**“多态”**
英文是:Polymorphism，在台湾被称作“多型”。维基百科中对此有详细解释说明。

多型（英语：Polymorphism），是指物件導向程式執行時，相同的訊息可能會送給多個不同的類別之物件，而系統可依據物件所屬類別，引發對應類別的方法，而有不同的行為。簡單來說，所謂多型意指相同的訊息給予不同的物件會引發不同的動作稱之。

再简化的说法就是“有多种形式”，就算不知道变量（参数）所引用的对象类型，也一样能进行操作，来者不拒。

**repr()函数**
著名的repr()函数，它能够**针对输入的任何对象返回一个字符串**。这就是多态的代表之一
```python
>>> repr([1,2,3])
'[1, 2, 3]'
>>> repr({'lang':'python'})
"{'lang': 'python'}"
```
```
class Circle():

    pi = 3.141592

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius


c = Circle()

c.setRadius(5)
print(c.getRadius())
print(c.area())
```

```python
"The code is from: http://zetcode.com/lang/python/oop/"

__metaclass__ = type

class Animal:
    def __init__(self, name= ''):
        self.name = name

    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        print('Meow!')

class Dog(Animal):
    def talk(self):
        print('Woof!')

a = Animal()
a.talk()

c = Cat('Missy')
c.talk()

d = Dog('Rocky')
d.talk()
```


### 封装和私有化  （__name， __python ; @property）

```python
__metaclass__ = type

class ProtectMe:
    def __init__(self):
        self.me = "qiwsir"
        self.__name = "kivi"
        
    @property
    def name(self):
        return self.__name

    
    def __python(self):
        print('I love Python.')


    def code(self):
        print('Which language do you like?')
        self.__python()

if __name__ == '__main__':
    p = ProtectMe()
    print(p.me)
    print(p.name)
    #print(p.__name)
    p.code()
    #p.__python()
    ```
```




#### 特殊方法

__dict__


__slots__


首先声明，__slots__能够限制属性的定义，但是这不是它存在终极目标，它存在的终极目标更应该是一个在编程中非常重要的方面：优化内存使用。


```python
>>> class Spring(object):
	__slots__ = ("tree", "flower")

	
>>> dir(Spring)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', 'flower', 'tree']
>>> Spring.__slots__
('tree', 'flower')
>>> t = Spring()
>>> t.__slots__
('tree', 'flower')
>>> Spring.tree = "liushu"
>>> Spring.flower = "yueji"
>>> t.tree = "guanyulan"
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    t.tree = "guanyulan"
AttributeError: 'Spring' object attribute 'tree' is read-only
>>> t.tree
'liushu'
>>> t.flower
'yueji'
>>> t.flower = "yueji"
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t.flower = "yueji"
AttributeError: 'Spring' object attribute 'flower' is read-only
>>> Spring.flower
'yueji'
>>> 
```
看来__slots__已经把实例属性牢牢地管控了起来，但更本质是的是优化了内存。诚然，这种优化会在大量的实例时候显出效果。

