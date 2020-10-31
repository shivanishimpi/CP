for _ in range(int(input())):
    strs = list(input().split(' '))
    print(strs)
    stringlist = []
    for i,j in zip(range(len(strs)), range(1,len(strs))):
        print(strs[i], strs[j])
        for m,n in zip(range(len(strs[i])), range(len(strs[j]))):

            #if strs[i] == strs[j]):
            #if strs[i][n] == strs[j][m]:
            #    stringlist.append(strs[i][n])
    #print(stringlist)
