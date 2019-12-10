#!/usr/bin/python
# -*- coding: utf-8 -*-

# yield生成器 不阻断循环进行，一个一个返回


def func1():
    for i in range(1, 5):
        return i


def func2():
    for m in range(1, 5):
        yield m


print(func1())   # 1
print(func2())   # <generator object func2 at 0x1033eb0a0>


yi = func2()
print(type(yi))  # <class 'generator'>
for i in yi:
    print(i)


'''
1
2
3
4
'''