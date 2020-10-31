n= int(input())
for i in range(n):
    m = int(input())
    arr = list(map(int, input().split()))
    arrn = arr + arr
    setar = set(arrn)
    print(len(setar))
