8. 题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

思路：
1.有右子树，沿着右子树出发，下一个节点即为右子树最左节点
2. 无右子树，但它是父节点的左节点，下一个即为父节点
3.无右子树，且有副节点，且是父节点的右节点，则向上寻找，直到找到是父节点的左节点


# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode is None:
            return None
        pNext = None
        if pNode.right:       #右子树
            pNode = pNode.right
            while pNode.left!=None:
                pNode = pNode.left
            pNext = pNode
        else:     #无右子树
            if pNode.next and pNode.next.left == pNode:     #但是父节点的左节点
                pNext = pNode.next
            elif pNode.next and pNode.next.right == pNode:    #第三种情况
                pNode =  pNode.next
                while pNode.next and pNode.next.right == pNode:
                    pNode = pNode.next
                pNext = pNode.next
        return pNext
