**ipython和jupyter中**

？
- 在变量前后使用问号？，可以显示对象的信息：
- 作为对象的自省。如果对象是一个函数或实例方法，定义过的文档字符串，也会显示出信息

？？
- 会显示函数的源码


?还有一个用途，就是像Unix或Windows命令行一样搜索IPython的命名空间。字符与通配符结合可以匹配所有的名字。例如，我们可以获得所有包含load的顶级NumPy命名空间：
np.*load*?

```python
In [45]: np.*load*?                
np.__loader__
np.load
np.loads
np.loadtxt
np.pkgload
```


ipython

**%run命令**
```python
#   %run ipython_script_test.py
```

```python
In [48]: import sys               
In [49]: sys.argv                
Out[49]: ['/Users/liwei/anaconda3/bin/ipython'] 
```
>如果一个Python脚本需要命令行参数（在sys.argv中查找），可以在文件路径之后传递，就像在命令行上运行一样。

> **笔记：如果想让一个脚本访问IPython已经定义过的变量，可以使用%run -i**


### 在Jupyter notebook中:

你也可以使用 **%load** ，它将脚本导入到一个代码格中：

### 中断运行的代码
代码运行时按Ctrl-C，无论是%run或长时间运行命令，都会导致KeyboardInterrupt

从剪贴板执行程序
```python
%paste # 直接粘贴
%cpaste
#会给出一条提示，使用%cpaste，你可以粘贴任意多的代码再运行。你可能想在运行前，先看看代码。如果粘贴了错误的代码，可以用Ctrl-C中断。
```

IPython的文档可以在shell中打开，我建议你用%quickref或%magic学习下所有特殊命令

集成Matplotlib

在IPython shell中，运行%matplotlib可以进行设置，可以创建多个绘图窗口，而不会干扰控制台session：

```python
In [26]: %matplotlib
Using matplotlib backend: Qt4Agg
```

在JUpyter中，命令有所不同（图2-6）：
```python
%matplotlib inline
```

动态引用，强类型

