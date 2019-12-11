#!/usr/bin/python
# -*- coding: utf-8 -*-
# 只出现一次的数

class Solution:
    @staticmethod
    def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] = dic[i] + 1
        for k, v in dic.items():
            if v == 1:
                return k


if __name__ == '__main__':
    dic = [4,1,2,1,2]
    print(Solution.singleNumber(dic))

