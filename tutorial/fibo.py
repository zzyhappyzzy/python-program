# -*- coding: utf_8 -*-
# coding refer: https://docs.python.org/3/library/codecs.html#module-codecs
# python version: 3.6+
#
# fibo.py
#
# Created by zhenzhaoyang on 2018/2/7.
# Copyright © 2018年 zhenchy. All rights reserved.
#
# Github: https://github.com/zzyhappyzzy
# Blog:   http://zyoung.me
#

# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

def _private_method1():
    print("this is private method1")

def public_method1():
    print("this is public method1")


# 结尾加上以下代码(if __name__ == "__main__":)，支持将python文件作为脚本执行;
# eg: python fibo.py 50  ====> 1 1 2 3 5 8 13 21 34
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
