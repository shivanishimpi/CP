n=int(input())
for i in range(n):
    c=list(map(int, input().split(" ")))
    x=(c[1]-c[0])/(c[2]+c[3])
    i,j=divmod(x,1)
    if (j==0):
        print(int(x))
    else:
        print("-1")
