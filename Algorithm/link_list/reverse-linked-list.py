#!/usr/bin/python
# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.var = x
        self.next = None


class Solution:
    def reverseList(self, head:ListNode) ->ListNode:
        pre = None
        cur = head
        while cur:
            nextnode = cur.next
            cur.next = pre
            pre = cur
            cur = nextnode
        return pre


if __name__ == '__main__':
    print("yes")

