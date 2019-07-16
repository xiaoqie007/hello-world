**while**
```python
import random

number = random.randint(1,101)

guess = 0

print('*'*30)

while True:
    num_input = input('请输入1到100任一个数：')
    guess += 1
    if not num_input.isdigit():
        print("Please input interger.")
    elif int(num_input) < 0 or int(num_input) >= 100:
        print('The number should be in 1 to 100.')
    else:
        if number == int(num_input):
            print('不错不错！，猜了%d次,您猜对了！'%guess)
            break
        elif number > int(num_input):
            print("您猜小了！\n哈哈 ")
        elif number < int(num_input):
            print("您猜大了！\n哈哈" )
        else:
            print("There is something bad, I will not work")

    print("*"*30)
```
**请牢记：任何用户输入的内容都是不可靠的。**

- **break和continue**
- **while...else**:
   - 一遇到else了，就意味着已经不在while循环内了。
- **for...else**
   - 这个循环也通常用在当跳出循环之后要做的事情。
```python
from math import sqrt#开方
for n in range(99, 1, -1):
    root = sqrt(n) #root开方根<class 'float'> or <class 'int'>
    if root == int(root):
        print (n)
        break
else:
    print('Nothing.')
```
### **重要**
>阅读代码是一个提升自己编程水平的好方法。如何阅读代码？像看网上新闻那样吗？一目只看自己喜欢的文字，甚至标题看不完就开始喷。
绝对不是这样，如果这样，不是阅读代码呢。

>**阅读代码的最好方法是给代码做注释。** *对，如果可能就给每行代码做注释。这样就能理解代码的含义了。*

**用open()打开文件，可以有不同的模式打开:**
1. r以读方式打开文件，可读取文件信息。(默认)
2. "w":以写方式打开文件，可向文件写入信息。如文件存在，则清空该文件，再写入新内容

3. "a":以追加模式打开文件（即一打开文件，文件指针自动移到文件末尾），如果文件不存在则创建
4. 使用**with**
```python
>>> with open('131.txt', 'a') as f:
	f.write("\nThis is about 'with...as...'")	
29
>>> with open("131.txt", 'r') as f:
	print(f.read())
	
This is a file ,/dnext is other file.
Aha, I like program
This is about 'with...as...'
```

**提示：养成一个好习惯**，只要打开文件，不用该文件了，就一定要随手关闭它。如果不关闭它，它还驻留在内存中，后面又没有对它的操作，是不是浪费内存空间了呢？同时也增加了文件安全的风险。

**read/readline/readlines**
- **read**：如果指定了参数size，就按照该指定长度从文件中读取内容，否则，就读取全文。被读出来的内容，全部塞到一个字符串里面。这样有好处，就是东西都到内存里面了，随时取用，比较快捷；“成也萧何败萧何”，也是因为这点，如果文件内容太多了，内存会吃不消的。文档中已经提醒注意在“non-blocking”模式下的问题，关于这个问题，不是本节的重点，暂时不讨论。
- **readline**：那个可选参数size的含义同上。它则是以行为单位返回字符串，也就是每次读一行，依次循环，如果不限定size，直到最后一个返回的是空字符串，意味着到文件末尾了(EOF)。
- **readlines**：size同上。它返回的是以行为单位的列表，即相当于先执行readline()，得到每一行，然后把这一行的字符串作为列表中的元素塞到一个列表中，最后将此列表返回




**读很大的文件**
 - 如果文件太大，就不能用read()或者readlines()一次性将全部内容读入内存，可以使用while循环和readlin()来完成这个任务。
 - 还有一个方法：fileinput模块
 ```python
>>> import fileinput
>>> for line in fileinput.input('/Users/liwei/Documents/Others/something.txt'):
	print(line)	

从明天起，做一个幸福的人
喂马，劈柴，周游世界
从明天起，关心粮食，蔬菜和水果
......
```
- **seek**
 这个函数的功能就是让指针移动。特别注意，它是以字节为单位进行移动的
 seek(...) seek(offset[, whence]) -> None. Move to new file position.
 ```
 Argument offset is a byte count. Optional argument whence defaults to 0 (offset from start of file, offset should be >= 0); other values are 1 (move relative to current position, positive or negative), and 2 (move relative to end of file, usually negative, although many platforms allow seeking beyond the end of a file). If the file is opened in text mode, only offsets returned by tell() are legal. Use of other offsets causes undefined behavior. Note that not all file objects are seekable.
 ```
 whence的值：

默认值是0，表示从文件开头开始计算指针偏移的量（简称偏移量）。这是offset必须是大于等于0的整数。
是1时，表示从当前位置开始计算偏移量。offset如果是负数，表示从当前位置向前移动，整数表示向后移动。
是2时，表示相对文件末尾移动。

>**loop**    **iterate**    **traversal**    **recursion**  

- 循环（loop），指的是在满足条件的情况下，重复执行同一段代码。比如，while语句。
- 迭代（iterate），指的是按照某种顺序逐个访问列表中的每一项。比如，for语句。
- 递归（recursion），指的是一个函数不断调用自身的行为。比如，以编程方式输出著名的斐波纳契数列。
- 遍历（traversal），指的是按照一定的规则访问树形结构中的每个节点，而且每个节点都只访问一次。

