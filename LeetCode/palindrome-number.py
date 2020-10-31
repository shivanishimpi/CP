"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?

#SOLUTION
for _ in range(int(input())):
    x = int(input())
    if x<0:
        print("false")
    else:
        x = str(x)
        #print(x)
        if len(x)%2=0: #
            mid=int(len(x)/2)
            #23432 01234
            if x[:int(mid-1)] == x[int(mid+1):]: #
                print('true')
"""
for _ in range(int(input())):
    x=int(input())
    x=str(x)
    if x == x[::-1]:
        print('true')
    else:
        print('false')
"""
#SUBMITTED
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if x == x[::-1]:
            return True
        else:
            return False
"""
