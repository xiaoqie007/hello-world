NumPy基础：数组和矢量计算
NumPy的部分功能如下：
ndarray，一个具有矢量算术运算和复杂广播能力的快速且节省空间的多维数组。
用于对整组数据进行快速运算的标准数学函数（无需编写循环）。
用于读写磁盘数据的工具以及用于操作内存映射文件的工具。
线性代数、随机数生成以及傅里叶变换功能。
用于集成由C、C++、Fortran等语言编写的代码的A C API。

对于大部分数据分析应用而言，我最关注的功能主要集中在：
用于数据整理和清理、子集构造和过滤、转换等快速的矢量化数组运算。
常用的数组算法，如排序、唯一化、集合运算等。
高效的描述统计和数据聚合/摘要运算。
用于异构数据集的合并/连接运算的数据对齐和关系型数据运算。
将条件逻辑表述为数组表达式（而不是带有if-elif-else分支的循环）。
数据的分组运算（聚合、转换、函数应用等）。。

NumPy之于数值计算特别重要的原因之一，是因为它可以高效处理大数组的数据。这是因为：
NumPy是在一个连续的内存块中存储数据，独立于其他Python内置对象。NumPy的C语言编写的算法库可以操作内存，而不必进行类型检查或其它前期工作。比起Python的内置序列，NumPy数组使用的内存更少。
NumPy可以在整个数组上执行复杂的计算，而不需要Python的for循环。

```python
In [1]: import numpy as np                                         

In [2]: my_arr= np.arange(1000000)                                 

In [3]: my_list= list(range(1000000))                              

In [4]: %time for _ in range(10): my_arr2 = my_arr * 2             
CPU times: user 19.5 ms, sys: 12.4 ms, total: 31.9 ms
Wall time: 29.8 ms

In [5]:  %time for _ in range(10): my_list2 = [x * 2 for x in my_list]       
CPU times: user 681 ms, sys: 184 ms, total: 866 ms
Wall time: 871 ms

In [6]:  
```

#基于NumPy的算法要比纯Python快10到100倍（甚至更快），并且使用的内存更少。



- NumPy一元函数对ndarray中的数据执行元素级运算的函数

np.abs(x)、np.fabs(x) ： 计算数组各元素的绝对值

np.sqrt(x) ： 计算数组各元素的平方根

np.square(x) ： 计算数组各元素的平方

np.log(x) 、np.log10(x)、np.log2(x) ： 计算数组各元素的自然对数、10底对数和2底对数

np.ceil(x) 、np.floor(x) ： 计算数组各元素的ceiling值或floor值
 ———————————————— 
np.rint(x) ： 计算数组各元素的四舍五入值
np.modf(x) ： 将数组各元素的小数和整数部分以两个独立数组形式返回
np.cos(x)、 np.cosh(x)、np.sin(x)、 np.sinh(x)、np.tan(x) 、np.tanh(x) ： 计算数组各元素的普通型和双曲型三角函数
np.exp(x) ： 计算数组各元素的指数值
np.sign(x) ： 计算数组各元素的符号值，1(+), 0, ‐1(‐)
 ———————————————— 
版权声明：本文为CSDN博主「brucewong0516」的原创文章，遵循CC 4.0 by-sa版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/brucewong0516/article/details/79186176