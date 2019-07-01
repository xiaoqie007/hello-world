#### 学习内容
#### 用时30分钟
- 函数工具-迭代器（Iterator）

1. Python 中的所有容器，都是可迭代的

2. 对象转换成 “可迭代对象” 的 iter(); 例如，>>>L = iter(['item 1', 'item 2', 3, 5])，>>>type(L), list_iterator

3. next("可迭代对象")；注意：触发 StopIteration 错误

4. 迭代器是个 Object，所以，写迭代器的时候写的是 Class，比如，我们写一个数数的迭代器，Counter：可以用到__iter__(self) 和 __next__(self)。
