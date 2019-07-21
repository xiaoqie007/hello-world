#### 特殊方法(2)

 __getattr__、__setattr__和其它类似方法

```python
__setattr__(self,name,value)：如果要给name赋值，就调用这个方法。
__getattr__(self,name)：如果name被访问，同时它不存在的时候，此方法被调用。
__getattribute__(self,name)：当name被访问时自动被调用（注意：这个仅能用于新式类），无论name是否存在，都要被调用。
__delattr__(self,name)：如果要删除name，这个方法就被调用。
```
```python
"""
study __getatter__ and __setattr__
"""
class Rectangle(object):
    """
    the width and length of Rectangle
    """
    def __init__(self):
        self.width = 0
        self.length = 0

    def setSize(self, size):
        self.width, self.length = size

    def getSize(self):
        return self.width, self.length

    size = property(getSize, setSize)

if __name__ == "__main__":
    r = Rectangle()
    r.width = 3
    r.length = 4
    #print(r.getSize())
    #r.setSize((30,40))
    print(r.size)
    r.size = 30, 40
    print(r.width)
    print(r.length)
```
```python
class NewRectangle(object):
    def __init__(self):
        self.width = 0
        self.length = 0

    def __setattr__(self, name, value):
        if name == "size":
            self.width, self.length = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if name == "size":
            return self.width, self.length
        else:
            raise AttributeError

if __name__ == "__main__":
    r = NewRectangle()
    r.width = 3
    r.length = 4
    print (r.size)
    r.size = 30, 40
    print (r.width)
    print (r.length)
```
```python
class NewRectangle(object):
    def __init__(self):
        self.width = 0
        self.length = 0

    def __setattr__(self,name, value):
        if name == "size":
            self.width, self.length = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if name == "size":
            return self.width, self.length
        else:
            raise AttributeError



if __name__ == "__main__":
    r = NewRectangle()
    r.width = 3
    r.length = 4
    print(r.size)
    
    r.size = 30, 40
    print (r.width)
    print (r.length)

获得属性顺序

通过实例获取其属性（也有说特性的，名词变化了，但是本质都是属性和方法），如果在__dict__中有相应的属性，就直接返回其结果；如果没有，会到类属性中找

```python
class A(object):
    author = "qiwsir"
    def __getattr__(self, name):
        if name != "author":
            return "from starter to master."

if __name__ == "__main__":
    a = A()
    print a.author
    print a.lang
-------------------
qiwsir
from starter to master.
>>>
```
>当a = A()后，并没有为实例建立任何属性，或者说实例的__dict__是空的，这在上节中已经探讨过了。但是如果要查看a.author，因为实例的属性中没有，所以就去类属性中找，发现果然有，于是返回其值"qiwsir"。但是，在找a.lang的时候，不仅实例属性中没有，类属性中也没有，于是就调用了__getattr__()方法。在上面的类中，有这个方法，如果没有__getattr__()方法呢？如果没有定义这个方法，就会引发AttributeError，这在前面已经看到了。

#### 双下划线

至此，是否注意到，我们使用很多以双下划线开头和结尾的方法名，比如__dict__，__init__个。在Python中，用这种方法表示特殊的方法名，当然，这是一个惯例，之所以这样做，主要是确保这些特殊的方法名不会跟你自己所定义的名称冲突，我们自己定义名称的时候，是绝少用双划线开头和结尾的。如果你需要重写这些方法，当然是可以的，具体参看前文关于继承的讲述。



**迭代器** __iter__
>提醒注意，如果读者用的是python3.x，迭代器对象实现的是__next__()方法，不是next()。并且，在python3.x中有一个内建函数next()，可以实现next(it)，访问迭代器，这相当于于python2.x中的it.next()（it是迭代对象）。

```python
"""
compute Fibonacci by iterator
"""
__metaclass__ = type

class Fibs:
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a+self.b
        return fib

if __name__ == "__main__":
    fibs = Fibs(5)
    print(list(fibs))
```

 
生成器 **generator**

生成器和迭代器有着一定的渊源关系。
生成器必须是可迭代的，诚然它又不仅仅是迭代器，但除此之外，又没有太多的别的用途，所以，我们可以把它理解为**非常方便的自定义迭代器。**

```python
>>> my_generator = (x*x for x in range(4))
>>> for i in my_generator:
	print(i)

	
0
1
4
9
>>> for i in my_generator:
	print(i)

#当第一遍循环的时候，将my_generator里面的值依次读出并打印，但是，当再读一次的时候，就发现没有任何结果。这种特性也正是迭代器所具有的。

>>> my_list = [x**2 for x in range(4)]
>>> for i in my_list:
	print(i)

	
0
1
4
9
>>> for i in my_list:
	print(i)

	
0
1
4
9
>>> 
```
>生成器解析式是有很多用途的，在不少地方替代列表，是一个不错的选择。特别是针对大量值的时候，如上节所说的，**列表占内存较多，迭代器（生成器是迭代器）的优势就在于少占内存**，因此无需将生成器（或者说是迭代器）实例化为一个列表，直接对其进行操作，方显示出其迭代的优势

```python
>>> sum(i for i in range(100))   #简洁
4950
>>> sum([i for i in range(100)])
4950
>>> 
```

定义和执行过程
yield

```python
>>> def g():
	yield 0
	yield 1
	yield 2

	
>>> g
<function g at 0x1044e1ae8>
>>> ge = g()
>>> ge
<generator object g at 0x1044db4f8>
>>> type(ge)
<class 'generator'>
>>> dir(ge)
['__class__', '__del__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__name__', '__ne__', '__new__', '__next__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'gi_code', 'gi_frame', 'gi_running', 'gi_yieldfrom', 'send', 'throw']
>>> next(ge)
0
>>> next(ge)
1
>>> next(ge)
2
>>> next(ge)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    next(ge)
StopIteration
>>> 
```
yield语句的作用，就是在调用的时候返回相应的值。详细剖析一下上面的运行过程：

- ge = g()：除了返回生成器之外，什么也没有操作，任何值也没有被返回。
- next(ge)：直到这时候，生成器才开始执行，遇到了第一个yield语句，将值返回，并暂停执行（有的称之为挂起）。
- next(ge)：从上次暂停的位置开始，继续向下执行，遇到yield语句，将值返回，又暂停。
- next(ge)：重复上面的操作。
- next(ge)：从上面的挂起位置开始，但是后面没有可执行的了，于是next()发出异常。

从上面的执行过程中，发现yield除了作为生成器的标志之外，还有一个功能就是返回值。那么它跟return这个返回值有什么区别呢？

弄清楚yield和return的区别:
```python
>>> def r_return(n):
...     print "You taked me."
...     while n > 0:
...         print "before return"
...         return n
...         n -= 1
...         print "after return"
... 
>>> rr = r_return(3)
You taked me.
before return
>>> rr
3
```
**从函数被调用的过程可以清晰看出，rr = r_return(3)，函数体内的语句就开始执行了**，遇到return，将值返回，然后就结束函数体内的执行。所以return后面的语句根本没有执行。这是return的特点

```python
#下面将return改为yield：
>>> def y_yield(n):
...     print "You taked me."
...     while n > 0:
...         print "before yield"
...         yield n
...         n -= 1
...         print "after yield"
... 
>>> yy = y_yield(3)    #没有执行函数体内语句
>>> yy.next()          #开始执行
You taked me.
before yield
3                      #遇到yield，返回值，并暂停
>>> yy.next()          #从上次暂停位置开始继续执行
after yield
before yield
2                      #又遇到yield，返回值，并暂停
>>> yy.next()          #重复上述过程
after yield
before yield
1
>>> yy.next()
after yield            #没有满足条件的值，抛出异常
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
>一般的函数，都是止于return。作为生成器的函数，由于有了yield，则会遇到它挂起，如果还有return，遇到它就直接抛出SoptIteration异常而中止迭代。

```python
def fibs(max):
    
    
    """
    斐波那契数列的生成器
    """
    
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1

if __name__ == "__main__":
    f = fibs(20)
    for i in f:
        print(i, end = ' ')

```

#### 生成器方法
```python
>>> def repeater(n):
	while True:
		n = (yield n)

		
>>> r = repeater(4)
>>> next(r)
4
>>> next(r)
>>> r.send('Hello')
'Hello'
>>> next(r)
>>> r = repeater(4)
>>> r.send('Hello')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    r.send('Hello')
TypeError: can't send non-None value to a just-started generator
>>> r.send(None)
4
>>> 
```

**close()和throw()**

- throw(type, value=None, traceback=None):用于在生成器内部（生成器的当前挂起处，或未启动时在定义处）抛出一个异常（在yield表达式中）。
- close()：调用时不用参数，用于关闭生成器。