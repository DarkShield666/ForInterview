#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy

a = ('1', '2', '3')
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
print(b, c, d)
print(id(b), id(c), id(d))

q = ['a', 'b', 'c']
w = q
e = copy.copy(q)
r = copy.deepcopy(q)
print(w, e, r)
print(id(w), id(e), id(r))

h = 5
i = h
j = copy.copy(h)
k = copy.deepcopy(h)
print(i, j, k)
print(id(i), id(j), id(k))

'''
('1', '2', '3') ('1', '2', '3') ('1', '2', '3')
4349233768 4349233768 4349233768
['a', 'b', 'c'] ['a', 'b', 'c'] ['a', 'b', 'c']
4349262344 4349262216 4349263816
5 5 5
4304951808 4304951808 4304951808


可变对象和不可变对象
可变对象：列表和字典，创建完之后可以改变的对象
不可变对象：一旦创建就不可修改的对象，元祖，字符串，数字
'''
