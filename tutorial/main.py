# -*- coding: utf_8 -*-
# coding refer: https://docs.python.org/3/library/codecs.html#module-codecs
# python version: 3.6+
#
# main.py
#
# Created by zhenzhaoyang on 2018/2/7.
# Copyright © 2018年 zhenchy. All rights reserved.
#
# Github: https://github.com/zzyhappyzzy
# Blog:   http://zyoung.me
#

# Comment
the_world_is_fat = True
if the_world_is_fat:
    print("Be careful not to fall off!")

a = 1 #this is the comment
#this is another comment
text = "# This is not a comment because it's inside quotes."
print(text)

# Operation
a = 2
b = 5
sum = a + b
div = 2 / 5   # division always returns a floating point number
divInt = 5 // 2 # division can get an integer result with operator //
print(a,"+",b,"=",sum)
print(div)
print(divInt)

squared = 5 ** 2 # 5 squared
print(squared)
powers = 2 ** 5 # 2 to the power of 7
print(powers)

# String
print("C:\some\name")  # \n被解释为换行符
print(r"C:\some\name") # 字符串前加r指明\不做转义处理

print("""\
    Usage: thingy [OPTIONS]
    -h                        Display this usage message
    -H hostname               Hostname to connect to
    """)

str = 3 * "un" + "ium"
print(str) # 3 times 'un', followed by 'ium'

# 相邻的字符串会自动拼接(仅限字符串，不支持变量和字符串<可用+拼接变量等>)
print("Py" "thon")
text = ("Put several strings within parentheses "
        "to have them joined together.")
print(text)

prefix = "Py"
print(prefix + "thon")

word = "Python"
print(word[0]) # 从左到右，起始为0
print(word[-1]) # 从右到左，起始位-1
print(word[0:2]) # [0-2)区间
print(word[0:]) # >=0
print(word[:7]) # <7

s = "supercalifragilisticexpialidocious"
print(len(s))

# List
arr = [1, 4, 9, 16, 25];
print(arr)
print(arr[0])
print(arr[-1])

arr += [36, 49, 64, 81, 100]
print(arr)

cubes = [1, 8, 27, 65, 125]  # something's wrong here
cubes[3] = 4 ** 3  # change list item value
print(cubes)
cubes.append(6 ** 3);
cubes.append(7 ** 3);
print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E'] # replace some values
print(letters)
print("the length of letters is ", len(letters))
letters[2:5] = [] # now remove them
print(letters)
letters[:] = [] # clear the list by replacing all the elements with an empty list
print(letters)

#Simple program (eg: Fibonacci issue)
a, b = 0, 1  # a = 0, b = 1
while b < 10:
    print(b)
    a, b = b, a+b


a = 80
if a < 60:
    print("D")
elif a < 70:
    print("C")
elif a < 80:
    print("B")
else:
    print("A")


words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

#copy list words[:]: for imute lists
for w in words[:]:
    if w == "window":
        words.insert(0,'the first')
print(words)

for i in range(5):
    print(i)

for i in range(5, 10):
    print(i)

#[0, 10) 每次增加3
for i in range(0, 10, 3):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# print(list(enumerate(a)))

b = list(range(5))
print(b)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# function
def fib(n):
    x, y = 1, 1
    while x < n:
        print(x, end=" ")
        x, y = y, x+y
    print()

fib(2000)


def sumExp(a, b, prompt=False, returnValue=False):
    sum = a + b
    if prompt:
        print(a,"+",b,"=",sum)
    if returnValue:
        return sum

print(sumExp(1, 2))
print(sumExp(1, 2, True))
print(sumExp(1, 2, True, True))

def concat(*args, sep="/"):
    """
    Documentation Strings
    """
    return sep.join(args)

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep = "."))

# Data Structures
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.index('banana'))
fruits.reverse()
print(fruits)
fruits.append('grape')
fruits.sort()
print(fruits)
print(fruits.pop())
print(fruits)

# 队列
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())
print(queue)

# 数组合成
squares = [x**2 for x in range(10)]
print(squares)

from math import pi
pi_arr = [round(pi, i) for i in range(1, 6)]
print(pi_arr)

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a

t = 12, 15, "great"
print(t)

a = set("abcadea")
print(a)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

del tel['sape']
tel['irv'] = 4127
print(tel)
all_keys = list(tel.keys())
print(all_keys)
guidoIn = 'guido' in tel
print(guidoIn)
jack_not_in = 'jack' not in tel
print(jack_not_in)

#dict()
dic1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dic2 = dict(sape=4139, guido=4127, jack=4098)
print(dic1,'\n',dic2)

#items()
for k, v in dic1.items():
    print(k, v)

#zip()
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0} ? It is {1}.'.format(q, a))

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

# Modules

# import all names
import fibo
fibo.fib(1000)
print(fibo.fib2(1000))
print(fibo.__name__)
fib = fibo.fib
fib(500)
fibo._private_method1()

# import particular names
from fibo import fib, fib2
fib(500)

# imports all names except those beginning with an underscore (_)
from fibo import *
fib(500)
public_method1()

# Module search path
import sys
print(sys.path)
# We can modify module search path using standard list operations:
sys.path.append('/ufs/guido/lib/python')
print(sys.path)

print(dir(fibo))

# File (关键词with可以在操作完文件后自动关闭文件，无需手动调用close函数)
import os

test_file_name = "test.txt"
if os.path.exists(test_file_name):
    print("file",test_file_name,"exit")
    with open(test_file_name, "a") as f:
         f.write("\nJust insert some text")
else:
    print("file",test_file_name,"not exit")
    with open(test_file_name, "a+") as f:
        f.write("First line")

if f.closed:
    print("file close auto")

with open(test_file_name) as f:
    read_data = f.read()
print(read_data)

# Exceptions
try:
    a = 5 / 0
except Exception as inst:
    print("exception type ",type(inst)," and args is ",inst.args)
else:
    print("no exception and continue")
finally:
    print("execute finally clause")


# Scope (global ===> Module   nonlocal ===> Scope)
def scope_test():
    def do_local():
        spam = "local spam"
    
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

# Class
class Animal:
    """A simple example class"""
    tricks = []   # mistaken use of a class variable , shared by all instance (所有实例共用）直接在func里使用就好
    
    def __init__(self, name="Jack", gender=1):
        self.age = 8;
        self.name = name
        self.gender = gender

    def eat(self):
        print("hungry and eat something")

animal0 = Animal()
print("age:",animal0.age,"name:",animal0.name,"gender:",animal0.gender)
animal1 = Animal("Tom", 2)
print("age:",animal1.age,"name:",animal1.name,"gender:",animal1.gender)

animal1.age = 18
print(animal1.age)
del animal1.age
animal1.eat()
print(animal1.__doc__)


# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
    
    def g(self):
        return 'hello world'
    
    h = g

c = C()
print(c.f(2, 5),c.h())


# Inheritance 继承
class Demo(Animal, C):
    def g(self, text="11"):
        return 'overide hello world ' + text

demo = Demo()
print(demo.g())
demo.eat()

























