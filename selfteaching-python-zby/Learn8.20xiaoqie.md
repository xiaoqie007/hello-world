
假设有一组字符串，你想要根据各字符串不同字母的数量对其进行排序：
```python
>>> strings = ['foo', 'card', 'bar', 'aaaa', 'abab']

>>> strings.sort(key= lambda x: len(set(list(x))))
>>> strings
['aaaa', 'foo', 'abab', 'bar', 'card']

>>> strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
>>> strings.sort()
>>> strings
['aaaa', 'abab', 'bar', 'card', 'foo']


>>> list('aaaa')
['a', 'a', 'a', 'a']
>>> set(list('aaaa'))
{'a'}
>>> set(list('foo'))
{'f', 'o'}
>>> set(list('bar'))
{'r', 'b', 'a'}
>>> 
```

- **笔记：lambda函数之所以会被称为匿名函数，与def声明的函数不同，原因之一就是这种函数对象本身是没有提供名称name属性。**


### 柯里化：部分参数应用

柯里化（currying）是一个有趣的计算机科学术语，它指的是通过“部分参数应用”（partial argument application）从现有函数派生出新函数的技术。例如，假设我们有一个执行两数相加的简单函数：

```python
>>> def add_numbers(x, y):
	return x + y

#通过这个函数，我们可以派生出一个新的只有一个参数的函数——add_five，它用于对其参数加5：
>>> add_five = lambda y: add_number(5, y)
>>> add_five
<function <lambda> at 0x10b0c21e0>


#add_numbers的第二个参数称为“柯里化的”（curried）。这里没什么特别花哨的东西，因为我们其实就只是定义了一个可以调用现有函数的新函数而已。内置的functools模块可以用partial函数将此过程简化：
>>> from functools import partial
>>> add_five = partial(add_numbers, 5)
>>> add_five
functools.partial(<function add_numbers at 0x10e03bae8>, 5)
>>> 

#### 生成器

能以一种一致的方式对序列进行迭代（比如列表中的对象或文件中的行）是Python的一个重要特点。这是通过一种叫做迭代器协议（iterator protocol，它是一种使对象可迭代的通用方式）的方式实现的，一个原生的使对象可迭代的方法。比如说，对字典进行迭代可以得到其所有的键：
```python
>>> some_dict = {'a': 1, 'b': 2, 'c': 3}
>>> for key in some_dict:
	print(key)

	
a
b
c

#当你编写for key in some_dict时，Python解释器首先会尝试从some_dict创建一个迭代器：
>>> dict_iterator = iter(some_dict)
>>> dict_iterator
<dict_keyiterator object at 0x10e045688>

#迭代器是一种特殊对象，它可以在诸如for循环之类的上下文中向Python解释器输送对象。大部分能接受列表之类的对象的方法也都可以接受任何可迭代对象。比如min、max、sum等内置方法以及list、tuple等类型构造器：
>>> list(dict_iterator)
['a', 'b', 'c']

#生成器（generator）是构造新的可迭代对象的一种简单方式。一般的函数执行之后只会返回单个值，而生成器则是以延迟的方式返回一个值序列，即每返回一个值之后暂停，直到下一个值被请求时再继续。要创建一个生成器，只需将函数中的return替换为yeild即可：

>>> def squares(n= 10):
	print('Generating squares from 1 to {0}'. format(n **2))
	for i in range(1, n + 1):
		yield i ** 2

#调用该生成器时，没有任何代码会被立即执行：
>>> gen= squares()
>>> gen
<generator object squares at 0x10e08b2a0>

#直到你从该生成器中请求元素时，它才会开始执行其代码：
>>> for  x in gen:
	print(x, end= ' ')

	
Generating squares from 1 to 100
1 4 9 16 25 36 49 64 81 100 
```

- 生成器表达式
另一种更简洁的构造生成器的方法是使用生成器表达式（generator expression）。这是一种类似于列表、字典、集合推导式的生成器。其创建方式为，把列表推导式两端的方括号改成圆括号：
```python
>>> gen = (x ** 2 for x in range(100))
>>> gen
<generator object <genexpr> at 0x10e0364f8>
>>> for  x in gen:
	print(x, end= ' ')

	
0 1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361 400 441 484 529 576 625 676 729 784 841 900 961 1024 1089 1156 1225 1296 1369 1444 1521 1600 1681 1764 1849 1936 2025 2116 2209 2304 2401 2500 2601 2704 2809 2916 3025 3136 3249 3364 3481 3600 3721 3844 3969 4096 4225 4356 4489 4624 4761 4900 5041 5184 5329 5476 5625 5776 5929 6084 6241 6400 6561 6724 6889 7056 7225 7396 7569 7744 7921 8100 8281 8464 8649 8836 9025 9216 9409 9604 9801 

#它跟下面这个冗长得多的生成器是完全等价的：
>>> def _make_gen():
	for x in range(100):
		yield x ** 2

		
>>> gen = _make_gen()
>>> gen
<generator object _make_gen at 0x10e08b318>
>>> for  x in gen:
	print(x, end= ' ')

	
0 1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361 400 441 484 529 576 625 676 729 784 841 900 961 1024 1089 1156 1225 1296 1369 1444 1521 1600 1681 1764 1849 1936 2025 2116 2209 2304 2401 2500 2601 2704 2809 2916 3025 3136 3249 3364 3481 3600 3721 3844 3969 4096 4225 4356 4489 4624 4761 4900 5041 5184 5329 5476 5625 5776 5929 6084 6241 6400 6561 6724 6889 7056 7225 7396 7569 7744 7921 8100 8281 8464 8649 8836 9025 9216 9409 9604 9801 

#生成器表达式也可以取代列表推导式，作为函数参数：
>>> sum(x ** 2 for x in range(100))
328350
>>> dict((i, i**2) for i in range(5))
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

#### itertools模块
标准库itertools模块中有一组用于许多常见数据算法的生成器。例如，groupby可以接受任何序列和一个函数。它根据函数的返回值对序列中的连续元素进行分组。下面是一个例子：
```python
>>> import itertools
	
>>> first_letter = lambda x: x[0]
	
>>> names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']

>>> for letter, names in itertools.groupby(names, first_letter):
	print(letter, list(names))

	
A ['Alan', 'Adam']
W ['Wes', 'Will']
A ['Albert']
S ['Steven']
>>> 
```


- **一些有用的itertools函数**

|函数|说明|
| :---:| :---:|
| combinations(iterable, k)| 生成一个由iterable中所有可能的k元素元组组成的序列，不考虑顺序（参考另外一个函数 combinations_with_replacement）|
|permutations(iterable,k)|生成一个由iterable中所有可能的k元元组组成的序列，考虑顺序|
|groupby(iterable[, keyfunc])|为每个唯一键生成一个（key, sub-iterator）|
|product(*iterables,repeat= 1)|生成输入的iterable的笛卡尔积，结果为元组，类似于嵌套for循环|

### 错误和异常处理

优雅地处理Python的错误和异常是构建健壮程序的重要部分。在数据分析中，许多函数函数只用于部分输入。例如，Python的float函数可以将字符串转换成浮点数，但输入有误时，有ValueError错误：
```python
>>> def add_int(x):
	try:
	    return x ** 2
	except:
	    return x
	else:
	    print('Succeeded')
	finally:
	    print('Done!')

	
>>> add_int('so')
	
Done!
'so'
>>> add_int(7)
	
Done!
49
```
### IPython的异常

如果是在%run一个脚本或一条语句时抛出异常，IPython默认会打印完整的调用栈（traceback），在栈的每个点都会有几行上下文：

```python
In [10]: %run examples/ipython_bug.py
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
/home/wesm/code/pydata-book/examples/ipython_bug.py in <module>()
     13     throws_an_exception()
     14
---> 15 calling_things()

/home/wesm/code/pydata-book/examples/ipython_bug.py in calling_things()
     11 def calling_things():
     12     works_fine()
---> 13     throws_an_exception()
     14
     15 calling_things()

/home/wesm/code/pydata-book/examples/ipython_bug.py in throws_an_exception()
      7     a = 5
      8     b = 6
----> 9     assert(a + b == 10)
     10
     11 def calling_things():

AssertionError:
```
自身就带有文本是相对于Python标准解释器的极大优点。你可以用魔术命令%xmode，从Plain（与Python标准解释器相同）到Verbose（带有函数的参数值）控制文本显示的数量。后面可以看到，发生错误之后，（用%debug或%pdb magics）可以进入stack进行事后调试。

### 3.3 文件和操作系统
r 只读模式
w 只写模式， 创建新文件（删除同名的任何文件）
a 附加到现有文件（如果文件不存在则创建一个）
r+ 读写模式
b 附加说明某模式用于二进制文件，即‘rb’或‘wb’
U 通用换行模式。单独使用‘U’或附加到其他读模式（如‘rU’）



```python
with open('hsye.txt') as f:
    lines = f.readlines()
```
一些常见的文件方法：
read([size]):以字符串形式返回文件数据， 可选的size用于说明读取的字节数
readlines([size])将文件返回为行列表，可选参数size
write(str) 将字符串写入文件
close() 关闭句柄
flush() 清空内部I/O缓存区， 并将数据行写回磁盘
seek(pos) 移动到指定的文件位置（整数）
tell() 以整数形式返回当前文件位置
closed 如果文件已关闭，则为True

#### 文件的字节和Unicode

Python文件的默认操作是“文本模式”，也就是说，你需要处理Python的字符串（即Unicode）。它与“二进制模式”相对，文件模式加一个b。

···python
with open(path, 'rb') as f:
   .....:     data = f.read(10)

In [233]: data
Out[233]: b'Sue\xc3\xb1a el '
···
注意，不要在二进制模式中使用seek。如果文件位置位于定义Unicode字符的字节的中间位置，读取后面会产生错误：
如果你经常要对非ASCII字符文本进行数据分析，通晓Python的Unicode功能是非常重要的。更多内容，参阅Python官方文档。
