n = int(input())
for i in range(n):
    x = int(input())
    if x == 1:
        print(-1)
    #elif x % 17==0:
    #    print(int('2'*(x-1)+'3'))
    else:
        print(int('5'*(x-1)+'4'))
