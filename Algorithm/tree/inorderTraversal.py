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


# Definition for a tree
class Tree:
    def __init__(self):
        self.root = None
        self.lis = []

        # 以下三个lis主要用于遍历打印存储，非必须
        self.preRsult = []
        self.inRsult = []
        self.postResult = []

    def addNode(self, val):
        node = TreeNode(val)                        # 实例化树节点
        if self.root == None:                       # 判断根节点是否为None，若为None，将根节点地址值添加到lis中
            self.root = node
            self.lis.append(self.root)
        else:
            rootNode = self.lis[0]                  # 将第一个元素设置为根节点
            if rootNode.left == None:
                rootNode.left = node
                self.lis.append(rootNode.left)
            elif rootNode.right == None:
                rootNode.right = node
                self.lis.append(rootNode.right)
                self.lis.pop(0)                     # 弹出lis的第一个元素

    def preOrderTraversal(self, root):
        if root == None:
            return
        self.preRsult.append(root.val)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)

    def preOrderStack(self, root):
        if root == None:
            return
        stack = []
        result = []
        node = root
        while node or stack:
            while node:
                result.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        print(result)


    def inOrderTraversal(self, root):
        if root == None:
            return
        self.inOrderTraversal(root.left)
        self.inRsult.append(root.val)
        self.inOrderTraversal(root.right)

    def inOrderStack(self, root):
        if root == None:
            return
        stack = []
        result = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        print(result)


    def postOrderTraversal(self, root):
        if root == None:
            return
        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        self.postResult.append(root.val)

    def postOrderStack(self, root):
        if root == None:
            return
        stack = []
        seq = []
        result = []
        node = root
        while node or stack:
            while node:
                seq.append(node.val)
                stack.append(node)
                node = node.right
            node = stack.pop()
            node = node.left
        while seq:
            result.append(seq.pop())
        print(result)


# class Solution:
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     pass


if __name__ == '__main__':
    li = [1, None, 2, 3]
    T = Tree()
    for i in li:
        T.addNode(i)

    T.preOrderTraversal(T.root)
    print(T.preRsult)
    T.preOrderStack(T.root)

    T.inOrderTraversal(T.root)
    print(T.inRsult)
    T.inOrderStack(T.root)

    T.postOrderTraversal(T.root)
    print(T.postResult)
    T.postOrderStack(T.root)



