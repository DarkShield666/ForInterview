#!/usr/bin/python
# -*- coding: utf-8 -*-

# 题号：94 二叉树的中序遍历
# 给定一个二叉树，返回它的中序遍历
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,3,2]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        pass