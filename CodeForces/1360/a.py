for _ in range(int(input())):
    li = list(map(int, input().split()))
    if 2* min(li) > max(li):
        print((2*min(li))**2)
    else:
        print(max(li)**2)
