#!/usr/bin/python
# -*- coding: utf-8 -*-

# 13 罗马数字转整数

# IV IX XL XC CD CM (4,9,40,90,400,900)
# I V X L C D M  (1,5,10,50,100,500,1000)


dic = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}
result = []

class Solution:
    @staticmethod
    def romanToIntself(s: str) -> int:
        i = 0
        while i < len(s):
            if s[i] in ['I', 'X', 'C']:
                if s[i:i+2] in dic.keys():
                    result.append(dic[s[i:i+2]])
                    i += 2
                else:
                    result.append(dic[s[i]])
                    i += 1
            else:
                    result.append(dic[s[i]])
                    i += 1
        return sum(result)


if __name__ == '__main__':
    ss = 'CMXCIX'
    s = Solution()
    # print(s.romanToInt(ss))
    print(s.romanToIntself(ss))