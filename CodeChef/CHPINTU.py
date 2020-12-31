"""
https://www.codechef.com/problems/CHPINTU
Chef went to Australia and saw the destruction caused by bushfires, which made him sad, so he decided to help the animals by feeding them fruits. First, he went to purchase fruits from Pintu.

Pintu sells M different types of fruits (numbered 1 through M). He sells them in N baskets (numbered 1 through N), where for each valid i, the i-th basket costs Pi and it contains fruits of type Fi. Chef does not have too much money, so he cannot afford to buy everything; instead, he wants to choose one of the M available types and purchase all the baskets containing fruits of that type.

Help Chef choose the type of fruit to buy such that he buys at least one basket and the total cost of the baskets he buys is the smallest possible.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and M.
The second line contains N space-separated integers F1,F2,…,FN.
The third line contains N space-separated integers P1,P2,…,PN.
Output
For each test case, print a single line containing one integer ― the minimum price Chef must pay.

Example Input
1
6 4
1 2 3 3 2 2
7 3 9 1 1 1

Example Output
5
"""

for _ in range(int(input())):
    v = list(map(int, input().split()))
    bnum, frtypes = v[0], v[1]
    fr = list(map(int, input().split()))
    bask = list(map(int, input().split()))
    dic= {}
    for f,b in zip(fr, bask):
        dic[f]= dic.get(f,0) +b
    val = [dic[i] for i in dic]
    print(min(val))
