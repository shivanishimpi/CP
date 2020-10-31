n=int(input())
for x in range(n):
    num=int(input())
    def gcd(c,b):
        while b>0:
            c,b=b,c%b
        return c
    def lcm(c,b):
        return c*b/gcd(c,b)
    b=1
    c=num-1
    d=num
    while((d-1)):
        if((gcd(c,b)+lcm(c,b))==num):
            print(c,b)
            break
        else:
            a=a-1
            b=b+1
        d=d-1
