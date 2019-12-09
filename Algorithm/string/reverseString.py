#!/usr/bin/python
# -*- coding: utf-8 -*-

# 字符串反转


class Solution:
    @staticmethod
    def reverseString(s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        s2 = ''
        while n > 0:
            s2 = s2 + s[n-1]
            n = n - 1
        print(s2)


if __name__ == '__main__':
    s = '"hello"'
    Solution.reverseString("\"ha ni SB uy\"")
    Solution.reverseString(s)
