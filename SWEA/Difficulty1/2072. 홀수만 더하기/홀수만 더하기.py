T=int(input())
for tc in range(1,T+1):
    s=list(map(int,input().split()))
    sum=0
    for x in s:
        if x%2==1:
            sum += x
    print(f'#{tc} {sum}')