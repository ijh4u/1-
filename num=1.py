n,m=map(int,input().split())
result = 0
while n != 1:
    if n%m ==  0:
        n= n//m
        result+=1
    else:
        n=n-1
        result += 1
print(result)