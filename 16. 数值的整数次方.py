题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

保证base和exponent不同时为0

#思路：
a^n  = { 2个 a的n/2次方    n为偶
       { 2个a的(n-1)次方 * a    n为奇数

class Solution:
    def Power(self, base, exponent):
        # write code here
        
        if base == 0:
            return 0.0
        res = self.powerexp(base, abs(exponent))
        if exponent < 0:
            return 1.0 / res
        return res
    def powerexp(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        res = self.powerexp(base, exponent>>1)
        res *= res
        if exponent & 1 == 1:
            res *= base
        return res
         
