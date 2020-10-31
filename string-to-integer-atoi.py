#NOT FOR DECIMALS
for _ in range(int(input())):
    strs = list(str(input()))
    print(strs)
    lis = [i for i in range(0,10)]
    alphabets = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    flag = False
    signs = ['+', '-']
    val = []
    for i in range(len(strs)):
        try:
            if int(strs[i]) in lis:
                flag = True
                #print(strs[i],'valid')
                val.append(strs[i])
        except:
            if str(strs[i]) in signs:
                flag = True
                #print(strs[i], 'valid')
                val.append(strs[i])

    val = int("".join(val))
    if strs[0] not in alphabets and flag == True:
        if int(val)>2**31-1:
            print(2**31-1)
        elif int(val)<-2**31:
            print(-2**31)
        else:
            print(val)
    else:
        print(0)
