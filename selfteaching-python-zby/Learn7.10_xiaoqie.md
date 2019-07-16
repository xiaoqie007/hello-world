#### 回顾

**占位符**---**str**
- %s ：字符串(采用str()的显示)
- %d ：十进制整数
- %f ：浮点数
- **用.format()更好**

**tuple**
> tuple是一种序列类型的数据，这点上跟list/str类似。它的特点就是其中的元素不能更改，这点上跟list不同，倒是跟str类似；它的元素又可以是任何类型的数据，这点上跟list相同，但不同于str。

**一般认为,tuple有这类特点,并且也是它使用的情景:**
- Tuple 比 list 操作速度快。如果您定义了一个值的常量集，并且唯一要用它做的是不断地遍历它，请使用 tuple 代替 list。
- 如果对不需要修改的数据进行 “写保护”，可以使代码更安全。使用 tuple 而不是 list 如同拥有一个隐含的 assert 语句，说明这一数据是常量。如果必须要改变这些值，则需要执行 tuple 到 list 的转换 (需要使用一个特殊的函数)。
- Tuples 可以在 dictionary（字典，后面要讲述） 中被用做 key，但是 list 不行。Dictionary key 必须是不可变的。Tuple 本身是不可改变的，但是如果您有一个 list 的 tuple，那就认为是可变的了，用做 dictionary key 就是不安全的。只有字符串、整数或其它对 dictionary 安全的 tuple 才可以用作 dictionary key。
- Tuples 可以用在字符串格式化中。

**type()**

**关于进制转换问题**
- 一般是用几个内建函数实现：
  > int(), bin(), oct(), hex()
```python
>>> int(10)
10
>>> 
>>> bin(10)
'0b1010'
>>> oct(10)
'0o12'
>>> hex(10)
```

**id()**
字典是否能原地修改？
>**列表**可以，所以列表是可变的；**字符串和元组**都不行，所以它们是不可变的。
**实验表明，字典可以原地修改，即它是可变的。**


**创建dict的方法：**
1. 创建一个空的dict，这个空dict，可以在以后向里面加东西用。
2. 利用元组在建构字典
3. 使用{}.fromkeys()
```python
website = {}.fromkeys(("third", 'forth'), 'facebook')
>>> website
{'third': 'facebook', 'forth': 'facebook'}
```
***提醒注意**的是，在字典中的“键”，必须是不可变的数据类型；“值”可以是任意数据类型*
```python
>>> dd = {(1,2):1}
>>> dd
{(1, 2): 1}
>>> dd = {[1,2]:1}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```
**基本操作**
- len(d)，返回字典(d)中的键值对的数量
- d[key]，返回字典(d)中的键(key)的值
- d[key]=value，将值(value)赋给字典(d)中的键(key)
- del d[key]，删除字典(d)的键(key)项（将该键值对删除）
- key in d，检查字典(d)中是否含有键为key的项

在做网页开发的时候，通常要用到模板，也就是你只需要写好HTML代码，然后将某些部位空出来，等着python后台提供相应的数据即可
```python
>>> temp = "<html><head><title>%(lang)s<title><body><p>My name is %(name)s.</p></body></head></html>"
>>> my = {"name":"qiwsir", "lang":"python"}
>>> temp % my
'<html><head><title>python<title><body><p>My name is qiwsir.</p></body></head></ht
```
> temp就是所谓的模板，在双引号所包裹的实质上是一段HTML代码。然后在dict中写好一些数据，按照模板的要求在相应位置显示对应的数据。


**浅拷贝和深拷贝**copy() 和 deepcopy()

```python
>>> x = {"name":"qiwsir", "lang":["python", "java", "c"]}
>>> y = x.copy()
>>> y
{'name': 'qiwsir', 'lang': ['python', 'java', 'c']}
>>> id(x)
4468902360
>>> id(y)
4468901928
>>> y['lang'].remove('c')
>>> y
{'name': 'qiwsir', 'lang': ['python', 'java']}
>>> x
{'name': 'qiwsir', 'lang': ['python', 'java']}
>>> y['name'] = 'laoxiao'
>>> y
{'name': 'laoxiao', 'lang': ['python', 'java']}
>>> x
{'name': 'qiwsir', 'lang': ['python', 'java']}
>>> id(x)
4468902360
>>> id(y)
4468901928
>>> id(x['lang'])
4468911880
>>> id(y['lang'])
4468911880
>>> id(x['name'])
4468608672
>>> id(y['name'])
4468813584
```

```python
>>> import copy
>>> z = copy.deepcopy(x)
>>> z
{'name': 'qiwsir', 'lang': ['python', 'java']}
>>> x
{'name': 'qiwsir', 'lang': ['python', 'java']}
>>> z['lang'].remove('java')
>>> z
{'name': 'qiwsir', 'lang': ['python']}
>>> x
{'name': 'qiwsir', 'lang': ['python', 'java']}
>>> x['name'] = 'zhaozhao'
>>> x
{'name': 'zhaozhao', 'lang': ['python', 'java']}

>>> import copy
>>> z = copy.deepcopy(x)
>>> z
{'name': 'zhaozhao', 'lang': ['python', 'java']}
>>> x
{'name': 'zhaozhao', 'lang': ['python', 'java']}
>>> id(z["lang"])
4425538120
>>> id(x["lang"])
4468911880
```

**dict.get()和dict['key']的区别:**
```python
>>> a = {'name' : 'zhaozhao'}
>>> a.clear()
>>> a
{}
>>> help(dict.get)
Help on method_descriptor:

get(self, key, default=None, /)
    Return the value for key if key is in the dictionary, else default.

>>> print(a.get('name'))
None
>>> a['name']
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a['name']
KeyError: 'name'
```

- d.get("name",'qiwsir')的方式，如果不能得到键"name"的值，就返回后面指定的值"qiwsir"
- D.setdefault(k)执行D.get(k,d),就跟前面一样了，然后，进一步执行另外一个操作，如果键k不在字典中，就在字典中增加这个键值对。当然，如果有就没有必要执行这一步了。

```python
>>> d = {"lang":"python"}
>>> d.get("name",'qiwsir')
'qiwsir'
>>> d
{'lang': 'python'}
>>> d = {"lang":"python"}
>>> d.setdefault("lang")
'python'
>>> d.setdefault("web")
>>> d
{'lang': 'python', 'web': None}
```

>在《列表(3)》中，有关于删除列表中元素的函数pop和remove，这两个的区别在于list.remove(x)用来删除指定的元素，而list.pop([i])用于删除指定索引的元素，如果不提供索引值，就默认删除最后一个。
 - **值得注意的是，pop函数中的参数是不能省略的，这跟列表中的那个pop有所不同。**
```python
>>> dd
{'name': 'qiwsir', 'lang': 'python', 'web': 'www.itdiffer.com'}
>>> dd.pop()
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    dd.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> dd.pop('name')
'qiwsir'
>>> dd
{'lang': 'python', 'web': 'www.itdiffer.com'}
```
**.popitem()**
```python
>>> dd
{'lang': 'python', 'web': 'www.itdiffer.com'}
>>> dd.popitem()
('web', 'www.itdiffer.com')
>>> dd.popitem()
('lang', 'python')
>>> dd.popitem()
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    dd.popitem()
KeyError: 'popitem(): dictionary is empty'
>>> dd
{}
```
**.update()**
```python
>>> d1 = {"lang":"python"}
>>> d2 = {"song":"I dreamed a dream"}
>>> d1.update(d2)
>>> d1
{'lang': 'python', 'song': 'I dreamed a dream'}
>>> d2
{'song': 'I dreamed a dream'}
>>> d2.update([("name","qiwsir"), ("web","itdiffer.com")])
>>> d2
{'song': 'I dreamed a dream', 'name': 'qiwsir', 'web': 'itdiffer.com'}
```
- 列表的元组是键值对

**.has_key()**





