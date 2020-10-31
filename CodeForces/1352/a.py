for _ in range(int(input())):
    num = int(input())
    c = 1
    pos_nums = []
    while num != 0:
        z = num % 10
        pos_nums.append(z *c)
        num = num // 10
        c = c*10
    #print(pos_nums)
    val = [p for p in pos_nums if p !=0]
    print(len(val))
    print(*val, sep=" ")
