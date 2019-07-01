#### 学习内容：
**Lecture 6: Recursion and Dictionaries(前半部分)**
#### 用时：40分钟

##### **WHAT IS RECURSION?**
1. Algorithmically:
a way to design solutions to problems by divide-and-conquer or decrease-and-conquer
- reduce a problem to simpler versions of the same problem		

2. Semantically:
a programming technique	where a	function	calls itself 
- in programming, goal is	to NOT have	infinite recursion	
- must have 1	or more	base cases that are easy to solve	
- must solve the same	problem	on some other input with the goal of simplifying the larger	problem	input

##### **Iteration Vs Recursion**


 ```Python
 def factorial_iter(n):
     prod = 1
     for i in range(i, n+1):
         prod += i
return prod
```

```Python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-)
```
- recurison may be simpler, more intuitive
- recurison may be efficient from programmer POV
- recurison may not be efficient from computer POV






