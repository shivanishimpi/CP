for _ in range(int(input())):
    s = list(str(input()))
    d=""
    w=True
    if s[0].isalpha():
        print(0)
    for x in s:
        if (x == "-" or x == "+" or x==" " or x.isdigit()):
            if x==" ":
                w=False
            else:
                d+=x
        else:
            break
    print(d)
    """if int(d)>(2**31-1):
        print(2**31-1)
    elif int(d)<(-2**31):
        print(-2**31)
    else:
        print(d)"""
