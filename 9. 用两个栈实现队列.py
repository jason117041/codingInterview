题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

思路：两个栈p1，p2，p1压入栈，p2为出栈。p1压入元素，当要出队列的时候
      (1)：p2为空，p1元素全部出栈压入p2，然后p2出栈
      (2): p2不为空，直接弹出p2元素
      
      
class Solution:
    def __init__(self):
        self.p1 = []
        self.p2 = []
    def push(self, node):
        # write code here
        self.p1.append(node)
    def pop(self):
        if len(self.p2) != 0:
            return self.p2.pop()
        else:
            while len(self.p1) != 0:
                self.p2.append(self.p1.pop())
            return self.p2.pop()
