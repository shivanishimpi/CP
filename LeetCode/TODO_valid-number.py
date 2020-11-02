for _ in range(int(input())):
    strs = list(str(input()))
    #print(strs)
    d=""
    for x in strs:
        if (x=='-' or x=="e" or x=='+' or x=="." or x==" " or x.isdigit()):
            d+=x
    print(d)
    j=0
    i = 0
    for y in range(len(d)):
        if d[y]==".":
            i = y
            j = y
        elif (d[y]=='e'):
            j = y
        if j<i:
            print("invalid",d)
