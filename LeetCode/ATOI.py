for _ in range(int(input())):
    strs = list(str(input()))
    #print(strs)
    #digits = [i for i in strs if i.isdigit()]
    alphabets = list('"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    #print(digits)
    digs = []
    flag = False
    if strs[1] not in alphabets:
        flag = True
        #print(strs[1])
    for i in range(len(strs)):
        if strs[i] not in alphabets and flag == True:
            digs.append(strs[i])            
    strippedDigs=[]
    #print(digs)
    for i in digs:
        if i.strip():
            strippedDigs.append(i)
    val = "".join(strippedDigs)
    #print(val)
    #print("".join(digs)
    #digs = float("".join(digs))
    #print(digs)
    if strs[1] not in alphabets and flag == True:
        if float(val)>2**31-1:
            print(2**31-1)
        elif float(val)<-2**31:
            print(-2**31)
        else:
            if float(val)==int(float(val)):
                print(int(val))
            else:
                print(float(val))
    else:
        print(0)
"""    lis = [i for i in range(0,10)]
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
    if strs[1] not in alphabets and flag == True:
        if int(val)>2**31-1:
            print(2**31-1)
        elif int(val)<-2**31:
            print(-2**31)
        else:
            print(val)
    else:
        print(0)
"""
