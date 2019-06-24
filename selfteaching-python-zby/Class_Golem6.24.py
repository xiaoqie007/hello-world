#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 10:16:45 2019

@author: liwei
"""

import datetime

#class Golem:
#    def __init__(self, name=None):
#        #注意 self 这个变量的定义是在def __init__(self, ...)这一句里完成的。
#        self.name = name
#        self.built_year = datetime.date.today().year
#        
#    def say_hi(self):
#        print('Hi')
#        
#g = Golem('Clay') #创建一个instance
#print(g.name) #之后解析器就去找 g 这个实例所在的 Scope 里面有没有 self.name
#print(g.built_year)
#print(g.say_hi)
#g.say_hi()
##
#print(type(g))
#print(type(g.name))
#print(type(g.built_year))
#print(type(g.__init__))
#print(type(g.say_hi))

#Running_Golem

class Golem:
    def __init__(self, name=None):
        #注意 self 这个变量的定义是在def __init__(self, ...)这一句里完成的。
        self.name = name
        self.built_year = datetime.date.today().year
        
    def say_hi(self):
        print('Hi')
class Running_Golem(Golem):
    def run(self):
        print("Can't you see? I'm running...")
    def say_hi(self): # you can overriding Methods in Parent Class
        print('Hey！Nice day, Huh?')
        
#rg = Running_Golem('Clay')
#print(rg.run)
#print(rg.run())
#print(rg.name)
#print(rg.built_year)
#print(rg.say_hi())


#Inspecting A Class
#1. help(object) 
#2. dir(object)
#3. object.__dict__
 
rg = Running_Golem('Clay')
help(rg)
print(dir(rg))
#print(rg.__init__)
print(hasattr(rg, 'built_year'))

#Scope
