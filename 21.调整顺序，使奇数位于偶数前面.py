题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

#如果使用排思想，增加两个指针分别为前和后，偶数start++，不是偶数end--，然后交换，这样相对顺序
#容易打乱，不稳定，使用sorted解决

class Solution:
    def reOrderArray(self, array):
        # write code here
        return sorted(array, key = lambda x:x%2,reverse = True)
