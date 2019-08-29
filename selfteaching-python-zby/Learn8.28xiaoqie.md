
### 将条件逻辑表述为数组运算

```python
In [92]: xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])                                  

In [93]: yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])                                  

In [94]: cond = np.array([True, False, True, True, False])                           

In [95]: result = [(x if c else y) for x, y,c in zip(xarr, yarr, cond)]              

In [96]: result                                                                      
Out[96]: [1.1, 2.2, 1.3, 1.4, 2.5]

In [97]: result= np.where(cond, xarr, yarr)                                          

In [98]: result                                                                      
Out[98]: array([1.1, 2.2, 1.3, 1.4, 2.5])

```

In [99]: arr = np.random.randn(4, 4)                                                 

In [100]: arr                                                                        
Out[100]: 
array([[ 1.50273208, -0.96131353, -1.05022908, -1.5567827 ],
       [ 1.05921788, -0.38584439,  0.00645908,  0.66149963],
       [ 0.11627404,  1.64675517,  0.85854393, -1.98831147],
       [ 1.03119828, -0.67670691,  1.53448313,  2.17968952]])

In [101]: arr > 0                                                                    
Out[101]: 
array([[ True, False, False, False],
       [ True, False,  True,  True],
       [ True,  True,  True, False],
       [ True, False,  True,  True]])

**np.where** np.where(条件， 数组1， 数组2)

- np.where(cond, xarr, yarr)



In [104]: np.where(arr > 0, 2, arr)  #用常数2替换arr中所有正的值：
                                                
Out[104]: 
array([[ 2.        , -0.96131353, -1.05022908, -1.5567827 ],
       [ 2.        , -0.38584439,  2.        ,  2.        ],
       [ 2.        ,  2.        ,  2.        , -1.98831147],
       [ 2.        , -0.67670691,  2.        ,  2.        ]])

