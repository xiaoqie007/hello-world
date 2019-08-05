#### pandas

**Setting**
设置新列，根据索引自动对齐数据
Setting a new column automatically aligns the data by the indexes.设置新列根据索引自动对齐数据

Setting by assigning with a NumPy array:


Missing data:

df1 = df.reindex(index= dates[0:4], columns= list(df.columns) + ['E'])

df1.loc[dates[0]: dates[1], 'E'] = 1

To drop any rows that have missing data.

删除任何缺省的数据的行

df1.dropna(how='any')

Filling missing data.:

df1.fillna(value=5)


To get the boolean mask where values are nan.
获取值为nan的布尔掩码

**Stats** 统计


Operating with objects that have different dimensionality and need alignment. In addition, pandas automatically broadcasts along the specified dimension.
使用具有不同维度且需要对齐的对象进行操作。 此外，pandas会自动沿指定维度进行广播。

```python
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
# shift 转移

df.sub(s, axis='index')
```


**apply**
应用

Applying functions to the data:

```python
numpy.cumsum(a, axis=None, dtype=None, out=None)[source]
Return the cumulative sum of the elements along a given axis.
```

df.apply(np.cumsum)

s = pd.Series(np.random.randint(0, 7, size=10))

s.value_counts()

**String Methods**

Series is equipped with a set of string processing methods in the str attribute that make it easy to operate on each element of the array, as in the code snippet below. Note that pattern-matching in str generally uses regular expressions by default (and in some cases always uses them). See more at Vectorized String Methods.

s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])

s.str.lower()

**Merge** 合并
Concatenating pandas objects together with concat():
使用 concat() 连接 pandans 对象

```python
df = pd.DataFrame(np.random.randn(10, 7))   #创建
pieces = [df[:2], df[3:4], df[6:]]   # 分块 break it into pieces
pd.concat(pieces)    #合并
```



```python
>>> pd.concat(pieces, ignore_index = True) #ignore_index的作用在合并后更新index

          0         1         2         3
0 -0.414600  2.199826  0.143863  0.465397
1  1.436002  0.373170 -1.780127  0.701960
2 -0.090006 -0.694837 -1.867175 -0.461207
3  1.711480  1.045030 -1.047360 -0.828558
4 -0.696143 -0.478827  0.178508  1.302182
>>> pd.concat(pieces)
          0         1         2         3
1 -0.414600  2.199826  0.143863  0.465397
2  1.436002  0.373170 -1.780127  0.701960
5 -0.090006 -0.694837 -1.867175 -0.461207
8  1.711480  1.045030 -1.047360 -0.828558
9 -0.696143 -0.478827  0.178508  1.302182
>>> 
````




**Join**

- merge
```python
   left = pd.DataFrame({'key':['foo', 'foo'], 'lval':[1, 2]})
   right = pd.DataFrame({'key':['foo', 'foo'], 'rval':[4, 5]})
   pd.merge(left, right, on= 'key')
```
  another
  ```python
  left = pd.DataFrame({'key':['foo', 'bar'], 'lval':[1, 2]})
  right = pd.DataFrame({'key':['foo', 'bar'], 'lval':[3, 4]})
  pd.merge(left, right, on = 'key')
```


**Append**

Append rows to a dataframe. See the Appending section.将行附加到数据框

```python
>>> df = pd.DataFrame(np. random.randn(8,4), columns= ['Q', 'W', 'E', 'R'])
>>> df
          Q         W         E         R
0  0.723308  1.432589  0.159191  0.155049
1  0.291876  0.086705 -0.038516 -1.193969
2  1.072239 -0.095449  0.188762 -1.723831
3  0.855219 -0.830527  0.638719  0.174604
4  0.618002 -0.095151  0.434471 -0.787565
5  0.098562 -2.059050  2.454902 -0.601307
6  1.214600  1.916077  1.321174  0.308665
7  1.549496  0.467249  2.025968 -1.173527
>>> s = df.iloc[5]
>>> s
Q    0.098562
W   -2.059050
E    2.454902
R   -0.601307
Name: 5, dtype: float64
>>> df.append(s) #ignore_index 默认False, 最后索引未更新
          Q         W         E         R
0  0.723308  1.432589  0.159191  0.155049
1  0.291876  0.086705 -0.038516 -1.193969
2  1.072239 -0.095449  0.188762 -1.723831
3  0.855219 -0.830527  0.638719  0.174604
4  0.618002 -0.095151  0.434471 -0.787565
5  0.098562 -2.059050  2.454902 -0.601307
6  1.214600  1.916077  1.321174  0.308665
7  1.549496  0.467249  2.025968 -1.173527
5  0.098562 -2.059050  2.454902 -0.601307
>>> df.append(s, ignore_index = True) #设置ignore=True后索引更新
          Q         W         E         R
0  0.723308  1.432589  0.159191  0.155049
1  0.291876  0.086705 -0.038516 -1.193969
2  1.072239 -0.095449  0.188762 -1.723831
3  0.855219 -0.830527  0.638719  0.174604
4  0.618002 -0.095151  0.434471 -0.787565
5  0.098562 -2.059050  2.454902 -0.601307
6  1.214600  1.916077  1.321174  0.308665
7  1.549496  0.467249  2.025968 -1.173527
8  0.098562 -2.059050  2.454902 -0.601307
>>> 
```


**Grouping**

By **“group by”** we are referring to a process involving one or more of the following steps:

**Splitting** the data into groups based on some criteria

**Applying** a function to each group independently

**Combining** the results into a data structure

```python
>>> df = pd.DataFrame({'A':['foo', 'bar', 'foo'],
		       'B':['one', 'two', 'three'],
		       'C':np.random.randn(3),
		       'D':np.random.randn(3)})
>>> df
     A      B         C         D
0  foo    one -0.838596  0.015826
1  bar    two  1.345653 -1.302828
2  foo  three  1.204724  1.579458
>>> df.groupby('A').sum()
            C         D
A                      
bar  1.345653 -1.302828
foo  0.366128  1.595284
>>> df.groupby(['A', 'B']).sum()
                  C         D
A   B                        
bar two    1.345653 -1.302828
foo one   -0.838596  0.015826
    three  1.204724  1.579458
>>> 
```


**Reshaping**
重塑
```python
#创建元组
>>> tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
			 'foo', 'foo', 'qux', 'qux'],
			['one', 'two', 'one', 'two',
			 'one', 'teo', 'one', 'two']]))
		  
>>> tuples
		  
[('bar', 'one'), ('bar', 'two'), ('baz', 'one'), ('baz', 'two'), ('foo', 'one'), ('foo', 'teo'), ('qux', 'one'), ('qux', 'two')]

>>> tuples[4] #索引位置4的值		  
('foo', 'one')

>>> tuples[0]#索引位置0的值		  
('bar', 'one')

>>> index = pd.MultiIndex.from_tuples(tuples, names= ['frist', 'second'])
		  
>>> index
		  
MultiIndex([('bar', 'one'),
            ('bar', 'two'),
            ('baz', 'one'),
            ('baz', 'two'),
            ('foo', 'one'),
            ('foo', 'teo'),
            ('qux', 'one'),
            ('qux', 'two')],
           names=['frist', 'second'])

>>> df = pd.DataFrame(np.random.randn(8, 2), index= index, columns= ['A', 'B'])
		  
>>> df		  
                     A         B
frist second                    
bar   one    -0.557433 -0.673296
      two    -0.835083  0.216120
baz   one     1.771292 -0.774356
      two    -0.121626 -0.401838
foo   one    -0.104992 -0.303534
      teo    -1.352586  1.365828
qux   one     0.710420  0.316396
      two     0.947269  0.480302
>>> df2 = df[:4]
		  
>>> df2
		  
                     A         B
frist second                    
bar   one    -0.557433 -0.673296
      two    -0.835083  0.216120
baz   one     1.771292 -0.774356
      two    -0.121626 -0.401838

# The stack() method “compresses” a level in the DataFrame’s columns.
		  
>>> stacked = df2.stack()
		  
>>> stacked
		  
frist  second   
bar    one     A   -0.557433
               B   -0.673296
       two     A   -0.835083
               B    0.216120
baz    one     A    1.771292
               B   -0.774356
       two     A   -0.121626
               B   -0.401838
dtype: float64

# With a “stacked” DataFrame or Series (having a MultiIndex as the index), the inverse operation of stack() is unstack(), which by default unstacks the last level:
		  
>>> stacked.unstack()
		  
                     A         B
frist second                    
bar   one    -0.557433 -0.673296
      two    -0.835083  0.216120
baz   one     1.771292 -0.774356
      two    -0.121626 -0.401838
>>> stacked.unstack(1)
		  
second        one       two
frist                      
bar   A -0.557433 -0.835083
      B -0.673296  0.216120
baz   A  1.771292 -0.121626
      B -0.774356 -0.401838
>>> stacked.unstack(0)
		  
frist          bar       baz
second                      
one    A -0.557433  1.771292
       B -0.673296 -0.774356
two    A -0.835083 -0.121626
       B  0.216120 -0.401838
>>> 
```

**Pivot tables**
数据透视表

Converting between period and timestamp enables some convenient arithmetic functions to be used. In the following example, we convert a quarterly frequency with year ending in November to 9am of the end of the month following the quarter end:

在句点和时间戳之间进行转换可以使用一些方便的算术函数。 在下面的示例中，我们将季度频率与11月结束的年度转换为季度结束后的月末的上午9点：
**???**
```python
>>> prng = pd.period_range('1990Q1', '2000Q4', freq = 'Q-NOV')
			
>>> ts = pd.Series(np.random.randn(len(prng)), prng)
			
>>> ts.index = (prng.asfreq('M', 'e')+ 1).asfreq('H', 's') + 9
			
>>> ts.head()
			
1990-03-01 09:00   -0.094215
1990-06-01 09:00    0.954762
1990-09-01 09:00   -1.152465
1990-12-01 09:00    1.469307
1991-03-01 09:00   -0.129239
Freq: H, dtype: float64
>>> 
```

**categoricals**

pandas can include categorical data in a DataFrame. For full docs, see the categorical introduction and the API documentation.
categoricals
pandas可以在DataFrame中包含分类数据。 有关完整文档，请参阅分类简介和API文档。
```python
>>> df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6],"raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})
			
>>> df['grade'] = df['raw_grade'].astype('category')
			
>>> df['grade']
			
0    a
1    b
2    b
3    a
4    a
5    e
Name: grade, dtype: category
Categories (3, object): [a, b, e]
>>> 
```

Rename the categories to more meaningful names (assigning to Series.cat.categories is inplace!).

```python
>>> df['grade'].cat.categories = ['very good', 'good', 'very bad']
			
>>> df['grade'] = df['grade'].cat.set_categories(['very bad', 'bad', 'medium', 'good', 'very good'])
			
>>> df['grade']
			
0    very good
1         good
2         good
3    very good
4    very good
5     very bad
Name: grade, dtype: category
Categories (5, object): [very bad, bad, medium, good, very good]
>>> df.sort_values(by = 'grade')
			
   id raw_grade      grade
5   6         e   very bad
1   2         b       good
2   3         b       good
0   1         a  very good
3   4         a  very good
4   5         a  very good
>>> df.groupby('grade').size()
			
grade
very bad     1
bad          0
medium       0
good         2
very good    3
dtype: int64
>>> 
```


**Plotting** 绘制

**Getting data in/out**
- csv
```
df.to_csv('foo.csv')
pd.read_csv('foo.csv')
```
- HDF5
```
df.to_hdf('foo.h5', 'df')
pd.read_hdf('foo.h5', 'df')
```
- Excel
```
df.to_excel('foo.xlsx', sheet_name='Sheet1')
pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
```

**Gotchas** 陷阱

