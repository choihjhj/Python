import sys
n=int(sys.stdin.readline()) #15
sum,end,cnt=0,0,0
for start in range(1,n+1):
    while end<=n and sum<n:
        sum+=end
        end+=1
    if sum==n:
        cnt+=1
    sum-=start
print(cnt) #4           