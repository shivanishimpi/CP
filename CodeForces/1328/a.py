for _ in range(int(input())):
    a,b = map(int, input().split())
    p= a%b
    q=a//b
    x = a//b + 1
    if a%b ==0:
        print(0)
    else:
        if x*b > a:
            print(b*x - a)
