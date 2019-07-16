#### **练习1**
- 问题描述

>有一个列表，其中包括10个元素，例如这个列表是[1,2,3,4,5,6,7,8,9,0],要求将列表中的每个元素一次向前移动一个位置，第一个元素到列表的最后，然后输出这个列表。最终样式是[2,3,4,5,6,7,8,9,0,1]

```pythion
>>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> b = a.pop(0)
>>> b
1
>>> a.append(b)
>>> a
[2, 3, 4, 5, 6, 7, 8, 9, 0, 1]
>>> 
```

#### **练习2**
- 问题描述

按照下面的要求实现对列表的操作：

>产生一个列表，其中有40个元素，每个元素是0到100的一个随机整数
如果这个列表中的数据代表着某个班级40人的分数，请计算成绩低于平均分的学生人数，并输出
对上面的列表元素从大到小排序
```python
import random
score = [random.randint(0,100) for i in range(40)]    #0到100之间，随机得到40个整数，组成列表
print (score)

num = len(score)
sum_score = sum(score)               #对列表中的整数求和
ave_num = sum_score/num              #计算平均数
less_ave = len([i for i in score if i<ave_num])    #将小于平均数的找出来，组成新的列表，并度量该列表的长度
print( "the average score is:%.1f" % ave_num)
print ("There are %d students less than average." % less_ave)

sorted_score = sorted(score, reverse=True)    #对原列表排序
print (sorted_score)
```

#### **练习3**
- 问题描述

如果将一句话作为一个字符串，那么这个字符串中必然会有空格（这里仅讨论英文），比如"How are you."，但有的时候，会在两个单词之间多大一个空格。现在的任务是，如果一个字符串中有连续的两个空格，请把它删除。
```python
>>> string = "I love  zhaozhao and  python.  "
>>> str_lst = string.split(' ')#以空格为分割，得到词汇列表
>>> print(str_lst)
['I', 'love', '', 'zhaozhao', 'and', '', 'python.', '', '']

>>> words = [s.strip() for s in str_lst] #剔除单词两边的空格
>>> print(words)
['I', 'love', '', 'zhaozhao', 'and', '', 'python.', '', '']
>>> words = [s for s in str_lst if s != ' '] #以空格为链接符，将单词链接起来
>>> print(words)
['I', 'love', '', 'zhaozhao', 'and', '', 'python.', '', '']
```
#### **BUG**
- **结果是令人失望的。经过一番折腾，空格根本就没有被消除。最后的输出和一开始的字符串完全一样。泪奔！**
- **查找原因。**
- **从输出中已经清楚表示了。当执行string.split(" ")的时候，是以空格为分割符，将字符串分割，并返回列表。列表中元素是由单词组成。原来字符串中单词之间的空格已经被作为分隔符，那么列表中单词两遍就没有空格了。所以，前面代码中就无需在用strip()去删除空格。另外，特别要注意的是，有两个空格连着呢，其中一个空格作为分隔符，另外一个空格就作为列表元素被返回了。这样一来，分割之后的操作都无作用了。**

```python
>>> words = [s for s in str_lst if s != '']#利用列表解析，将空格检出
>>> print(words)
['I', 'love', 'zhaozhao', 'and', 'python.']
>>> new_string = ' '.join(words)#以空格为链接符，将单词链接
>>> print(new_string)
I love zhaozhao and python.


>>> other_str = new_string.split('.')#以句号为分割，得到词汇列表
>>> other_str
['I love zhaozhao and python', '']
>>> lst1 = [i for i in other_str if i != '']#利用列表解析，将空格检出
>>> lst1
['I love zhaozhao and python']
>>> new_str1 = ' '.join(lst1)#以空格为链接符，将单词链接
>>> new_str1
'I love zhaozhao and python'
```

####**练习4**
- 问题描述
  - 斐波那契数列
```python
a, b = 0, 1
for i in range(4): #改变这里的数，就能得到相应的结果
    a, b = b, a+b
print(a)
print(b)
```

