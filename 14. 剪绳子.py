剪绳子
题目：给你一根长度为n的绳子，请把绳子剪成m段 (m和n都是整数，n>1并且m>1)
每段绳子的长度记为k[0],k[1],...,k[m].请问k[0]*k[1]*...*k[m]可能的最大乘积是多少？
例如，当绳子的长度为8时，我们把它剪成长度分别为2,3,3的三段，此时得到的最大乘积是18.

解法一：o（n^2）时间复杂度的动态规划， f(n) = f(i) * f(n-i)
def maxProductAfterCutting(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        a = [0, 1,2,3] #最优解数组，长度为3时，3？1*2，3为最优
        
        for i in range(4, n+1):
            maxN = 0
            for j in range(1, i):
                tmp = a[j] * a[i - j]
                if tmp > maxN:
                    maxN = tmp
            a.append(maxN)
        return a[-1]
        
        
        
#解法2,贪婪法，n>=5时，尽可能剪3，当剩下长度为4，则应该剪成2段。时间复杂度o(1)
def cut(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        l3 = n // 3 #尽可能剪3
        if n - l3 * 3 == 1:  #如果剩下的是4的长度，则最后一段不能剪，因为2*2>3*1
            l3 -= 1
        l2 = (n - l3*3) //2
        return 3**l3 * 2**l2
