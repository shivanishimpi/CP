n = int(input())
for i in range(n):
    val = list(map(int, input().split()))
    pol1, pol2 = val[0], val[1]
    if(pol1 % pol2 == 0):
        print("YES")
    else:
        print("NO")
 
