题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39


思路,不能用递归，自下而上

class Solution:
    def Fibonacci(self, n):
        # write code here
        if n <= 0:
            return 0
        if n == 1:
            return 1
        f1, f2 = 0, 1
        
        for i in range(2, n+1):
            fn = f1 + f2
            f1 = f2
            f2 = fn
        return fn
