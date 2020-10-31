for _ in range(int(input())):
    t = int(input())
    lis = list(map(int, input().strip()))
    #print(t,lis)
    a = []
    b = []
    f=1
    for i in lis:
        if i == 0:
            a.append(0)
            b.append(0)
        elif i == 2:
            if f:
                a.append(1)
                b.append(1)
            else:
                a.append(0)
                b.append(2)
        else:
            if f:
                a.append(1)
                b.append(0)
            else:
                a.append(0)
                b.append(1)
            f = 0
    print(''.join(map(str, a)))
    print(''.join(map(str, b)))
