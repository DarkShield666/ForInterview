#!/usr/bin/python
# -*- coding: utf-8 -*-


# 删除列表里重复的数字，返回长度

class Solution(object):

    @staticmethod
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return len(nums)
        tmp = nums[0]
        index = 0
        for i, v in enumerate(nums):
            if tmp == v:
                continue
            else:
                nums[index] = tmp
                tmp = v
                index += 1
        nums[index] = tmp
        return len(nums[:index+1])


    @staticmethod
    def remove(nums):
        dic = {}
        for i in nums:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] = dic[i] + 1
        return dic


if __name__ == '__main__':
    num = [0,0,0,1,2,3,3,3,6]
    test = Solution()
    print(test.removeDuplicates(num))