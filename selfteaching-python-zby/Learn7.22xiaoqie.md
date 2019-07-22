#### 上下文管理协议

Python中的上下文管理协议中必须包含__enter__()和__exit__()两个方法。

上下文管理器

> 网上能够找到的最通常的说法是：上下文管理器使支持上下文管理协议的对象，这种对象实现了__enter__()和__exit__()方法。

更Python一点的说法，可以说是**在某任务执行之初，上下文管理器做好执行准备，当任务（代码块）执行完毕或者中间出现了异常，上下文管理器负责结束工作。**



```python
#!/usr/bin/env python
# coding=utf-8

read_file = open("23501.txt")
write_file = open("23502.txt", "w")

try:
    r = read_file.readlines()
    for line in r:
        write_file.write(line)
finally:
    read_file.close()
    write_file.close()
```

**如果你不知道“上下文管理器”，这样做无可厚非，可偏偏现在已经知道了，所以，从今以后这样做就不是最优的了，因为它可以用“上下文管理器”写的更好。所以，用with语句改写之后，就是很优雅的了。**
**>>>**

**with**
```python
with open('2305.txt') as read_file, open("23503.txt", 'w') as write_file:
    for line in read_file.readlines():
        write_file.write(line)
```
```python
class ContexManagerOpenDemo(object):
    def __enter__(self):  #先开始
        print("Starting the Manager.")

    def __exit__(self, *others): #再出去
        print("exiting the Manager.")


with ContexManagerOpenDemo(): #再进来
    print("In the manager.")
```

在上面的代码示例中，我们写了一个类ContextManagerOpenDemo()，你就把它理解为我自己写的Open()吧，当然使最简版本了。在这个类中，__enter__()方法和__exit__()方法都比较简单，就是要检测是否执行该方法。

然后用with语句来执行，目的是按照“上下文管理器”的解释那样，应该首先执行类中的__enter__()方法，它总是在进入代码块前被调用的，接着就执行代码块——with语句下面的内容，当代码块执行完毕，离开的时候又调用类中的__exit__()。
执行结果：
```python
Starting the Manager.
In the manager.
exiting the Manager.
>>> 

```python
class ContexManagerOpenDemo(object):

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        
    def __enter__(self):
        print("Starting the Manager.")
        print('*'*17)
        self.open_file = open(self.filename, self.mode)
        return self.open_file
    

    def __exit__(self, *others):
        self.open_file.close()
        print('*'*17)
        print("exiting the Manager.")


with ContexManagerOpenDemo("test.txt", 'r') as reader:
    print("In the manager.")
    for line in reader:
        print(line)
```

**>>>>**


```python
Starting the Manager.
*****************
In the manager.
Hello World, 

This data will be written to the file.Don't delete existing data 

Add this to the existing file.You have a good job.we have a good choiceAdd this to the existing file.

You have a good job.

we have a good choice.

*****************
exiting the Manager.
>>> 
```

**这段代码的意图主要是：**

- 通过__init__()能够读入文件名和打开模式，以使得看起来更接近open()；
- 当进入语句块时，先执行__enter__()方法，把文件打开，并返回该文件对象；
- 执行代码块内容，打印文件内容；
- 离开代码块的时候，执行__exit__()方法，关闭文件。**


**contextlib模块**

Python中的这个模块使上下文管理中非常好用的东东，这也是标准库中的一员，不需要另外安装了。

常用的是contextmanger、closing和nested。

contextlib.closing()
有一种或许常用到的情景，就是连接数据库，并返回一个数据库对象，在使用完之后关闭数据库连接，其形状如下：
```python
with contextlib.closing(CreateDB()) as db:
    db.query()
```
以上不是可运行的代码，只是一个架势，读者如果在编码中使用，需要根据实际情况改写。

当数据库语句**db.query()** 结束之后，数据库连接自动关闭。   

contextlib.nested()

nested的汉语意思是“嵌套的，内装的”，从字面上读者也可能理解了，这个方法跟嵌套有关。前面有一个示例，是从一个文件读取，然后写入到另外一个文件。我不知道读者是否想过可以这么写：
```python
with open("23501.txt") as read_file：
    with open("23503.txt", "w") as write_file:
        for line in read_file.readlines():
            write_file.write(line)
```

```python
import contextlib

with contextlib.nested(open("23501.txt", "r"), open("23503.txt", "w")) as (read_file, write_file):
    for line in read_file.readlines():
        write_file.write(line)
```
**体会一下上面两段代码的魅力**



**contextlib.contextmanager**

contextlib.contextmanager是一个装饰器，它作用于生成器函数（也就是带有yield的函数），一单生成器函数被装饰以后，就返回一个上下文管理器，即contextlib.contextmanager因为装饰了一个生成器函数而产生了__enter__()和__exit__()方法。例如：

特别要提醒，被装饰的生成器函数只能产生一个值，否则就会抛出RuntimeError异常；如果有as子句，则所产生的值，会通过as子句赋给某个变量，就如同前面那样，例如下面的示例:

```python
import cairo
from contextlib import contextmanager

@contextmanager
def saved(cr):
    cr.save()
    try:
        yield cr
    finally:
        cr.restore()

def tree(angle):
    cr.move_to(0, 0)
    cr.translate(0, -65)
    cr.line_to(0, 0)
    cr.stroke()
    cr.scale(0.72, 0.72)
    if angle > 0.72:
        for a in [-angle, angle]:
            with saved(cr):
                cr.rotate(a)
                tree(angle * 0.75)

surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, 280, 204)
cr = cairo.Context(surf)
cr.translate(140, 203)
cr.set_line_width(5)
tree(0.75)
surf.write_to_png('fractal-tree.png')
```


错误和异常(1)

- 语法错误(syntax errors)
- 跟踪记录(Traceback)”，还可以给它取一个更优雅的名字“回溯

|异常|描述|
| -- | --- |
|NameError|尝试访问一个没有申明的变量|
|ZeroDivisionError|除数为0|
|SyntaxError|语法错误|
|IndexError	|索引超出序列范围|
|KeyError	|请求一个不存在的字典关键字|
|IOError	|输入输出错误（比如你要读的文件不存在）|
|AttributeError	|尝试访问未知的对象属性|

如果读者在调试程序的时候遇到了异常，不要慌张，这是好事情，是python在帮助你修改错误。只要认真阅读异常信息，再用dir()，help()或者官方网站文档、google等来协助，一定能解决问题。


**处理异常**
处理异常的方式之一，使用try...except...。
在except子句中，有一个raise

```python
class Calculator(object):
    is_raise = False
    def calc(self, express):
        try:
            return eval(express)
        except ZeroDivisionError:
            if self.is_raise:
                print("zero can not division.")
            else:
                raise
            
if __name__ == "__main__":
    c = Calculator()
    c.is_raise = True #通过实例属性修改
    print (c.calc("8/0"))

>>>
zero can not division.
None 
#最后的None是c.calc("8/0")的返回值，因为有print c.calc("8/0")，所以被打印出来。
>>> 
```

**错误和异常(2)**

处理多个异常
```python
所谓处理多个异常的意思是可以容许捕获不同的异常，有不同的except子句处理。

while 1:
    print("this is a division program.")
    c = input("input 'c' continue, otherwise logout:")
    if c == 'c':
        a = input("first number:")
        b = input("second number:")
        try:
            print(float(a)/float(b))
            print("****************")
        #except ZeroDivisionError:
        #    print("The second number can't be zero!")
        #    print("*"*20)
        #except ValueError:
        #    print("please input number.")
        #    print("*"*20)
        except (ZeroDivisionError, ValueError):
            print ("please input rightly.")
            print ("********************")
        except (ZeroDivisionError, ValueError) as e:
            print(e)

    else:
        break
```

以上程序中，之处理了两个异常，还可能有更多的异常呢？如果要处理，怎么办？可以这样：execpt:或者except Exception as e，后面什么参数也不写就好了。
```python
#!/usr/bin/env python
# coding=utf-8
while 1:
    try:
        x = input("the first number:")
        y = input("the second number:")

        r = float(x)/float(y)
        print (r)
    except Exception as e:
        print (e)
        print ("try again.")
    else:
    #finally: 和else:的区别
        break

```
需要对程序中的except简单说明，这次没有像前面那样写，而是except Exception, e，意思是不管什么异常，这里都会捕获，并且传给变量e，然后用print e把异常信息打印出来。

```python
x = 10
try:
    x = 1/0
except Exception as e:
    print(e)

finally:
    print("del x")
    del x

>>>
division by zero
del x
>>> x
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> 

```

**将上面的各个子句都综合起来使用，写成如下样式：**
```python
try:
    do something
except:
    do something
else:
    do something
finally
    do something
```

错误和异常(3)

**assert**

assert，翻译过来是“断言”之意。assert是一句等价于布尔真的判定，发生异常就意味着表达式为假。

```python
class Account(object):
    def __init__(self, number, balance):
        self.number = number
        self.balance = 0

    def deposit(self, amount):
        assert amount > 0
        self.balance += balance

    def withdraw(self, amount):
        assert amount > 0
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("balance is not enough")

if __name__ == '__main__':
	a = Account(1000)
	a.deposit(-10)
>>>
Traceback (most recent call last):
  File "<pyshell#3>", line 3, in <module>
    a.deposit(-10)
  File "/Users/liwei/Documents/Others/acco.py", line 9, in deposit
    assert amount > 0
AssertionError
```

**如果没有特别的目的，断言应该用于如下情况：**

- 防御性的编程
- 运行时对程序逻辑的检测
- 合约性检查（比如前置条件，后置条件）
- 程序中的常量
- 检查文档

(上述要点来自：Python 使用断言的最佳时机 )

>**不论是否理解，可以先看看，请牢记，在具体开发过程中，有时间就回来看看本教程，不断加深对这些概念的理解，这也是master的成就之法。**

