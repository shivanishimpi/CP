n = int(input())
for n in range(n):
        m=list(map(int, input().split()))
        a, b = m[0], m[1]
        #print(a,b)
        n = b-a
        c=0
        if(n>0):
                if(n%2==0):
                        c+=2
                else:
                        c+=1
        elif(n<0):
                if(abs(n)%2==0):
                        c+=1
                else:
                        c+=2
        print(c)
