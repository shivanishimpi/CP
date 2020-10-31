def odd(n):
  if n%2==0:
    return 0
  else:
    return 1
for _ in range(int(input())):
  n, k = map(int,input().split())
  lhs=(n-k)/2
  rhs=k*(k-1)/2
 
  if(k>n):
    print("NO")
 
  else:
 
    if((odd(n)==1) & (odd(k)==0)):
      print("NO")
    
    elif((odd(n)==0) & (odd(k)==1)):
      print("NO")
 
    else:
      if(lhs>=rhs):
        print("YES")
      else:
        print("NO")
