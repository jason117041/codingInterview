机器人运动范围
题目描述
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

思路：回溯法。
机器人从（0，0）开始移动，当准备进入（row,col）格子时，先判断能不能进入，如果能进入，判单能否进入(row-1，col),(row+1,col),(row,col-1),
(row,col+1)

# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold < 0 or rows<=0 or cols<=0:
            return 0
        visited = []
        for i in range(rows * cols):
            visited.append(0)
        count = self.movingCountCore(threshold,rows,cols,0,0,visited)
        return count
        
    def movingCountCore(self,thredshold, rows, cols, row, col, visited):
        count = 0
        if self.check(thredshold,rows,cols, row, col, visited):
            visited[row*cols+col] = 1
            count = 1 + self.movingCountCore(thredshold,rows,cols,row+1,col,visited) + \
            self.movingCountCore(thredshold,rows,cols,row-1,col,visited) + \
            self.movingCountCore(thredshold,rows,cols,row,col+1,visited) + \
            self.movingCountCore(thredshold,rows,cols,row+1,col-1,visited)
        return count
            
    # 判断机器人能否进入坐标位(row,col)的方格
    def check(self, thredshold, rows, cols, row, col, visited):
        if row >= 0 and row < rows and col >=0 and col < cols and \
            self.getDigitSum(row) + self.getDigitSum(col) <= thredshold and \
            not visited[row*cols + col]:
                return True
        return False
    def getDigitSum(self, num):
        s = 0           # 获取num数位和
        while num > 0:
            s += num % 10
            num = num // 10
        return s



