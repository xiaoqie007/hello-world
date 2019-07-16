
**constant algorithms** 常数算法
**linear algorithms** 线性算法
**logarithmic algorithms** 对数算法
**linear algorithms** 线性算法
**quadratic algorithms** 二次算法
**exponential algorithms** 指数算法
**a log linear algorithm** 对线性算法
**searching and sorting algorithms** 搜索和排序算法

```python
 from __future__ import division
 #引用了一个模块之后，再做除法，就不管什么情况，都是得到浮点数的结果了。
 divmod(5,2)  #表示5除以2，返回了商和余数
 (2, 1)
```
round() 实现四舍五入
math模块
dir(math)
**变量无类型，对象有类型**

区别repr()和str，
一个最简单的区别，repr是函数，str是跟int一样，一种对象类型。

r"c:\news"，由r开头引起的字符串，就是原始字符串，在里面放任何字符都表示该字符的原始含义。

python非常提倡的string.format()的格式化方法，其中{索引值}作为占位符
```python
>>> a = "This is a Book"
>>> a.istitle()
False
>>> b = a.title()     #这样就把所有单词的第一个字母转化为大写
>>> b
'This Is A Book'
>>> b.istitle()       #判断每个单词的第一个字母是否为大写
True
```

**join拼接字符串**
```python
>>> b
'www.itdiffer.com'
>>> c = b.split(".")
>>> c
['www', 'itdiffer', 'com']
>>> ".".join(c)
'www.itdiffer.com'
>>> "*".join(c)
'www*itdiffer*com'
```

>**ASCII**（pronunciation: 英语发音：/ˈæski/ ASS-kee[1]，American Standard Code for Information Interchange，美国信息交换标准代码）是基于拉丁字母的一套电脑编码系统。它主要用于显示现代英语，而其扩展版本EASCII则可以部分支持其他西欧语言，并等同于国际标准ISO/IEC 646。由于万维网使得ASCII广为通用，直到2007年12月，逐渐被Unicode取代。

> **Unicode**（中文：万国码、国际码、统一码、单一码）是计算机科学领域里的一项业界标准。它对世界上大部分的文字系统进行了整理、编码，使得电脑可以用更为简单的方式来呈现和处理文字。

>Unicode伴随着通用字符集的标准而发展，同时也以书本的形式对外发表。Unicode至今仍在不断增修，每个新版本都加入更多新的字符。目前最新的版本为7.0.0，已收入超过十万个字符（第十万个字符在2005年获采纳）。Unicode涵盖的数据除了视觉上的字形、编码方法、标准的字符编码外，还包含了字符特性，如大小写字母。

>**UTF-8**（8-bit Unicode Transformation Format）是一种针对Unicode的可变长度字符编码，也是一种前缀码。它可以用来表示Unicode标准中的任何字符，且其编码中的第一个字节仍与ASCII兼容，这使得原来处理ASCII字符的软件无须或只须做少部份修改，即可继续使用。因此，它逐渐成为电子邮件、网页及其他存储或发送文字的应用中，优先采用的编码。

**reversed**函数:它返回一个可以迭代的对象（关于迭代的问题，后续会详述之），不过是已经将原来的序列对象反转了
```python
>>> list(reversed("abcd"))
['d', 'c', 'b', 'a']
```

**list.append(x)** == **a[len(a):]= [x]**

>**'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'**

- append and extend

**list.extend(L)** == **list[len(list):] = L** L:是待并入的list。

- 用内建函数**hasattr()**判断一个字符串是否是可迭代的
```python
astr = 'python'
hasattr(astr, '__iter__')
True
```
>hasattr()的判断本质就是看那个类型中是否有__iter__函数。

**这就是列表的一个重要特征：*列表是可以修改的。这种修改，不是复制一个新的，而是在原地进行修改。***

- 列表扩容的函数append()和extend()
有相同的地方：
  - 都是原地修改列表
  - 既然是原地修改，就不返回值

```
>>> lst = [1,2,3]
>>> lst.append(["qiwsir","github"])
>>> lst
[1, 2, 3, ['qiwsir', 'github']]  #append的结果
>>> len(lst)
4

>>> lst2 = [1,2,3]
>>> lst2.extend(["qiwsir","github"])
>>> lst2
[1, 2, 3, 'qiwsir', 'github']   #extend的结果
>>> len(lst2)
5
```
- **append是整建制地追加，extend是个体化扩编。**

- **保留字**
>and, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with,yield

**list和str**
- 相同点
   - 都属于序列类型的数据
- 区别
   - list是可以改变的，str不可变

**list和str转化**
- split()和join()
```python
>>> s = "I am, writing\npython\tbook on line"   #这个字符串中有空格，逗号，换行\n，tab缩进\t 符号
>>> print s         #输出之后的样式
I am, writing
python  book on line
>>> s.split()       #用split(),但是括号中不输入任何参数
['I', 'am,', 'writing', 'python', 'book', 'on', 'line']
```
**"[sep]".join(list)**

