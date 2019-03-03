#!/usr/bin/python
# -*- coding: utf-8 -*-

# a *args **kwargs


def func(a, *args, **kwargs):
    print(type(a), type(args), type(kwargs))
    print(a, args, kwargs)


func(1, 2, 3)
func('string', 2, 3, b=3, cc=5)

'''
可变参数列表类型如图，而且参数类型必须按 a args kwargs顺序
'''