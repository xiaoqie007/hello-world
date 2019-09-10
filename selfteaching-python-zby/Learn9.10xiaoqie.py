#python 统计list中各个元素出现的次数

#利用Python字典统计
#利用Python的collection包下Counter的类统计
#利用Python的pandas包下的value_counts的类统计


import numpy as np
rolls = np.random.randint(low= 1, high= 5, size = 20)
lst = list(rolls)
print(lst)

#方法一：利用字典dict来完成统计
dict = {}
for key in lst:
    dict[key] = dict.get(key, 0) +1
#print(dict)
#扩展排序：python的sorted函数对字典按key排序和按value排序
#sorted(iterable,key,reverse)，
#iterable是一个可迭代的对象，例如可以是dict.items()、dict.keys()等；key是key是一个函数，用来选取参与比较的元素，
#reverse则是用来指定排序是倒序还是顺序，reverse=true则是倒序，reverse=false时则是顺序，默认时reverse=false。

#要按key值对字典排序，则可以使用如下语句：
sorted(dict.keys()) #sorted(dict.keys(), reverse = True)
#sorted函数按value值对字典排序
sorted(dict.items(), key= lambda item: item[1], reverse= True)
#>>>dict = {1: 4, 2: 5, 3: 2, 4: 6, 5: 3}
#>>>
# 这里的dict.items()实际上是将dict转换为可迭代对象，
# 迭代对象的元素为（‘1’,4）、（‘2’,5）、（‘3’,2）、（‘4’,6），items()方法将字典的元素转化为了元组，
# 而这里key参数对应的lambda表达式的意思则是选取元组中的第二个元素作为比较参数（如果写作key=lambda item:item[0]的话
# 则是选取第一个元素作为比较对象，也就是key值作为比较对象。
# lambda x:y中x表示输出参数，y表示lambda函数的返回值），所以采用这种方法可以对字典的value进行排序。
# 注意排序后的返回值是一个list，而原字典中的名值对被转换为了list中的元组。
# >>>[(4, 6), (2, 5), (1, 4), (5, 3), (3, 2)]

#方法二：利用Python的collection包下Counter的类
from collections import Counter
result = Counter(lst)
print(result)


#方法三：Python的pandas包下的value_counts方法

import pandas as pd

result = pd.value_counts(lst)
print(result)