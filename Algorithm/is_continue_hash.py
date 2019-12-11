#!/usr/bin/python
# -*- coding: utf-8 -*-

# 判断扑克牌是否是顺子
# 大小王为0，可以重复，其他数字不能重复


def is_continue_hash(numbers):
    cards = {}
    for num in numbers:
        if num == 0:
            continue
        if num in cards.keys():
            return False
        else:
            cards[num] = 1
    return True if max(cards.keys()) - min(cards.keys()) <= 4 else False

num = [0,3,0,9,4]
print(is_continue_hash(num))

