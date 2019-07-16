####总结：
- 数据类型:int/str/bool/list/dict/tuple
 1. 如何记住这些方法：
    - 交互模式下dir()或help()
    - google
- 在上述类型中：
 - 能够索引的，如list/str，其中的元素可以重复
 - 可变的，如list/dict，即其中的元素/键值可以原地修改
 - 不可变的，如str/int，即不能进行原地修改
 - 无索引序列的，如dict，即其中的元素（键值对）没有排列顺序
 
 **set**
 - 以**set()** 来建立集合，这种方式所创立的集合都是可原处修改的集合，或者说是可变的，也可以说是unhashable
 - 还有一种集合，不能在原处修改。这种集合的创建方法是用**frozenset()**，顾名思义，这是一个被冻结的集合，当然是不能修改了，那么这种集合就是hashable类型——可哈希。
```python
>>> f_set = frozenset('python')
>>> f_set
frozenset({'n', 'y', 'o', 't', 'h', 'p'})
>>> f_set.add('qiwsir')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    f_set.add('qiwsir')
AttributeError: 'frozenset' object has no attribute 'add'
>>> a_set = set('python')
>>> a_set
{'n', 'y', 'o', 't', 'h', 'p'}
>>> a_set.add('qiwsir')
>>> a_set
{'n', 'y', 'o', 't', 'h', 'p', 'qiwsir'}
```
**运算符**
 - 比较运算符
 - 逻辑运算符
 - 布尔运算
 - ......

**语句**

**一般所有高级语言，都包含如下语句，Python也不例外：**

- 循环语句:容许一些语句反复运行数次。循环可依据一个默认的数目来决定运行这些语句的次数；或反复运行它们，直至某些条件改变。
- 条件语句:容许仅当某些条件成立时才运行某个区块。否则，这个区块中的语句会略去，然后按区块后的语句继续运行。
- 无条件分支语句容许运行顺序转移到程序的其他部分之中。包括跳跃（在很多语言中称为Goto）、副程序和Procedure等。
循环、条件分支和无条件分支都是控制流程。

**有哪些语句：**
 - **print**
 - **import**
 - **赋值语句**
 - **条件语句**
   1. 必须要通过缩进方式来表示语句块的开始和结束
   2. 缩进用四个空格（也是必须的，别的方式或许可以，但不提倡）
   **if/else/elif**

   ```python
    if 条件1：
       执行的内容1
    elif 条件2:
    执行的内容2
    elif 条件3：
    执行的内容3
    else:
    执行的内容4
    ```
   3. 三元操作符: **A = Y if X else Z**
     - 如果X为真，那么就执行A=Y
     - 如果X为假，就执行A=Z

```python
>>> x = 4
>>> y = 5
>>> a = 'zahozhao' if x > y else 'liwei'
>>> a
'liwei'
>>> a = 'zahozhao' if x == y else 'liwei'
>>> a
'liwei'
>>> a = 'zahozhao' if x < y else 'liwei'
>>> a
'zahozhao'
```


  

