#!/usr/bin/python
# -*- coding: utf-8 -*-


# 最长公共前缀

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) <= 1:
        print(len(strs))
        return ""

    ex = strs[0]
    for i in range(len(strs)):
        while strs[i].find(ex, 0) != 0:
            ex = ex[0:len(ex) - 1]
    if ex == "":
        return ""
    else:
        return ex


strs = ['12abwic4sdgdg', '12abw222sdgs', '12abw36rbdfgn', '12abwoww3']

print(longestCommonPrefix(strs))

