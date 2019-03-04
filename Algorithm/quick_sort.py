#!/usr/bin/python
# -*- coding: utf-8 -*-

# 快排
# 选中序列第一个元素，运用递归将比第一个元素小的放在左边，比第一个元素大的放在右边


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        index = 0
        m = array[index]
        left = [i for i in array[index+1:] if i <= m]
        right = [i for i in array[index+1:] if i > m]
        return quick_sort(left) + [m] + quick_sort(right)


ll = [5,6,1,3,13,3,6,7,2,6]
print(quick_sort(ll))