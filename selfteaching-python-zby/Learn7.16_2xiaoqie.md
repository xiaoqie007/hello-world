
#### **return**
- 返回值
- 有的函数，没有return，一样执行完毕，就算也干了某些活儿吧。事实上，不是没有返回值，也有，只不过是None。比如这样一个函数：
```python
>>> def my_fun():
...     print "I am doing somthin."
>>> a = my_fun()
I am doing somthin.
>>> print a
None
这就是只干活儿，没有return的函数，事实上返回的是一个None。这种模样的函数，通常不用上述方式调用，而采用下面的方式，因为他们返回的是None，似乎这个返回值利用价值不高，于是就不用找一个变量来接受返回值了。
>>> my_fun()
I am doing somthin.
```

- 类似循环中的break的作用。
```
>>> def my_fun():
...     print "I am coding."
...     return
...     print "I finished."
... 
>>> my_fun()
I am coding.
```
看出玄机了吗？在函数中，本来有两个print语句，但是中间插入了一个return，仅仅是一个return。当执行函数的时候，只执行了第一个print语句，第二个并没有执行。这是因为第一个之后，遇到了return，它告诉函数要返回，即中断函数体内的流程，离开这个函数。结果第二个print就没有被执行。所以，return在这里就有了一个作用，结束正在执行的函数，有点类似循环中的break的作用。

#### 函数文档
```
'''  ........     '''
用 **my_fun.__doc__** 进行调用
```
先参考一段来自微软网站的比较高度抽象，而且意义涵盖深远的说明。我摘抄过来，看官读一读，是否理解，虽然是针对VB而言的，一样有启发。

**参数和变量之间的差异 (Visual Basic)**(了解)

多数情况下，过程必须包含有关调用环境的一些信息。执行重复或共享任务的过程对每次调用使用不同的信息。此信息包含每次调用过程时传递给它的变量、常量和表达式。

若要将此信息传递给过程，过程先要定义一个形参，然后调用代码将一个实参传递给所定义的形参。 您可以将形参当作一个停车位，而将实参当作一辆汽车。 就像一个停车位可以在不同时间停放不同的汽车一样，调用代码在每次调用过程时可以将不同的实参传递给同一个形参。

形参表示一个值，过程希望您在调用它时传递该值。

当您定义 Function 或 Sub 过程时，需要在紧跟过程名称的括号内指定形参列表。对于每个形参，您可以指定名称、数据类型和传入机制（ByVal (Visual Basic) 或 ByRef (Visual Basic)）。您还可以指示某个形参是可选的。这意味着调用代码不必传递它的值。

每个形参的名称均可作为过程内的局部变量。形参名称的使用方法与其他任何变量的使用方法相同。

实参表示在您调用过程时传递给过程形参的值。调用代码在调用过程时提供参数。

调用 Function 或 Sub 过程时，需要在紧跟过程名称的括号内包括实参列表。每个实参均与此列表中位于相同位置的那个形参相对应。

与形参定义不同，实参没有名称。每个实参就是一个表达式，它包含零或多个变量、常数和文本。求值的表达式的数据类型通常应与为相应形参定义的数据类型相匹配，并且在任何情况下，该表达式值都必须可转换为此形参类型。

```python
>>> def add(x):     #x是参数，准确说是形参
...     a = 10      #a是变量
...     return a+x  #x就是那个形参作为变量，其本质是要传递赋给这个函数的值
... 
>>> x = 3           #x是变量，只不过在函数之外
>>> add(x)          #这里的x是参数，但是它由前面的变量x传递对象3
13
>>> add(3)          #把上面的过程合并了
13
```
```
>>> def foo(lst):
...     lst.append(99)
...     return lst
... 
>>> x = [1, 3, 5]
>>> y = foo(x)
>>> y
[1, 3, 5, 99]
>>> x
[1, 3, 5, 99]
>>> id(x)
3075464588L
>>> id(y)
3075464588L
```

**全局变量和局部变量**

```python
>>> x= 2
>>> def funcx():
	x = 9
	print('this x is in the funcx:-->', x)

	
>>> funcx()
this x is in the funcx:--> 9
>>> print("*"*20)
********************
>>> print('this x is out of funcx:-->', x)
this x is out of funcx:--> 2
>>> 
```
> 特别要关注的是，前一个x输出的是函数内部的变量x;后一个x输出的是函数外面的变量x

慎用：(global x 的意思是在声明x是全局变量，也就是说这个x跟函数外面的那个x同一个)
```
x = 2
def funcx():
    global x    #跟上面函数的不同之处
    x = 9
    print "this x is in the funcx:-->",x
funcx()
print "--------------------------"
print "this x is out of funcx:-->",x

this x is in the funcx:--> 9
--------------------------
this x is out of funcx:--> 9
```

- **命名空间**

- **参数收集**(用args这种形式的参数接收多个值之外，还可以用*kargs的形式接收数值)

```python
>>> def func(x, *arg):
	print(x) #输出参数x的值
	result = x
	print(arg) #输出通过*arg方式的值
	for i in arg:
		result += i
	return result

>>> print(func(1,2,3,4,5,6,7,8,9)) #赋给函数的参数个数不仅仅是两个
1
(2, 3, 4, 5, 6, 7, 8, 9)
45
>>> 
```
- 值1传给了参数x
- 值2,3,4,5,6.7.8.9被塞入一个tuple里面，传给了arg

**在各类编程语言中，常常会遇到以foo，bar，foobar等之类的命名**

- **kargs 接收数值
```python
>>> def foo(**kargs):
	print(kargs)

	
>>> foo(a= 1, b= 2, c= 3)
{'a': 1, 'b': 2, 'c': 3}
>>> 
```
- 如果用**kargs的形式收集值，会得到dict类型的数据，但是，需要在传值的时候说明“键”和“值”，因为在字典中是以键值对形式出现的。


#### ***args** 和 ***kargs结合** 四个结合的情况
```python
>>> def foo(x, y, z, *args, **kargs):
	print(x)
	print(y)
	print(z)
	print(args)
	print(kargs)
	
>>> foo('zhaozhao', '12', 'hello')
zhaozhao
12
hello
()
{}

>>> foo(1,2,3,4,5,6,7)
1
2
3
(4, 5, 6, 7)
{}

>>> foo(1,2,3,4,5,6,7, name= 'qiwsir')
1
2
3
(4, 5, 6, 7)
{'name': 'qiwsir'}
>>> 
```


#### 另外一种传值方式
```
>>> def add(x, y):
	return (x+y)

>>> add(2,3)
5
>>> bars = (2,3)
>>> add(*bars)
5
先把要传的值放到元组中，赋值给一个变量bars，然后用add(*bars)的方式，把值传到函数内。这有点像前面收集参数的逆过程。注意的是，元组中元素的个数，要跟函数所要求的变量个数一致。
```
### 复习
-python中函数的参数通过赋值的方式来传递引用对象。下面总结通过总结常见的函数参数定义方式，来理解参数传递的流程:
- def foo(p1,p2,p3,...)
```
>>> def foo(z,x,y):
	print('z+x+y=%d'%(x+y+z))
	
>>> foo(1,2,3)
z+x+y=6
>>> 
```
- def foo(p1=value1,p2=value2,...)
```python
>>> foo(z=1,x=2,y=3)
z+x+y=6
>>> def foo(z=1,x=2,y=3):
	print('z+x+y=%d'%(x+y+z))
	
>>> foo(z=2,x=4,y=6)
z+x+y=12
>>> 
```

- def foo(*args)
>这种方式适合于不确定参数个数的时候，在参数args前面加一个*，注意，仅一个哟。

- def foo(**args)
>这种方式跟上面的区别在于，必须接收类似arg=val形式的。

```
>>> def foo(**args):    #这种方式接收，以dictionary的形式接收数据对象
...     print (args)
...

>>> foo(1,2,3)          #这样就报错了
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() takes exactly 0 arguments (3 given)

>>> foo(a=1,b=2,c=3)    #这样就可以了，因为有了键值对
{'a': 1, 'c': 3, 'b': 2}
```

