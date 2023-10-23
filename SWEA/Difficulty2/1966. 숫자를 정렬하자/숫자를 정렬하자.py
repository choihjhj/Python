T=int(input())
for tc in range(1,T+1):
    input()
    s=list(map(int,input().split()))
    s.sort()
    print(f"#{tc}",*s)