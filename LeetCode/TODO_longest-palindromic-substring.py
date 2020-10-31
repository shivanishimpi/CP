"""
Given a string s, return the longest palindromic substring in s.
"""
for _ in range(int(input())):
    s = list(str(input()))
    print(s)
    for i in range(len(s)):
        for j in range(len(s)):
            #print(i,j)
            if s[i]==s[j] and i!= j:
                print(i, s[i], j, s[j])
                for k in range(i,j):
                    print(s[k])
