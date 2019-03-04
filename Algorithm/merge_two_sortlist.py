#!/usr/bin/python
# -*- coding: utf-8 -*-

# 合并两个有序数组


def merge_two_sort_list(sortlist_a, sortlist_b):
    a = b = 0
    new_list = []
    while a < len(sortlist_a) and b < len(sortlist_b):
        if sortlist_a[a] < sortlist_b[b]:
            new_list.append(sortlist_a[a])
            a += 1
        else:
            new_list.append(sortlist_b[b])
            b += 1

    if a < len(sortlist_a):
        new_list.extend(sortlist_a[a:])
    else:
        new_list.extend(sortlist_b[b:])
    return new_list


a = [3,5,6,6,9]
b = [1,2,4,5,6,7,8,9]

print(merge_two_sort_list(a,b))

