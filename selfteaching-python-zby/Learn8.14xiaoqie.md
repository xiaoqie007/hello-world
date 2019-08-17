
**tuple**

变量拆分常用来迭代元组或列表序列：
```python
>>> seq = [(1,2,3), (4,5,6),(7,8,9)]

>>> for a,b,c in seq:
	print('a={0}, b={1},c={2}'.format(a,b,c))
	
a=1, b=2,c=3
a=4, b=5,c=6
a=7, b=8,c=9

>>> for a,b,c in seq:
	print('a={1}, b={2},c={0}'.format(a,b,c))
	
a=2, b=3,c=1
a=5, b=6,c=4
a=8, b=9,c=7
>>> 
```

Python最近新增了更多高级的元组拆分功能，允许从元组的开头“摘取”几个元素。它使用了特殊的语法*rest，这也用在函数签名中以抓取任意长度列表的位置参数：

>>> values = 1,2,3,4,5
>>> a,b, *rest = values
>>> a,b
(1, 2)
>>> rest
[3, 4, 5]
>>> 

rest的部分是想要舍弃的部分，rest的名字不重要。作为惯用写法，许多Python程序员会将不需要的变量使用下划线：

```python
>>> a,b, *_ = values
>>> a,b
(1, 2)

>>> _
[3, 4, 5]
>>> 
```

list添加和删除元素
append 在列表末尾添加元素
insert 可以在特定的位置插入元素
插入的序号必须在0和列表长度之间。

> 警告：与append相比，insert耗费的计算量大，因为对后续元素的引用必须在内部迁移，以便为新元素提供空间。如果要在序列的头部和尾部插入元素，你可能需要使用collections.deque，一个双尾部队列。

insert的逆运算是pop，它移除并返回指定位置的元素：

如果已经定义了一个列表，用extend方法可以追加多个元素：


通过加法将列表串联的计算量较大，因为要新建一个列表，并且要复制对象。用extend追加元素，尤其是到一个大列表中，更为可取。因此：



排序

你可以用sort函数将一个列表原地排序（不创建新的对象）：

```python
>>> a = [7,3,2,4,3,2]
>>> a.sort()
>>> a
[2, 2, 3, 3, 4, 7]
```
sort有一些选项，有时会很好用。其中之一是二级排序key，可以用这个key进行排序。例如，我们可以按长度对字符串进行排序：

```python
>>> b = ['saw', 'small', 'He', 'foxes', 'six']
>>> b
['saw', 'small', 'He', 'foxes', 'six']
>>> b.sort(key = len)
>>> b
['He', 'saw', 'six', 'small', 'foxes']
>>> 
```

### 二分搜索和维护已排序的列表


bisect模块支持二分查找，和向已排序的列表插入值。bisect.bisect可以找到插入值后仍保证排序的位置，bisect.insort是向这个位置插入值：

```pyhon
In [1]: import bisect                            
In [2]: c = [1,2,2,2,3,4,7]                                                     
In [3]: bisect.bisect(c, 2)                                                     
Out[3]: 4

In [4]: bisect.bisect(c, 6)                                           
Out[4]: 6

In [5]: c                                                                       
Out[5]: [1, 2, 2, 2, 3, 4, 7]

In [6]: bisect.insort(c, 6)                                                     
In [7]: c                                                                       
Out[7]: [1, 2, 2, 2, 3, 4, 6, 7]

```

**注意：bisect模块不会检查列表是否已排好序，进行检查的话会耗费大量计算。因此，对未排序的列表使用bisect不会产生错误，但结果不一定正确。**

切片

···python
In [19]: seq                                                                    
Out[19]: [7, 2, 3, 6, 3, 5, 6, 0, 1]

In [20]: seq[-3:]                                                               
Out[20]: [6, 0, 1]

In [21]: seq[::2]                                                               
Out[21]: [7, 3, 3, 6, 1]

In [22]: seq[::-1]                                                              
Out[22]: [1, 0, 6, 5, 3, 6, 3, 2, 7]

In [23]: seq[::3]                                                               
Out[23]: [7, 6, 6]
···

**序列函数**
当你索引数据时，使用enumerate的一个好方法是计算序列（唯一的）dict映射到位置的值：


```python
enumerate函数
>>> collection = [1,2,3,4,5]
>>> for value in collection:
	# do something with value
	i += 1

	
>>> i
5
>>> for i, value in enumerate(collection):
	print(i, value)
	
0 1
1 2
2 3
3 4
4 5
```
```python
some_list = ['foo', 'bar', 'baz']
>>> mapping = {}
>>> for i, v in enumerate(some_list):
	mapping[v] = i

	
>>> mapping
{'foo': 0, 'bar': 1, 'baz': 2}
>>> 
```

**sorted函数**

sorted函数可以从任意序列的元素返回一个新的排好序的列表：

```python
>>> a = 'hajsn dndks'
>>> sorted(a)
[' ', 'a', 'd', 'd', 'h', 'j', 'k', 'n', 'n', 's', 's']

>>> a = [2,3,4,2,4,33,2,3,2,22,3,2,3]
>>> sorted(a)
[2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 22, 33]
>>> 
```

**zip函数**
zip可以将多个列表、元组或其它序列成对组合成一个元组列表：


给出一个“被压缩的”序列，zip可以被用来解压序列。也可以当作把行的列表转换为列的列表。这个方法看起来有点神奇：

```python
>>> seq1 = [1,2,3,4,5]
>>> seq2 = ['one', 'two', 'three']
>>> zipped = zip(seq1, seq2)
>>> pitcher = list(zipped)
>>> pitcher
[(1, 'one'), (2, 'two'), (3, 'three')]
>>> first_name, last_name = zip(*pitcher)
>>> first_name
(1, 2, 3)
>>> last_name
('one', 'two', 'three')
>>> 
```

**reversed函数**
```python
- reversed可以从后向前迭代一个序列：
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(reversed(range(10)))
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> 
```

要记住reversed是一个生成器（后面详细介绍），只有实体化（即列表或for循环）之后才能创建翻转的序列。


字典
字典可能是Python最为重要的数据结构。它更为常见的名字是哈希映射或关联数组。它是键值对的大小可变集合，键和值都是Python对象。创建字典的方法之一是使用尖括号，用冒号分隔键和值：
```python
>>> empty_dict = {}
>>> d1 = {'a': 'some value', 'b': [1,2,3,4]}
>>> d1
{'a': 'some value', 'b': [1, 2, 3, 4]}
>>> d1[8] = 'zhaozhao'
>>> d1
{'a': 'some value', 'b': [1, 2, 3, 4], 8: 'zhaozhao'}
#你可以像访问列表或元组中的元素一样，访问、插入或设定字典中的元素：
>>> d1['b']
[1, 2, 3, 4]

#你可以用检查列表和元组是否包含某个值的方法，检查字典中是否包含某个键：
>>> 'b' in d1
True

>>> d1[8] = 'liwei'
>>> d1
{'a': 'some value', 'b': [1, 2, 3, 4], 8: 'liwei'}

>>> d1['dummy'] = 'another value'
>>> d1
{'a': 'some value', 'b': [1, 2, 3, 4], 8: 'liwei', 'dummy': 'another value'}

#可以用del关键字或pop方法（返回值的同时删除键）删除值：
>>> del d1[8]
>>> d1
{'a': 'some value', 'b': [1, 2, 3, 4], 'dummy': 'another value'}

>>> ret = d1.pop('dummy')
>>> ret
'another value'
>>> d1
{'a': 'some value', 'b': [1, 2, 3, 4]}
>>> 
```

- keys和values是字典的键和值的迭代器方法。虽然键值对没有顺序，这两个方法可以用相同的顺序输出键和值：
```python
>>> list(d1.keys())
['a', 'b']
>>> list(d1.values())
['some value', [1, 2, 3, 4]]
>>> list(d1.values())
['some value', [1, 2, 3, 4]]
>>> 

#用update方法可以将一个字典与另一个融合：

>>> d1.update({'b': 'foo', 'c': 12})
>>> d1
{'a': 'some value', 'b': 'foo', 'c': 12}
>>> 
```
#update方法是原地改变字典，因此任何传递给update的键的旧的值都会被舍弃。

用序列创建字典

常常，你可能想将两个序列配对组合成字典。下面是一种写法：
```python
mapping = {}
for key, value in zip(key_list, value_list):
    mapping[key] = value
```
```python
>>> mapping = {}
>>> key_list = [1,2,3]
>>> value_list = ['one', 'two', 'three']
>>> for key, value in zip(key_list, value_list):
	mapping[key] = value

#因为字典本质上是2元元组的集合，dict可以接受2元元组的列表：	
>>> mapping
{1: 'one', 2: 'two', 3: 'three'}
>>> mapping1 = dict(zip(range(5), reversed(range(5))))
>>> mapping
{1: 'one', 2: 'two', 3: 'three'}
>>> mapping1
{0: 4, 1: 3, 2: 2, 3: 1, 4: 0}
>>> 


- 默认值

下面的逻辑很常见：

```python
if key in some_dict:
    value = some_dict[key]
else:
    value = default_value
```
因此，dict的方法get和pop可以取默认值进行返回，上面的if-else语句可以简写成下面：

```python
value = some_dict.get(key, default_value)
```


**setdefault**

方法就正是干这个的。前面的for循环可以改写为：
```python
for word in words:
    letter = word[0]
    by_letter.setdefault(letter, []).append(word)
```

collections模块有一个很有用的类，defaultdict，它可以进一步简化上面。传递类型或函数以生成每个位置的默认值：

```python
from collections import defaultdict
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
```

有效的键类型

字典的值可以是任意Python对象，而键通常是不可变的标量类型（整数、浮点型、字符串）或元组（元组中的对象必须是不可变的）。这被称为“可哈希性”。可以用hash函数检测一个对象是否是可哈希的（可被用作字典的键）:

**集合**
集合是无序的不可重复的元素的集合。你可以把它当做字典，但是只有键没有值。可以用两种方式创建集合：通过set函数或使用尖括号set语句：

所有逻辑集合操作都有另外的原地实现方法，可以直接用结果替代集合的内容。对于大的集合，这么做效率更高：

列表、集合和字典推导式

```python
[expr for val in collection if condition]
```
它等同于下面的for循环;

```python
result = []
for val in collection:
    if condition:
	    result.append(expr)

```
```python
>>> strings = ['a', 'as', 'bat', 'cat', 'dove', 'python']
>>> [x.upper() for x in strings if len(x) > 2]
['BAT', 'CAT', 'DOVE', 'PYTHON']
>>> [x.upper() for x in strings if len(x) > 1]
['AS', 'BAT', 'CAT', 'DOVE', 'PYTHON']
>>> [x.upper() for x in strings if len(x) > 3]
['DOVE', 'PYTHON']
>>> 
```
用相似的方法，还可以推导集合和字典。字典的推导式如下所示：
```python
dict_comp = {key-expr : value-expr for value in collection if condition}
```
集合的推导式与列表很像，只不过用的是尖括号：

```python
set_comp = {expr for value in collection if condition}
```
>>> strings = ['a', 'as', 'at', 'cat', 've', 'python']
>>> unique_lengths = {len(x) for x in strings}
>>> unique_lengths
{1, 2, 3, 6}
>>> 

map函数可以进一步简化：
```python
>>> set(map(len, strings))
{1, 2, 3, 6}
>>> 
```

作为一个字典推导式的例子，我们可以创建一个字符串的查找映射表以确定它在列表中的位置：

```python
>>> string = ['sd', 'sdsd', 'reds', 'defswe', 'sdsefs', 'sfeffdss']
>>> loc_mapping = {val: index for index, val in enumerate(strings)}
>>> loc_mapping
{'a': 0, 'as': 1, 'at': 2, 'cat': 3, 've': 4, 'python': 5}
>>> 
```

嵌套列表推导式