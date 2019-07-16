#### 自省
- help() >> keywords >> quit(q) >> math(help模式下)
- help('moudles') ， help('math')
- dir():使用内置的 dir() 函数来检查模块（以及其它对象）的内容
- 文档字符串,__doc__ 属性。这个属性是一个字符串，它包含了描述对象的注释。Python 称之为文档字符串或docstring
```
>>> print(str.__doc__)
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
```

#### 检查python对象
对于面向对象的类和类实例也是如此。例如，可以看到每个Python符串都被赋予了一些属性， dir()函数揭示了这些属性。

于是在计算机术语中，对象是拥有标识和值的事物，属于特定类型、具有特定特征和以特定方式执行操作。并且，对象从一个或多个父类继承了它们的许多属性。除了关键字和特殊符号（象运算符，如 + 、 - 、 * 、 ** 、 / 、 % 、 < 、 > 等）外，Python 中的所有东西都是对象。Python具有一组丰富的对象类型：字符串、整数、浮点、列表、元组、字典、函数、类、类实例、模块、文件等。

当您有一个任意的对象（也许是一个作为参数传递给函数的对象）时，可能希望知道一些关于该对象的情况。如希望python告诉我们：

- 对象的名称是什么？
- 这是哪种类型的对象？
- 对象知道些什么？
- 对象能做些什么？
- 对象的父对象是谁？

### 名称(**question?**)
- 并非所有对象都有名称，但那些有名称的对象都将名称存储在其 __name__ 属性中。注：名称是从对象而不是引用该对象的变量中派生的。

```python
>>> dir() #dir()函数
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'ave_num', 'b', 'i', 'less_num', 'less_score', 'lst', 'lst1', 'new_str1', 'new_string', 'num', 'other_str', 'random', 'score', 'sorted_score', 'str_lst', 'string', 'words']
>>> directory = dir #新变量
>>> directory()#跟dir()一样的结果
>>> directory.__name__ #dir()的名字
'dir'
>>> __name__ #这是不一样的
'__main__'
>>> 
```
```python
模块拥有名称，Python 解释器本身被认为是顶级模块或主模块。当以交互的方式运行 Python 时，局部 __name__ 变量被赋予值 '__main__' 。同样地，当从命令行执行 Python 模块，而不是将其导入另一个模块时，其 __name__ 属性被赋予值 '__main__' ，而不是该模块的实际名称。这样，模块可以查看其自身的 __name__ 值来自行确定它们自己正被如何使用，是作为另一个程序的支持，还是作为从命令行执行的主应用程序。因此，下面这条惯用的语句在 Python 模块中是很常见的：
```
```python
if __name__ == '__main__':
    # Do something appropriate here, like calling a
    # main() function defined elsewhere in this module.
    main()
else:
    # Do nothing. This module has been imported by another
    # module that wants to make use of the functions,
    # classes and other useful bits it has defined.
```

#### 类型 type()

#### 标识 id()
```python
>>> print(id.__doc__)
Return the identity of an object.

This is guaranteed to be unique among simultaneously existing objects.
(CPython uses the object's memory address.)
>>> 
```

#### 属性 ( dir(),hasattr(),getattr() )
对象拥有属性，并且**dir()** 函数会返回这些属性的列表。但是，有时我们只想测试一个或多个属性是否存在。如果对象具有我们正在考虑的属性，那么通常希望只检索该属性。这个任务可以由 **hasattr() 和 getattr()** 函数来完成.

```python
>>> hasattr(id, '__int__')
 
False
>>> hasattr(id, '__name__')
 
True
>>> hasattr(id, '__doc__')
 
True
>>> print(getattr(id, '__doc__'))
 
Return the identity of an object.

This is guaranteed to be unique among simultaneously existing objects.
(CPython uses the object's memory address.)
>>> 
```
#### 可调用 ( callable() )
可以调用表示潜在行为（函数和方法）的对象。可以用 callable() 函数测试对象的可调用性
```python
>>> print(callable.__doc__)
Return whether the object is callable (i.e., some kind of function).
Note that classes are callable, as are instances of classes with a
__call__() method.

>>> callable('a list')
False
>>> callable('dir') 
False
>>> callable('str')
False

>>> callable(dir) #注意dir和上面‘dir’的区别，导致不一样的结果
True
>>> callable(str)
True
>>> 
```
#### 实例 (instance)
在 type() 函数提供对象的类型时，还可以使用 isinstance() 函数测试对象，以确定它是否是某个特定类型或定制类的实例：
```python
>>> print(isinstance.__doc__)
Return whether an object is an instance of a class or of a subclass thereof.
A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
or ...`` etc.

>>> isinstance(42, str)
False
>>> isinstance('python', str)
True
>>> 
```
#### 子类(ubclass)
在类这一级别，可以根据一个类来定义另一个类，同样地，这个新类会按照层次化的方式继承属性。Python 甚至支持多重继承，多重继承意味着可以用多个父类来定义一个类，这个新类继承了多个父类。 issubclass() 函数使我们可以查看一个类是不是继承了另一个类：

```python
>>> print issubclass.__doc__
issubclass(C, B) -> Boolean
Return whether class C is a subclass (i.e., a derived class) of class B.
>>> class SuperHero(Person):   # SuperHero inherits from Person...
...     def intro(self):       # but with a new SuperHero intro
...         """Return an introduction."""
...         return "Hello, I'm SuperHero %s and I'm %s." % (self.name, self.age)
...
>>> issubclass(SuperHero, Person)
1
>>> issubclass(Person, SuperHero)
0
```




