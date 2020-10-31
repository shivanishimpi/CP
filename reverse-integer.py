"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
#SOLUTION1
for _ in range(int(input())):
    x = int(input())
    if x >= 0: #if x is postiive 
        x=str(x) #no need to take abs
        if int(x[::-1])<=2**31-1: #reverse should be less than 2**31-1
            print(int(x[::-1])) #if it is less then return the reverse
        else: #if the reverse is greater than 2**31-1
            print(0)
    else:
        x=str(abs(x))
        if int(x[::-1])<=2**31:
            print(-int(x[::-1]))
        else:
            print(0)
"""
#SUBMITTED 
class Solution(object):
    def reverse(self,x):
        if x >= 0: #if x is postiive 
            x=str(x) #no need to take abs
            if int(x[::-1])<=2**31-1: #reverse should be less than 2**31-1
                return int(x[::-1]) #if it is less then return the reverse
            else: #if the reverse is greater than 2**31-1
                return 0
        else:
            x=str(abs(x))
            if int(x[::-1])<=2**31:
                return -int(x[::-1])
            else:
                return 0
"""
