n=int(input())
for i in range(n):
    fake=int(input())
    nec=list(map(int, input().strip().split(" ")))
    bre=list(map(int, input().strip().split(" ")))
    su=[]
    def vala():
        for j in range(len(nec)):
            su.append(nec[j]+bre[j])
    vala()
    c=True
    t=0
    while(c):
        if len(su) != len(set(su)):
            if t==0:
                nec.sort(reverse=True)
                bre.sort(reverse=True)
                su.clear()
                vala()
                t+=1
            elif t==1:
                nec.sort()
                bre.sort()
                su.clear()
                vala()
                t+=1
            elif t==2:
                nec.sort(reverse=True)
                bre.sort()
                su.clear()
                vala()
                t+=1
            elif t==3:
                nec.sort()
                bre.sort(reverse=True)
                su.clear()
                vala()
                t+=1
        else:
            c=False
    print(*nec, sep=' ')
    print(*bre, sep=' ')
