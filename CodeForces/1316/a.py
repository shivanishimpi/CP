n = int(input())
for i in range(n):
    m = list(map(int, input().split()))
    stu, high = m[0], m[1]
    scores = list(map(int, input().split()))
    #for i in range(stu):
    if sum(scores) == high:
        #if (sum(scores)/stu==high/stu):
        print(sum(scores))
    elif sum(scores) < high:
        print(sum(scores))
    else:
        print(high)
