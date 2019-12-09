#!/usr/bin/python
# -*- coding: utf-8 -*-

# 给一个数组，求数组里的最小值的下标


def min_index(list: list):
    if len(list) == 0:
        return
    else:
        x = min(list)
        result = []
        for i in range(len(list)):
            if list[i] == x:
                result.append(i)
        return result


if __name__ == '__main__':
    a = [3,2,1,5,7,9,1,4,1,5]
    r = min_index(a)
    print(r)