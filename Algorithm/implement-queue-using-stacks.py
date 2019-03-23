#!/usr/bin/python
# -*- coding: utf-8 -*-
# 232-用栈实现队列

from collections import deque


class Stack:
    def __init__(self):
        self.items = deque()

    def push(self, val):
        return self.items.append(val)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0


class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, val):
        self.s1.push(val)

    def pop(self):
        if not self.s2.empty():
            return self.s2.pop()
        while not self.s1.empty():
            val = self.s1.pop()
            self.s2.push(val)
        return self.s2.pop()

    def peek(self):
        if not self.s2.empty():
            return self.s2.top()
        while not self.s1.empty():
            val = self.s1.pop()
            self.s2.push(val)
        return self.s2.top()

    def empty(self):
        return self.s1.empty() and self.s2.empty()


if __name__ == '__main__':
    s = Stack()
    s.push(5)
    s.push(6)
    s.push(8)
    print(s.items)

    print(s.top())
    print(s.empty())
    print(s.pop())
    print(s.pop())