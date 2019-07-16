 **循环**
  - range(start,stop[, step])

 1. 这个函数可以创建一个数字元素组成的列表。
 2. 这个函数最常用于for循环（关于for循环，马上就要涉及到了）
 3. 函数的参数必须是整数，默认从0开始。返回值是类似[start, start + step, start + 2*step, ...]的列表。
 4. step默认值是1。如果不写，就是按照此值。
 5. 如果step是正数，返回list的最最后的值不包含stop值，即start+istep这个值小于stop；如果step是负数，start+istep的值大于stop。
 6. step不能等于零，如果等于零，就报错。

 #### **很好的zip()**
 ```python
>>> a = [1,2,3,4,5]
>>> b = [9,8,7,6,5]
>>> c = []
>>> for i in range(len(a)):
...     c.append(a[i]+b[i])
... 
>>> c
[10, 10, 10, 10, 10]
```
```python
>>> a = [1,2,3,4,5]
>>> b = [9,8,7,6,5,1,3]
>>> d = []
>>> for x,y in zip(a,b):
...     d.append(x+y)
... 
>>> d
[10, 10, 10, 10, 10]
```
```python
>>> a = [1,2,3,4,5]
>>> b = ["python","www.itdiffer.com","qiwsir"]
>>> length = len(a) if len(a) < len(b) else len(b)
>>> length
3
>>> c = []
>>> for i in range(length):
	c.append(str(a[i])+ ':'+b[i])	
>>> c
['1:python', '2:www.itdiffer.com', '3:qiwsir']


>>> d = []
>>> for x, y in zip(a, b):
	d.append(str(x) + y)	
>>> d
['1python', '2www.itdiffer.com', '3qiwsir']
```

>问题：有一个dictionary，
**myinfor = {"name":"qiwsir","site":"qiwsir.github.io","lang":"python"}**,将这个字典变换成：
**infor = {"qiwsir":"name","qiwsir.github.io":"site","python":"lang"}**

- 方法1: for

```
infor = {}
for k, v in myinfor.items():
    infor[v] = k
infor
{"qiwsir":"name","qiwsir.github.io":"site","python":"lang"}
```

- 方法2: zip

**dict(zip(myinfor.values(), myinfor.keys()))**

   - 以上分解：
```python
>>> myinfor.values()    #得到两个list
['python', 'qiwsir', 'qiwsir.github.io']
>>> myinfor.keys()
['lang', 'name', 'site']
>>> temp = zip(myinfor.values(),myinfor.keys())     #压缩成一个list，每个元素是一个tuple
>>> temp
[('python', 'lang'), ('qiwsir', 'name'), ('qiwsir.github.io', 'site')]

>>> dict(temp)                          #这是函数dict()的功能，将上述列表转化为dictionary
{'python': 'lang', 'qiwsir.github.io': 'site', 'qiwsir': 'name'}
```

**同时得到元素索引和元素怎么办？**
**enumerate()**

**问题：将字符串中的某些字符替换为其它的字符串。原始字符串"Do you love Canglaoshi? Canglaoshi is a good teacher."，请将"Canglaoshi"替换为"PHP".**
```python
>>> raw = "Do you love Canglaoshi? Canglaoshi is a good teacher."
>>> raw_list = raw.split(' ')
>>> for i, string in enumerate(raw_list):
	if string == "Canglaoshi":
		raw_list[i] = 'PHP'		
>>> raw_list
['Do', 'you', 'love', 'Canglaoshi?', 'PHP', 'is', 'a', 'good', 'teacher.']


>>> for i, string in enumerate(raw_list):
	if "Canglaoshi" in string:
		raw_list[i] = "PHP"
		
>>> raw_list
['Do', 'you', 'love', 'PHP', 'PHP', 'is', 'a', 'good', 'teacher.']
```
**list解析**
```python
>>> power2
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> squares = [x**2 for x in range(1, 10)]
>>> squares
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```
```python
>>> myfamily = [' zhaozhao ','liwei de ','  xiaoyu']
>>> [one.strip() for one in myfamily]
['zhaozhao', 'liwei de', 'xiaoyu']
```