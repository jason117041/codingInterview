题目描述
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。


class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if len(s) <= 0:
            return False
        has_sign = False
        has_dot = False
        has_e = False
        for i in range(len(s)):
            if s[i] == 'E' or s[i] =='e':
                if has_e:
                    return False
                else:
                    has_e = True
                    if i == len(s) - 1:
                        return False
            elif s[i] == '+' or s[i] == '-':
                if has_sign:
                    if s[i-1] != 'e' and s[i-1]!='E':
                        return False
                else:
                    has_sign = True
                    if i != 0 and s[i-1]!='e' and s[i-1]!='E':
                        return False
            elif s[i] == '.':
                if has_dot or has_e:
                    return False
                else:
                    has_dot = True
                    if i > 0 and s[i-1]=='e' and s[i-1] == 'E':
                        return False
            else:
                if s[i] <'0' or s[i] > '9':
                    return False

        return True
        
        
        
        
        
        
