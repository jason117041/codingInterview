二进制中1的个数
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。



思路：
n减去1 再与本身相与，会导致最右边为0

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here 
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n - 1) & n
        return count
