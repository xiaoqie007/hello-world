### pandas官网学习
- Python Data Analysis Library
pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

pandas is a NumFOCUS sponsored project. This will help ensure the success of development of pandas as a world-class open-source project, and makes it possible to donate to the project.

Warning Starting with the 0.25.x series of releases, pandas only supports Python 3.5.3 and higher. See Plan for dropping Python 2.7 for more details.
Warning The minimum supported Python version will be bumped to 3.6 in a future release.
Warning Panel has been fully removed. For N-D labeled data structures, please use xarray
Warning read_pickle() and read_msgpack() are only guaranteed backwards compatible back to pandas version 0.20.3 (GH27082)


What’s new in 0.25.0 (July 18, 2019)¶

Warning：

*Panel has been fully removed. For N-D labeled data structures, please use **xarray** *

**Enhancements：**

Groupby aggregation with relabeling¶

- groupby

Pandas has added special groupby behavior, known as “named aggregation”, for naming the output columns when applying multiple aggregation functions to specific columns (GH18366, GH26512).

```python
>>> import pandas as pd
>>> 
>>> animals = pd.DataFrame({'kind':['cat','dog', 'cat', 'dog'],})
>>> animals = pd.DataFrame({'kind':['cat','dog', 'cat', 'dog'],
			    'height':[9.1, 6.0, 9.5, 34.0],
			    'weight':[7.9, 7.5, 9.9, 198.0]})
>>> animals
  kind  height  weight
0  cat     9.1     7.9
1  dog     6.0     7.5
2  cat     9.5     9.9
3  dog    34.0   198.0
>>> animals.groupby('kind').agg(
	min_height = pd.NameAgg(column='height',aggfunc='min'),
	max_height = pd.NameAgg(column='heght', aggfunc='max'),
	average_weight = pd.NameAgg(column='weight', aggfunc=np.mean),
	)
```

**MulitIndex**
pd.MultiIndex.from_product([['a', 'abc'], range(500)])


**Json normalize with max_level param support¶**
```python
>>> data = [{
	'CreatedBy': {'Name': 'Uaer001'},
	'Lookup':{'TextField':'Some text',
		  'UserField':{'Id':'ID001', 'Name':'Name001'}},
	'Image':{'a': 'b'}
	}]
	
>>> json_normalize(data, max_level= 1)
	
  CreatedBy.Name Lookup.TextField                    Lookup.UserField Image.a
0        Uaer001        Some text  {'Id': 'ID001', 'Name': 'Name001'}  
     b
>>> json_normalize(data, max_level= 2)
	
  CreatedBy.Name Lookup.TextField  ... Lookup.UserField.Name Image.a
0        Uaer001        Some text  ...               Name001       b

[1 rows x 5 columns]

>>> json_normalize(data, max_level= 3)
	
  CreatedBy.Name Lookup.TextField  ... Lookup.UserField.Name Image.a
0        Uaer001        Some text  ...               Name001       b

[1 rows x 5 columns]
```



**Series.explode to split list-like values to rows**

```python
>>> import pandas as pd
	
>>> df = pd.DataFrame([{'var1': 'a,b,c', 'var2': 1},
		       {'var1': 'd,e,f', 'var2':2}])
	
>>> df
	
    var1  var2
0  a,b,c     1
1  d,e,f     2
>>> df. assign(var1= df.var1.str.split(',')).explode('var1')
	
  var1  var2
0    a     1
0    b     1
0    c     1
1    d     2
1    e     2
1    f     2

>>> 
```
**Package overview**

pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python. Additionally, it has the broader goal of becoming the most powerful and flexible open source data analysis / manipulation tool available in any language. It is already well on its way toward this goal.


Here are just a few of the things that pandas does well:

The best way to think about the pandas data structures is as flexible containers for lower dimensional data. For example, DataFrame is a container for Series, and Series is a container for scalars. We would like to be able to insert and remove objects from these containers in a dictionary-like fashion.

Mutability and copying of data


**Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:**

```python
>>> datas = pd.date_range('20190701', periods = 6)
>>> datas
DatetimeIndex(['2019-07-01', '2019-07-02', '2019-07-03', '2019-07-04',
               '2019-07-05', '2019-07-06'],
              dtype='datetime64[ns]', freq='D')
>>> df = pd.DataFrame(np.random.randn(6, 4), index = datas, columns = list('ABCD'))
# np.random.randn(6, 4)  6列数个， 4行数个
>>> df
                   A         B         C         D
2019-07-01 -0.328337 -0.194976  0.467727 -1.097221
2019-07-02 -2.605594  0.207596 -0.764849  0.446691
2019-07-03  1.548134  1.265210 -1.146961 -0.336198
2019-07-04 -0.061891  1.241550 -0.715711 -0.216914
2019-07-05 -1.415277  1.673424 -0.778283  0.189490
2019-07-06  1.084922 -1.124417 -0.719880  0.632569
```

**Viewing data**
- df.head() 前
- df.tail() 后
- df.index 索引
- df.coulmns 列
- df.to_numpy() 

**difference between pandas and NumPy: NumPy arrays have one dtype for the entire array, while pandas DataFrames have one dtype per column.**

**Note：** DataFrame.to_numpy() does not include the index or column labels in the output.

- df.describe() 显示快速统计摘要
- df.T 转换你的数据

**Sorting by an axis:** axis轴
- df.sort_index(axis=1, ascending=False) 按轴排序

**上次调取的btc数据可以用df.sort_index(ascending = 0)把索引倒序排列
axis = 1 可以把列（columns）倒序排列**

**Sorting by values:**

- df.sort_values(by='B')

**Selection**

> **Note While standard Python / Numpy expressions for selecting and setting are intuitive and come in handy for interactive work, for production code, we recommend the optimized pandas data access methods, .at, .iat, .loc and .iloc.**

**Getting**

- df[]

df['A'], df[:3], df[3:9] ,A是columns， ：3， 3:9 是索引

**Selection by label 按标签选择**
For getting a cross section using a label:

**df.loc[dates[0]]**

Selecting on a multi-axis by label:按标签选择多轴

**df.loc[:, ['A', 'B']]**

Showing label slicing, both endpoints are included:显示标签切片，包括两个端点。

**df.loc['20130102':'20130104', ['A', 'B']]**

Reduction in the dimensions of the returned object:
减少返回对象的尺寸

**df.loc['20130102', ['A', 'B']]**

For getting a scalar value:获取标量值

For getting fast access to a scalar (equivalent to the prior method): 快速访问标量

**df.at[dates[0], 'A']**

Select via the position of the passed integers:通过传入整数的位置选择
**df.iloc[3]**

By integer slices, acting similar to numpy/python: 通过整数切片

**df.iloc[3:5, 0:2]**

By lists of integer position locations, similar to the numpy/python style:通过整数位置列表

**df.iloc[[1,2,4], [0,2]]**

For slicing rows explicitly: 明确的切片行

**df.iloc[1:3, :]**

For slicing columns explicitly:

**df.iloc[:, 1:3]**

For getting a value explicitly:

**df.iloc[1,1]**

For getting fast access to a scalar (equivalent to the prior method):

**df.iat[1,1]**





### **Boolean indexing**

Using a single column’s values to select data.
使用单个列的值来选择数据
**df[df.A > 0]**

Selecting values from a DataFrame where a boolean condition is met.

**df[df > 0]**

Using the isin() method for filtering: 使用 isin 方法过滤。
- df[df > 0]


```python
#Using the isin() method for filtering:
  df2 = df.copy()
  df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
 
  df2[df2['E'].isin(['two', 'four'])]















