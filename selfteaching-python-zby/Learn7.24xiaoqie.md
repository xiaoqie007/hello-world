
#### 标准库
**heapq**

- 堆（heap），是一种数据结构

> 堆（英语：heap)，是计算机科学中一类特殊的数据结构的统称。堆通常是一个可以被看做一棵树的数组对象。

- 堆的实现是通过构造二叉堆，也就是一种二叉树。

heapq模块
heapq中的heap是堆，q就是queue（队列）的缩写。此模块包括：
```python
>>> import heapq
>>> heapq.__all__
['heappush', 'heappop', 'heapify', 'heapreplace', 'merge', 'nlargest', 'nsmallest', 'heappushpop']
>>> 
```

heappush(heap, x)：将x压入对heap（这是一个列表）
```python
>>> help(heapq.heappush)
Help on built-in function heappush in module _heapq:

heappush(...)
    heappush(heap, item) -> None. Push item onto heap, maintaining the heap invariant.

>>> 
```

```
>>> import heapq
>>> heap = []
>>> heapq.heappush(heap, 3)
>>> heapq.heappush(heap, 5)
>>> heapq.heappush(heap, 7)
>>> heapq.heappush(heap, 0)
>>> heapq.heappush(heap, 4)
>>> heapq.heappush(heap, 8)
>>> heap
[0, 3, 7, 5, 4, 8]
```


**heappop(heap)：删除最小元素**
```
>>> heapq.heappop(heap)
0
>>> heap
[3, 4, 7, 5, 8]
>>> 
```
**heapify()：将列表转换为堆**
```python
>>> h1 = [2,4,6,8,9,0,1,5,3]
>>> heapq.heapify(h1)
>>> h1
[0, 3, 1, 4, 9, 6, 2, 5, 8]
>>> 
```
经过这样的操作，列表h1就变成了堆（注意观察堆的顺序，和列表不同），可以对h1（堆）使用heappop()或者heappush()等函数了。否则，不可。
```python
>>> heapq.heappop(h1)
0
>>> h1
[1, 3, 2, 4, 9, 6, 8, 5]
>>> heapq.heappush(h1, 19)
>>> h1
[1, 3, 2, 4, 9, 6, 8, 5, 19]
>>> heapq.heappush(h1, 9)
>>> h1
[1, 3, 2, 4, 9, 6, 8, 5, 19, 9]
>>> heapq.heappop(h1)
1
>>> h1
[2, 3, 6, 4, 9, 9, 8, 5, 19]
>>> 
```
```python
#不要认为堆里面只能放数字，之所以用数字，是因为对它的逻辑结构比较好理解。

>>> heapq.heappush(h1, 'q')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    heapq.heappush(h1, 'q')
TypeError: '<' not supported between instances of 'str' and 'int'
>>> h1
[2, 3, 6, 4, 9, 9, 8, 5, 19, 'q']
>>> heapq.heappush(h1, 'w')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    heapq.heappush(h1, 'w')
TypeError: '<' not supported between instances of 'str' and 'int'
>>> h1
[2, 3, 6, 4, 9, 9, 8, 5, 19, 'q', 'w']
>>> 
```

**heapreplace()**

>是heappop()和heappush()的联合，也就是删除一个，同时加入一个。
例如：
```python
>>> heapq.heapreplace(h1, 3.14)
2
>>> h1
[3, 3.14, 6, 4, 9, 9, 8, 5, 19, 'q', 'w']
>>> 
```
- 先简单罗列关于对的几个常用函数。那么堆在编程实践中的用途在哪方面呢？主要在排序上。**一提到排序，读者肯定想到的是sorted()或者列表中的sort()，不错，这两个都是常用的函数，而且在一般情况下已经足够使用了。如果再使用堆排序，相对上述方法应该有优势。**

- **堆排序的优势不仅更快，更重要的是有效地使用内存，当然，另外一个也不同忽视，就是简单易用。**比如前面操作的，删除数列中最小的值，就是在排序基础上进行的操作。

**deque模块** 在collections模块中

方法1:
```python
>>> lst = [1,2,3]
>>> lst.append(4) #lst右边加上一个数字
>>> lst
[1, 2, 3, 4] #如何在左边加上一个数字？
>>> nl = [7]
>>> nl.extend(lst)  #通过extend方法，将lst中的元素迭代到nl中
>>> nl
[7, 1, 2, 3, 4]
```

```python
help> list.extend
Help on method_descriptor in list:

list.extend = extend(self, iterable, /)
    Extend list by appending elements from the iterable.

```

方法二：

collections模块中东西很多，我们只用到deque。
将列表转化为deque。deque在汉语中有一个名字，叫做“双端队列”（double-ended queue）。

```python
>>> from collections import deque
>>> lst = [1,2,3,4]
>>> qlst = deque(lst)
>>> qlst.append(5)
>>> qlst
deque([1, 2, 3, 4, 5])

>>> qlst.appendleft(7)
>>> qlst
deque([7, 1, 2, 3, 4, 5])

>>> qlst.pop()
5
>>> qlst
deque([7, 1, 2, 3, 4])

>>> qlst.popleft()
7
>>> qlst
deque([1, 2, 3, 4])
>>> 
```

**rotate**

rotate()的功能是将[1, 2, 3, 4]的首位连起来，你就想象一个圆环，在上面有1,2,3,4几个数字。如果一开始正对着你的是1，依顺时针方向排列


```python
>>> qlst
deque([1, 2, 3, 4])
>>> qlst.rotate(3) #rotate(3)，表示每个数字按照顺时针方向前进三个位置
>>> qlst
deque([2, 3, 4, 1])
>>> qlst
deque([2, 3, 4, 1])
>>> qlst.rotate(1)
>>> 
>>> qlst
deque([1, 2, 3, 4])
>>> qlst.rotate(2)
>>> qlst
deque([3, 4, 1, 2])
>>> qlst.rotate(-1) #参数是负数，那么就逆时针转。
>>> qlst
deque([4, 1, 2, 3])
>>> 
```



#### 标准库(5)

**calendar**

calendar(year,w=2,l=1,c=6)

返回year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21 W+18+2 C。l是每星期行数。
```
>>>year = calendar.calendar(2019)
>>>print(year)
```

**isleap(year)**
- 判断是否为闰年，是则返回true，否则false
```python
>>> calendar.isleap(2019)
False
>>> calendar.isleap(2020)
True
```

**leapdays(y1,y2)**
返回在Y1，Y2两年之间的闰年总数，包括y1，但不包括y2，这有点如同序列的切片一样。
```python
>>> calendar.leapdays(2020, 2050)
8
>>> calendar.leapdays(2003, 2005)
1
>>> 
```

**month(year,month,w=2,l=1)**
返回year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。


**monthcalendar(year,month)**
返回一个列表，列表内的元素还是列表，这叫做嵌套列表。每个子列表代表一个星期，都是从星期一到星期日，如果没有本月的日期，则为0。
```python
>>> calendar.monthcalendar(2019, 7)
[[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31, 0, 0, 0, 0]]
```
**monthrange(year,month)**
```python
>>> print(calendar.monthrange(2019, 2))
(4, 28)
```
**weekday(year,month,day)**
>>> calendar.weekday(2019, 2, 28) #星期四
3
>>> 


**time**
time()

time模块是常用的。
```python
>>> import time
>>> time.time()
1563870235.756107

>>> time.localtime()
time.struct_time(tm_year=2019, tm_mon=7, tm_mday=23, tm_hour=16, tm_min=24, tm_sec=41, tm_wday=1, tm_yday=204, tm_isdst=0)

>>> t = time.localtime()
>>> t[0] #通过索引
2019

>>> time.localtime(100000)
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=2, tm_hour=11, tm_min=46, tm_sec=40, tm_wday=4, tm_yday=2, tm_isdst=0)
>>> 
```

**gmtime()**
```
>>> time.gmtime()
time.struct_time(tm_year=2019, tm_mon=7, tm_mday=23, tm_hour=8, tm_min=29, tm_sec=2, tm_wday=1, tm_yday=204, tm_isdst=0)
```
**asctime()**
```
>>> time.asctime()
'Tue Jul 23 16:29:21 2019'
>>> h = time.localtime(100000)
>>> time.asctime(h)
'Fri Jan  2 11:46:40 1970'
>>> 
```
- 注意，time.asctime()的参数必须是时间元组，类似上面那种。不是时间戳，通过time.time()得到的时间戳，也可以转化为上面形式：

**ctime()**
```
>>> time.ctime()
'Tue Jul 23 16:32:58 2019'
>>> 
```

>在前述函数中，通过localtime()、gmtime()得到的是时间元组，通过time()得到的是时间戳。有的函数如asctime()是以时间元组为参数，有的如ctime()是以时间戳为函数。这样做的目的是为了满足编程中多样化的需要。

**mktime()**

**strftime()**
- 将时间元组按照指定格式要求转化为字符串。如果不指定时间元组，就默认为localtime()值。我说复杂，是在于其format，需要用到下面的东西。


```python
|格式| 含义	|取值范围（格式）|
|--|  --|  --|

| %y| 去掉世纪的年份	| 00-99，如"15"|

%Y	完整的年份	如"2015"
%j	指定日期是一年中的第几天	001-366
%m	返回月份	01-12
%b	本地简化月份的名称	简写英文月份
%B	本地完整月份的名称	完整英文月份
%d	该月的第几日	如5月1日返回"01"
%H	该日的第几时（24小时制）	00-23
%l	该日的第几时（12小时制）	01-12
%M	分钟	00-59
%S	秒	00-59
%U	在该年中的第多少星期（以周日为一周起点）	00-53
%W	同上，只不过是以周一为起点	00-53
%w	一星期中的第几天	0-6
%Z	时区	在中国大陆测试，返回CST，即China Standard Time
%x	日期	日/月/年
%X	时间	时:分:秒
%c	详细日期时间	日/月/年 时:分:秒
%%	‘%’字符	‘%’字符
%p	上下午	AM or PM
```
```python
>>> time.strftime("%y, %m, %d")
'19, 07, 23'
>>> time.strftime("%y/ %m/ %d")
'19/ 07/ 23'
>>> 
```
- 分隔符可以自由指定。既然已经变成字符串了，就可以“随心所欲不逾矩”了。

**strptime()**

- strptime()的作用是将字符串转化为时间元组。请注意的是，其参数要指定两个，一个是时间字符串，另外一个是时间字符串所对应的格式，格式符号用上表中的。例如：

```python
>>> today = time.strftime("%y/%m/%d")
>>> today
'15/05/05'
>>> time.strptime(today, "%y/%m/%d")
time.struct_time(tm_year=2015, tm_mon=5, tm_mday=5, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=125, tm_isdst=-1)
```

#### datetime

- datetime模块中有几个类：

  - datetime.date：日期类，常用的属性有year/month/day
  - datetime.time：时间类，常用的有hour/minute/second/microsecond
  - datetime.datetime：日期时间类
  - datetime.timedelta：时间间隔，即两个时间点之间的时间长度
  - datetime.tzinfo：时区类


**timedelta类**
- 主要用来做时间的运算
```python
>>> now = datetime.datetime.now()
>>> print （now）
2015-05-05 09:22:43.142520

>>> b = now + datetime.timedelta(hours=5) #对now增加5个小时
>>> print （b）
2015-05-05 14:22:43.142520

>>> c = now + datetime.timedelta(weeks=2) #增加2周
>>> print（ c）
2015-05-19 09:22:43.142520

>>> d = c - b #计算时差
>>> print （d）
13 days, 19:00:00
```

### 标准库(6)
- urllib

标准库(7)
- xml
  - 扩展标记语言

如果是Python3.3以上，就没有这个必要了，只需要一句话
**import xml.etree.ElementTree as ET**
即可，然后由模块自动来寻找适合的方式。


标准库(8)
- json
就传递数据而言，xml是一种选择，还有另外一种，就是json，它是一种轻量级的数据交换格式，如果读者要做web编程，是会用到它的。

python标准库中有json模块，主要是执行序列化和反序列化功能：

- 序列化：encoding，把一个python对象编码转化成json字符串
- 反序列化：decoding，把json格式字符串解码转换为python数据对象

>

**
- Tableau 构建数据分析思维模型
- Numpy 掌握科学计算中 通用数据的多维容器
- pandas 掌握强大的底层数据操作与分析库
**


依然无法阻挡python在科学计算领域大行其道。之所以这样，就是因为它是python。

- 开源，就这一条就已经足够了，一定要用开源的东西。至于为什么，本教程前面都阐述过了。
- 因为开源，所以有非常棒的社区，里面有相当多支持科学计算的库，不用还等待何时？
- 简单易学，这点对那些不是专业程序员来讲非常重要。我就接触到一些搞天文学和生物学的研究者，他们正在使用python进行计算。
- 在科学计算上如果用了python，能够让数据跟其它的比如web无缝对接，这不是很好的吗？

当然，最重要一点，就是本教程是讲python的，所以，在科学计算这块肯定不会讲Fortran或者R，一定得是python。

