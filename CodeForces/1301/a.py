n = int(input())
for g in range(n):
    a=list(map(str, input().strip()))
    b=list(map(str, input().strip()))
    c=list(map(str, input().strip()))
    x=-1
    for y in range(len(a)):
        if (b[y]==c[y] or a[y]==c[y]):
            x+=1
    if (x==(len(a)-1)):
        print("YES")
    else:
        print("NO")
