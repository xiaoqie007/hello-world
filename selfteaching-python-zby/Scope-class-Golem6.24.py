#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:01:47 2019

@author: liwei
"""
import datetime

# * `hasattr(object, attr)` 查询这个 `object` 中有没有这个 `attr`，返回布尔值
# * `getattr(object, attr)` 获取这个 `object` 中这个 `attr` 的值
# * `setattr(object, attr, value)` 将这个 `object` 中的 `attr` 值设置为 `value`

#class Golem:
#    population = 0
#    __life_span = 10
#    
#    def __init__(self, name=None):
#        self.name = name
#        self.built_year = datetime.date.today().year
#        self.__active = True
#        Golem.population += 1
#    
#    def say_hi(self):
#        print('Hi!')
#    
#    def cease(self):
#        self.__active = False
#        Golem.population -= 1          # 执行一遍之后，试试把这句改成 population += 1
#    
#    def is_active(self):
#        if datetime.date.today().year - self.built_year >= Golem.__life_span:
#            self.cease()
#        return self.__active
#
#g = Golem()
#print(hasattr(Golem, 'population')) #True
#print(hasattr(g, 'population')) #True
#print(hasattr(g,'__life_span')) #False
#print(hasattr(Golem,'__life_span')) #False
#print(hasattr(g, 'say_hi')) #True
#print(hasattr(g, 'is_active')) #True
#print(hasattr(g, '__active')) #False
#print(hasattr(g, 'built_year')) #True
#print(hasattr(g, 'name')) #True
#
#print(Golem.population) #1
#setattr(Golem, 'population', 10)
#print(Golem.population) #10
#
#x = Golem()
#print(Golem.population) #11
#x.cease()
#print(Golem.population) #10
#print(getattr(g, 'population')) #10
#print(g.is_active()) #True


#* ① `class Golem` 之外；
#* ② `class Golem` 之内；
#* ③ `__init__(self, name=None)` 之内；
#* ④ `cease(self)` 之内；

#把population这个变量也改成私有：__population,为从外查看变量增设个函数，返回那个值好了


class Golem:
    __population = 0
    __life_span = 10
    
    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year
        self.__active = True
        Golem.__population += 1
    
    def say_hi(self):
        print('Hi!')
    
    def cease(self):
        self.__active = False
        Golem.__population -= 1          # 执行一遍之后，试试把这句改成 population += 1
    
    def is_active(self):
        if datetime.date.today().year - self.built_year >= Golem.__life_span:
            self.cease()
        return self.__active
    @property
    def population(delf):
        return Golem.__population
    @population.setter
    def population(self, value):
        Golem.__population= value
g = Golem('Clay')
#g.population
#print(g.population())
#g.population = 100
help(Golem)
setattr(Golem, 'population', 10000)
print(g.population)

 