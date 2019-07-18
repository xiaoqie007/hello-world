
#### 递归
- 斐波那契
```python
def fib(n):
    """
    This is Fibonacci by Recursion.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) +fib(n-2)

if __name__ == "__main__":
    f = fib(10)
    print(f)
```
- 解析步骤

**fib(3)**

**fib(3-1)** + fib(3-2)

**fib(2-1) + fib(2-2)** +fib(3-2)

**1+ 0+ 1, >>>fib(3)=2**

```python
“”“
the better Fibonacci
”“”
meno = {0:0, 1:1} #初始化

def fib(n):
    if not n in meno:
        meno[n] = fib(n-1) + fib(n-2)
    return meno[n]
if __name__ == "__main__":
    f = fib(10)
    print(f)
```

#### 几个特殊函数  ---- (函数式编程)

如果以前没有听过，等你开始进入编程界，也会经常听人说“函数式编程”、“面向对象编程”、“指令式编程”等属于。它们是什么呢？这个话题要从“编程范式”讲起。（以下内容源自维基百科）

编程范型或编程范式（英语：Programming paradigm），（范即模范之意，范式即模式、方法），是一类典型的编程风格，是指从事软件工程的一类典型的风格（可以对照方法学）。如：函数式编程、程序编程、面向对象编程、指令式编程等等为不同的编程范型。

编程范型提供了（同时决定了）程序员对程序执行的看法。例如，在面向对象编程中，程序员认为程序是一系列相互作用的对象，而在函数式编程中一个程序会被看作是一个无状态的函数计算的串行。

正如软件工程中不同的群体会提倡不同的“方法学”一样，不同的编程语言也会提倡不同的“编程范型”。一些语言是专门为某个特定的范型设计的（如Smalltalk和Java支持面向对象编程，而Haskell和Scheme则支持函数式编程），同时还有另一些语言支持多种范型（如Ruby、Common Lisp、Python和Oz）。

编程范型和编程语言之间的关系可能十分复杂，由于一个编程语言可以支持多种范型。例如，C++设计时，支持过程化编程、面向对象编程以及泛型编程。然而，设计师和程序员们要考虑如何使用这些范型元素来构建一个程序。一个人可以用C++写出一个完全过程化的程序，另一个人也可以用C++写出一个纯粹的面向对象程序，甚至还有人可以写出杂揉了两种范型的程序。


正如前面引文中所说的，python是支持多种范型的语言，可以进行所谓函数式编程，其突出体现在有这么几个函数：

**filter、map、reduce、lambda、yield**

有了它们，最大的好处是程序更简洁；没有它们，程序也可以用别的方式实现，只不过麻烦一些罢了。所以，还是能用则用之吧。更何况，恰当地使用这几个函数，能让别人感觉你更牛X。


### - **lambda**

```python
>>> def add(x): #add(函数)
	x += 3
	return x
>>> add(3)
6

>>> lam = lambda x: x+ 3 #用lambda这个函数替代add(x)
>>> lam(3)
6

>>> g = lambda x, y:x+y #x+y,并返回结果
>>> g(3,4)
7

>>> (lambda x: x**2)(3) #返回3的平方
9
>>> 
```
通过上面例子，总结一下lambda函数的使用方法：

- 在lambda后面直接跟变量
- 变量后面是冒号
- 冒号后面是表达式，表达式计算结果就是本函数的返回值

简明扼要，用一个式子表示:
>**lambda arg1, arg2, ...argN : expression using arguments**

要特别提醒看官：虽然lambda 函数可以接收任意多个参数 (包括可选参数) 并且返回单个表达式的值，但是**lambda 函数不能包含命令，包含的表达式不能超过一个。不要试图向 lambda 函数中塞入太多的东西；如果你需要更复杂的东西，应该定义一个普通函数，然后想让它多长就多长。**
```python
>>> lamb = [lambda x:x, lambda x:x**2,lambda x:x**3,lambda x:x**4]
>>> for i in lamb:
	print(i(3), end = ' ')
3 9 27 81 
>>> 
```


### - **map**

map(func,seq) ：func是一个函数，seq是一个序列对象
在执行的时候，序列对象中的每个元素，按照从左到右的顺序，依次被取出来，并塞入到func那个函数里面，并将func的返回值依次存到一个list中

- 理解要点：
  - 对iterable中的每个元素，依次应用function的方法（函数）（这本质上就是一-个for循环）。
  - 将所有结果返回一个list。
  - 如果参数很多，则对那些参数并行执行function。
```python
>>> lst1 = [1,2,3,4,5]
>>> lst2 = [6,7,8,9,0]
>>> lst3 = [7,8,9,2,1]
>>> map(lambda x,y,z: x+y+z, lst1,lst2,lst3)
[14, 17, 20, 15, 6]
```

### - **reduce**   py3需(from functools import reduce)
```python
>>> from functools import reduce
>>> reduce(lambda x, y: x+y, [1,2,3,4,5])
15

>>> lst1 = [1,2,3,4,5,6,7,8,9]
>>> lst2 = [9,8,7,6,5,4,3,2,1]
>>> map(lambda x, y:x+y, lst1, lst2)
<map object at 0x10619e2e8>
>>> list(map(lambda x, y:x+y, lst1, lst2))
[10, 10, 10, 10, 10, 10, 10, 10, 10]
>>> 
```
  - 以上例子对比说明：**map是上下运算，reduce是横着**逐个元素进行运算。
     

for普世的，reduce是简洁的。


为了锻炼思维，看这么一个问题，有两个list，a = [3,9,8,5,2],b=[1,4,9,2,6],计算：a[0]b[0]+a[1]b[1]+...的结果。



### - **filter**
- filter的中文含义是“过滤器”
- filter(function, iterable)
```python
>>> numbers = range(-5,5)
>>> numbers
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

>>> filter(lambda x: x>0, numbers) 
[1, 2, 3, 4]

>>> [x for x in numbers if x>0]     #与上面那句等效
[1, 2, 3, 4]

???
 >>> filter(lambda c: c!='i', 'qiwsir')  #能不能对应上面文档说明那句话呢？
'qwsr'      #“If iterable is a string or a tuple, the result also has that type;”

???
>>> ss = filter(lambda c: c != 'i', 'qiwsir')
>>> ss
<filter object at 0x1046b5fd0>
>>> str(ss)
'<filter object at 0x1046b5fd0>'
>>> list(ss)
['q', 'w', 's', 'r']

```




