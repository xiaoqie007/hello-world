#### 日期和时间
Python内建的datetime模块提供了datetime、date和time类型。datetime类型结合了date和time，是最常使用的：

```python
from datetime import datetime, date, time

# - strftime 方法将datetime格式化字符串

# - strptime 可以将字符串转换成 datetime 对象
```

当你聚类或对时间序列进行分组，替换datetimes的time字段有时会很有用。例如，用0替换分和秒：

两个 datetime.datetime 对象的差会产生一个datetime.timedelta 类型。

```python

In [41]: dt2                                                                    
Out[41]: datetime.datetime(2011, 11, 15, 22, 30)

In [42]: dt                                                                     
Out[42]: datetime.datetime(2011, 10, 29, 20, 30, 21)

In [43]: delta = dt2- dt                                                        
In [44]: delta                                                                  
Out[44]: datetime.timedelta(days=17, seconds=7179)

In [45]: type(delta)                                                            
Out[45]: datetime.timedelta
```
### 控制流

if 、 elif 和else

```python
>>> sequence = [1, 2, None, 4, None, 5]
>>> total = 0
>>> for value in sequence:
	if value is None:
		continue
	total += value

	
>>> total
12
>>> for value in sequence:
	if value is None:
		break
	total += value

	
>>> total
15
>>> sequence = [1, 2, None, 4, None, 5]
>>> total = 0
>>> for value in sequence:
	if value is None:
		break
	total += value

	
>>> total
3
>>> 
```

While循环

while循环指定了条件和代码，当条件为False或用break退出循环，代码才会退出：

**Pass**

pass是Python中的非操作语句。代码块不需要任何动作时可以使用（作为未执行代码的占位符）；因为Python需要使用空白字符划定代码块，所以需要pass：


**range**

```python
range函数返回一个迭代器，它产生一个均匀分布的整数序列

range的三个参数是（起点，终点，步进）：

>>> seq = [1,2,3,4]
>>> for i in range(len(seq)):
	val = seq[i]

	
>>> val
4
>>> sum = 0
>>> for i in range(100000):
	if i % 3 == 0 or i % 5 == 0:
		sum += i

		
>>> sum
2333316668
```

三元表达式

Python中的三元表达式可以将if-else语句放到一行里。语法如下：

**value = true-expr if condition else false-expr**

true-expr或false-expr可以是任何Python代码。它和下面的代码效果相同：

```python
if condition:
    value = true-expr
else:
    value = false-expr
```

