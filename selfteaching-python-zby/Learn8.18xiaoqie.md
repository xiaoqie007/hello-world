**镶嵌列表推导式**
```python
>>> all_data
[['John', 'Emily', 'Michael', 'Mary', 'Steven'], ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
>>> result = [name for names in all_data for name in names if name.count('e') >=2]
>>> result
['Steven']
>>> 
```
- 嵌套列表推导式看起来有些复杂。列表推导式的for部分是根据嵌套的顺序，过滤条件还是放在最后

你可以有任意多级别的嵌套，但是如果你有两三个以上的嵌套，你就应该考虑下代码可读性的问题了。分辨列表推导式的列表推导式中的语法也是很重要的：
```python
>>> [[x for x in tup] for tup in some_tuples]
[[1, 2, 3, 4, 9], [4, 5, 6, 7, 7, 8, 9], [7, 8, 9, 11, 12, 13]]
>>> 
```
这段代码产生了一个列表的列表，而不是扁平化的只包含元素的列表

函数
```python
>>> def my_function(x, y, z = 1.5):# x,y 是位置参数（positional）, z是一些关键字参数（keyword）.
	if z > 1:
		return z * (x + y)
	else:
		return z / (x + y)
	
>>> my_function
<function my_function at 0x10658eae8>
>>> print(my_function)
<function my_function at 0x10658eae8>
>>> my_function(5,6,z = 5)
55
>>> my_function(5,6,z = 0.7)
0.06363636363636363
>>> my_function(5,6,z = 1.5)
16.5
>>> my_function(5,6)
16.5
>>> 
```

函数参数的主要限制在于：关键字参数必须位于位置参数（如果有的话）之后。你可以任何顺序指定关键字参数。也就是说，你不用死记硬背函数参数的顺序，只要记得它们的名字就可以了。

笔记：也可以用关键字传递位置参数， 前面的例子，也可以写为
```python
my_function(x= 5, y= 6, z= 7)
my_function(y= 6, x= 5, z= 7)
#这种写法可以提高可读性。
```

命名空间、作用域，和局部函数

- 注意：我常常建议人们不要频繁使用global关键字。
因为全局变量一般是用于存放系统的某些状态的。如果你发现自己用了很多，那可能就说明得要来点儿面向对象编程了（即使用类）。

返回多个值

```python
>>> def f():
	a = 5
	b = 6
	c = 7
	return{'a':a, 'b':b, ' c':c}

>>> a = f()
>>> a
{'a': 5, 'b': 6, ' c': 7}
>>> 
```
