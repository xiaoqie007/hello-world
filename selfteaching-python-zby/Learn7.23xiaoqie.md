
“模块自信”的本质是：**开放**

**模块是程序**

**包或者库**
- 顾名思义，包或者库，应该是比“模块”大的。也的确如此，一般来讲，一个“包”里面会有多个模块，当然，“库”是一个更大的概念了，比如Python标准库中的每个库，都可以看成有好多个包，每个包，都有若干个模块。或许这个概念不是很明确，这么理解不会耽误你使用。

- 对于一个包，因为它是由多个模块组成，也就是说是多个.py的文件，那么这个所谓“包”也就是我们熟悉的一个目录罢了。现在就需要解决如何引用某个目录中的模块问题了。解决方法就是在该目录中放一个__init__.py文件。__init__.py是一个空文件，将它放在某个目录中，就可以将该目录中的其它.py文件作为模块被引用。

**帮助、文档和源码**
>dir()
>help()

pprint.__doc__是查看整个类的文档，还知道整个文档是写在什么地方的吗？
```python
>>> print(pprint.__file__)
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/pprint.py
#告诉我们这个模块的位置
```
>**请读者在闲暇时间，阅读以下源码。事实证明，这种标准库中的源码是质量最好的。**



**sys.exit()**

```python
>>> for i in range(10):
	if i == 7:
		sys.exit(print("I wet out at here."))
	else:
		print(i)

		
0
1
2
3
4
5
6
I wet out at here.
>>> for i in range(10):
	if i == 7:
		sys.exit(0)
	else:
		print(i)

		
0
1
2
3
4
5
6
```

**sys.path**

**sys.path** 已经不陌生了，前面用过。它可以查找模块所在的目录，以列表的形式显示出来。如果用append()方法，就能够向这个列表增加新的模块目录

```python
>>> 
>>>import pprint
>>>pprint.pprint(sys.path)
['',
 '/Users/liwei/Documents',
 '/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip',
 '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7',
 '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload',
 '/Users/liwei/Library/Python/3.7/lib/python/site-packages',
 '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages']

```
**sys.stdin, sys.stdout, sys.stderr**

这三个放到一起，因为他们的变量都是类文件流对象，分别表示标准UNIX概念中的标准输入、标准输出和标准错误。与python功能对照，sys.stdin获得输入（用raw_input()输入的通过它获得，python3.x中是imput()），sys.stdout负责输出了。

>流是程序输入或输出的一个连续的字节序列，设备(例如鼠标、键盘、磁盘、屏幕、调制解调器和打印机)的输入和输出都是用流来处理的。程序在任何时候都可以使用它们。一般来讲，stdin（输入）并不一定来自键盘，stdout（输出）也并不一定显示在屏幕上，它们都可以重定向到磁盘文件或其它设备上。

还记得print()吧，在这个学习过程中，用的很多。它的本质就是sys.stdout.write(object + '\n')。

```python
>>> for i in range(3):
	print(i)
	
0
1
2
>>> import sys
>>> for i in range(3):
	sys.stdout.write(str(i) + '\n')
	
0
2
1
2
2
2
>>> for i in range(3):
	sys.stdout.write(str(i) + '\n')
	
0
2
1
2
2
2
>>> for i in range(3):
	sys.stdout.write(str(i))
	
01
11
21
>>> 
```
```python
>>> f = open("stdout.md", "w")
>>> sys.stdout = f
>>> print "Learn Python: From Beginner to Master"
>>> f.close()
```
- sys.stdout = f之后，就意味着将输出目的地转到了打开（建立）的文件中，如果使用print()，即将内容输出到这个文件中，在控制台并无显现

**copy**
```python
>>> import copy
>>> copy.__all__
['Error', 'copy', 'deepcopy']
>>> 
```
```python
import copy

class MyCopy(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

foo = MyCopy(7)

a = ["foo", foo]
b = a[:]
c = list(a)
d = copy.copy(a)
e = copy.deepcopy(a)

a.append("abc")
foo.value = 17

print("original: %r\n slice: %r\n list(): %r\n copy(): %r\n deepcopy(): %r\n" %(a,b,c,d,e))
```
```python
original: ['foo', 17, 'abc']
 slice: ['foo', 17]
 list(): ['foo', 17]
 copy(): ['foo', 17]
 deepcopy(): ['foo', 7]

>>> 
```

**OS**
os模块提供了访问操作系统服务的功能，它所包含的内容比较多。

操作文件：重命名rename 、删除文件remove
```
>>> import os
>>> os.rename("22201.py", "newtemp.py")
```

```python
>>> help(os.rename)
Help on built-in function rename in module posix:

rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
    Rename a file or directory.
    
    If either src_dir_fd or dst_dir_fd is not None, it should be a file
      descriptor open to a directory, and the respective path string (src or dst)
      should be relative; the path will then be relative to that directory.
    src_dir_fd and dst_dir_fd, may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError.

>>> 
```
```python
>>> help(os.remove)
Help on built-in function remove in module posix:

remove(path, *, dir_fd=None)
    Remove a file (same as unlink()).
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.

```
注意帮助中一句话Remove a file，os.remove()就是用来删除文件的


操作目录
os.listdir：显示目录中的文件
```python
>>> os.listdir("/home/qw/Documents/VBS/StarterLearningPython/2code/rd")
['b.py', 'c.py']
>>> files = os.listdir("/home/qw/Documents/VBS/StarterLearningPython/2code/rd")
>>> for f in files:
...     print f
... 
b.py
c.py
```



- **os.getcwd, os.chdir：当前工作目录，改变当前工作目录**

- **os.pardir:获得父类目录**


```python
>>> import os
>>> cwd = os.getcwd() #获得当前工作目录
>>> print(cwd)
/Users/liwei/Documents
>>> os.chdir(os.pardir) #返回上一级工作目录
>>> cwd = os.getcwd() #获得当前工作目录
>>> print(cwd)
/Users/liwei
>>> os.chdir('Documents') #到“Documents”工作目录下
>>> cwd = os.getcwd() #获得当前工作目录
>>> print(cwd)
/Users/liwei/Documents
>>> os.pardir #os.pardir的功能是获得父级目录，相当于..
'..'
>>> 
```

- **os.makedirs, os.removedirs：创建和删除目录**
```python
>>> dir = os.getcwd()
>>> dir
'/Users/liwei/Documents'
>>> os.removedirs(dir)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    os.removedirs(dir)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/os.py", line 239, in removedirs
    rmdir(name)
PermissionError: [Errno 13] Permission denied: '/Users/liwei/Documents'
>>> dir = os.getcwd()
>>> dir
'/Users/liwei/Documents'
>>> os.makedirs('newrd')
>>> os.chdir('newrd')
>>> os.getcwd()
'/Users/liwei/Documents/newrd'
>>> os.listdir(os.getcwd())
[]
>>> newdir = os.getcwd()
>>> os.removedirs(newdir)
>>> os.getcwd()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    os.getcwd()
FileNotFoundError: [Errno 2] No such file or directory
>>> os.chdir('Documents')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    os.chdir('Documents')
FileNotFoundError: [Errno 2] No such file or directory: 'Documents'
>>> os.chdir(os.pardir) #回到父级目录
>>> os.getcwd()
'/Users/liwei/Documents'
>>> 
```
补充一点，前面说的如果目录不空，就不能用os.removedirs()删除。但是，可以用模块shutil的retree方法。
```python
>>> os.getcwd()
'/home/qw/Documents/VBS/StarterLearningPython/2code'
>>> os.chdir("rd")
>>> now = os.getcwd()
>>> now
'/home/qw/Documents/VBS/StarterLearningPython/2code/rd'
>>> os.listdir(now)
['b.py', 'c.py']
>>> import shutil
>>> shutil.rmtree(now)
>>> os.getcwd()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: [Errno 2] No such file or directory
```


对于os.makedirs()还有这样的特点：
```python
>>> os.getcwd()
'/home/qw/Documents/VBS/StarterLearningPython/2code'
>>> d0 = os.getcwd()
>>> d1 = d0+"/ndir1/ndir2/ndir3"    #这是想建立的目录，但是中间的ndir1,ndir2也都不存在。
>>> d1
'/home/qw/Documents/VBS/StarterLearningPython/2code/ndir1/ndir2/ndir3'
>>> os.makedirs(d1)
>>> os.chdir(d1)
>>> os.getcwd()
'/home/qw/Documents/VBS/StarterLearningPython/2code/ndir1/ndir2/ndir3'
```
**中间不存在的目录也被建立起来，直到做右边的目录为止。与os.makedirs()类似的还有os.mkdir()，不过，os.mkdir()没有上面这个功能，它只能一层一层地建目录。

os.removedirs()和os.rmdir()也类似，区别也类似上面。**

**文件和目录属性**

os.stat()
```python
>>> os.getcwd()
'/Users/liwei/Documents'
>>> p = os.getcwd()
>>> p
'/Users/liwei/Documents'
>>> os.stat(p)
os.stat_result(st_mode=16832, st_ino=633989, st_dev=16777223, st_nlink=13, st_uid=501, st_gid=20, st_size=416, st_atime=1563854767, st_mtime=1563854655, st_ctime=1563854655)

>>> pf = p + '/代码进度.py'

>>> os.stat(pf)

os.stat_result(st_mode=33188, st_ino=4301706038, st_dev=16777223, st_nlink=1, st_uid=501, st_gid=20, st_size=1889, st_atime=1563859865, st_mtime=1551186806, st_ctime=1551192101)

>>> fi = os.stat(pf)

>>> mt = fi[8] #fi[8]就是st_mtime的值，它代表最后modified（修改）文件的时间。看结果：
>>> mt
1551186806

>>> import time
>>> time.ctime(mt)
'Tue Feb 26 21:13:26 2019'
>>> 


```python
#有了一个webbrowser模块。可以专门用来打开指定网页。
>>> import webbrowser
>>> webbrowser.open('http://www.google.com')
True
>>> webbrowser.open('http://www.baidu.com')
True
>>> 
```
