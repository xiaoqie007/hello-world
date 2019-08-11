1.4 安装和设置
由于人们用Python所做的事情不同，所以没有一个普适的Python及其插件包的安装方案。由于许多读者的Python科学计算环境都不能完全满足本书的需要，所以接下来我将详细介绍各个操作系统上的安装方法。我推荐免费的Anaconda安装包。写作本书时，Anaconda提供Python 2.7和3.6两个版本，以后可能发生变化。本书使用的是Python 3.6，因此推荐选择Python 3.6或更高版本。

Windows
要在Windows上运行，先下载Anaconda安装包。推荐跟随Anaconda下载页面的Windows安装指导，安装指导在写作本书和读者看到此文的的这段时间内可能发生变化。

现在，来确认设置是否正确。打开命令行窗口（cmd.exe），输入python以打开Python解释器。可以看到类似下面的Anaconda版本的输出：

C:\Users\wesm>python
Python 3.5.2 |Anaconda 4.1.1 (64-bit)| (default, Jul  5 2016, 11:41:13)
[MSC v.1900 64 bit (AMD64)] on win32
>>>
要退出shell，按Ctrl-D（Linux或macOS上），Ctrl-Z（Windows上），或输入命令exit()，再按Enter。

Apple (OS X, macOS)
下载OS X Anaconda安装包，它的名字类似Anaconda3-4.1.0-MacOSX-x86_64.pkg。双击.pkg文件，运行安装包。安装包运行时，会自动将Anaconda执行路径添加到.bash_profile文件，它位于/Users/$USER/.bash_profile。

为了确认成功，在系统shell打开IPython：

$ ipython
要退出shell，按Ctrl-D，或输入命令exit()，再按Enter。

GNU/Linux
Linux版本很多，这里给出Debian、Ubantu、CentOS和Fedora的安装方法。安装包是一个脚本文件，必须在shell中运行。取决于系统是32位还是64位，要么选择x86 (32位)或x86_64 (64位)安装包。随后你会得到一个文件，名字类似于Anaconda3-4.1.0-Linux-x86_64.sh。用bash进行安装：

$ bash Anaconda3-4.1.0-Linux-x86_64.sh
笔记：某些Linux版本在包管理器中有满足需求的Python包，只需用类似apt的工具安装就行。这里讲的用Anaconda安装，适用于不同的Linux安装包，也很容易将包升级到最新版本。

接受许可之后，会向你询问在哪里放置Anaconda的文件。我推荐将文件安装到默认的home目录，例如/home/$USER/anaconda。

Anaconda安装包可能会询问你是否将bin/目录添加到$PATH变量。如果在安装之后有任何问题，你可以修改文件.bashrc（或.zshrc，如果使用的是zsh shell）为类似以下的内容：

export PATH=/home/$USER/anaconda/bin:$PATH
做完之后，你可以开启一个新窗口，或再次用~/.bashrc执行.bashrc。

**安装或升级Python包**
在你阅读本书的时候，你可能想安装另外的不在Anaconda中的Python包。通常，可以用以下命令安装：

- conda install package_name
如果这个命令不行，也可以用pip包管理工具：

- pip install package_name
你可以用conda update命令升级包：

- conda update package_name
pip可以用--upgrade升级：

- **pip install --upgrade package_name**
本书中，你有许多机会尝试这些命令。
 ```python
 #pip insatll --upgrade package_name
 ```

- 注意：当你使用conda和pip二者安装包时，千万不要用pip升级conda的包，这样会导致环境发生问题。当使用Anaconda或Miniconda时，最好首先使用conda进行升级。

Python 2 和 Python 3

第一版的Python 3.x出现于2008年。它有一系列的变化，与之前的Python 2.x代码有不兼容的地方。因为从1991年Python出现算起，已经过了17年，Python 3 的出现被视为吸取一些列教训的更优结果。

2012年，因为许多包还没有完全支持Python 3，许多科学和数据分析社区还是在使用Python 2.x。因此，本书第一版使用的是Python 2.7。现在，用户可以在Python 2.x和Python 3.x间自由选择，二者都有良好的支持。

但是，Python 2.x在2020年就会到期（包括重要的安全补丁），因此再用Python 2.7就不是好的选择了。因此，本书使用了Python 3.6，这一广泛使用、支持良好的稳定版本。我们已经称Python 2.x为“遗留版本”，简称Python 3.x为“Python”。我建议你也是如此。

本书基于Python 3.6。你的Python版本也许高于3.6，但是示例代码应该是向前兼容的。一些示例代码可能在Python 2.7上有所不同，或完全不兼容。

集成开发环境（IDEs）和文本编辑器
当被问到我的标准开发环境，我几乎总是回答“IPython加文本编辑器”。我通常在编程时，反复在IPython或Jupyter notebooks中测试和调试每条代码。也可以交互式操作数据，和可视化验证数据操作中某一特殊集合。在shell中使用pandas和NumPy也很容易。

但是，当创建软件时，一些用户可能更想使用特点更为丰富的IDE，而不仅仅是原始的Emacs或Vim的文本编辑器。以下是一些IDE：

PyDev（免费），基于Eclipse平台的IDE；

JetBrains的PyCharm（商业用户需要订阅，开源开发者免费）；

Visual Studio（Windows用户）的Python Tools；

Spyder（免费），Anaconda附带的IDE；

Komodo IDE（商业）。

因为Python的流行，大多数文本编辑器，比如Atom和Sublime Text 3，对Python的支持也非常好。

1.5 社区和会议
除了在网上搜索，各式各样的科学和数据相关的Python邮件列表是非常有帮助的，很容易获得回答。包括：

pydata：一个Google群组列表，用以回答Python数据分析和pandas的问题；

pystatsmodels： statsmodels或pandas相关的问题；

scikit-learn和Python机器学习邮件列表，scikit-learn@python.org；

numpy-discussion：和NumPy相关的问题；

scipy-user：SciPy和科学计算的问题；

因为这些邮件列表的URLs可以很容易搜索到，但因为可能发生变化，所以没有给出。

每年，世界各地会举办许多Python开发者大会。如果你想结识其他有相同兴趣的人，如果可能的话，我建议你去参加一个。许多会议会对无力支付入场费和差旅费的人提供财力帮助。下面是一些会议：

PyCon和EuroPython：北美和欧洲的两大Python会议；

SciPy和EuroSciPy：北美和欧洲两大面向科学计算的会议；

PyData：世界范围内，一些列的地区性会议，专注数据科学和数据分析；

国际和地区的PyCon会议（http://pycon.org有完整列表） 。

1.6 本书导航
如果之前从未使用过Python，那你可能需要先看看本书的第2章和第3章，我简要介绍了Python的特点，IPython和Jupyter notebooks。这些知识是为本书后面的内容做铺垫。如果你已经掌握Python，可以选择跳过。

接下来，简单地介绍了NumPy的关键特性，附录A中是更高级的NumPy功能。然后，我介绍了pandas，本书剩余的内容全部是使用pandas、NumPy和matplotlib处理数据分析的问题。我已经尽量让全书的结构循序渐进，但偶尔会有章节之间的交叉，有时用到的概念还没有介绍过。

尽管读者各自的工作任务不同，大体可以分为几类：

与外部世界交互

阅读编写多种文件格式和数据存储；

数据准备

清洗、修改、结合、标准化、重塑、切片、切割、转换数据，以进行分析；

转换数据

对旧的数据集进行数学和统计操作，生成新的数据集（例如，通过各组变量聚类成大的表）；

建模和计算

将数据绑定统计模型、机器学习算法、或其他计算工具；

展示

创建交互式和静态的图表可视化和文本总结。

代码示例
本书大部分代码示例的输入形式和输出结果都会按照其在IPython shell或Jupyter notebooks中执行时的样子进行排版：

In [5]: CODE EXAMPLE
Out[5]: OUTPUT
但你看到类似的示例代码，就是让你在in的部分输入代码，按Enter键执行（Jupyter中是按Shift-Enter）。然后就可以在out看到输出。

示例数据
各章的示例数据都存放在GitHub上：http://github.com/pydata/pydata-book。 下载这些数据的方法有二：使用git版本控制命令行程序；直接从网站上下载该GitHub库的zip文件。如果遇到了问题，可以到我的个人主页，http://wesmckinney.com/， 获取最新的指导。

为了让所有示例都能重现，我已经尽我所能使其包含所有必需的东西，但仍然可能会有一些错误或遗漏。如果出现这种情况的话，请给我发邮件：wesmckinn@gmail.com。报告本书错误的最好方法是O’Reilly的errata页面，http://www.bit.ly/pyDataAnalysis_errata。​

引入惯例
Python社区已经广泛采取了一些常用模块的命名惯例：

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels as sm
也就是说，当你看到np.arange时，就应该想到它引用的是NumPy中的arange函数。这样做的原因是：在Python软件开发过程中，不建议直接引入类似NumPy这种大型库的全部内容（from numpy import *）。

行话
由于你可能不太熟悉书中使用的一些有关编程和数据科学方面的常用术语，所以我在这里先给出其简单定义：

数据规整（Munge/Munging/Wrangling） 指的是将非结构化和（或）散乱数据处理为结构化或整洁形式的整个过程。这几个词已经悄悄成为当今数据黑客们的行话了。Munge这个词跟Lunge押韵。

伪码（Pseudocode） 算法或过程的“代码式”描述，而这些代码本身并不是实际有效的源代码。

语法糖（Syntactic sugar） 这是一种编程语法，它并不会带来新的特性，但却能使代码更易读、更易写。


```python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels as sm

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels as sm
```
Munge

Pseudocode

Syntactic sugar

行话
由于你可能不太熟悉书中使用的一些有关编程和数据科学方面的常用术语，所以我在这里先给出其简单定义：

数据规整（Munge/Munging/Wrangling） 指的是将非结构化和（或）散乱数据处理为结构化或整洁形式的整个过程。这几个词已经悄悄成为当今数据黑客们的行话了。Munge这个词跟Lunge押韵。

伪码（Pseudocode） 算法或过程的“代码式”描述，而这些代码本身并不是实际有效的源代码。

语法糖（Syntactic sugar） 这是一种编程语法，它并不会带来新的特性，但却能使代码更易读、更易写。


