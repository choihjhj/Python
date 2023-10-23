T=int(input())
for tc in range(1,T+1):
    input()
    s = [abs(int(x)) for x in input().split()]
    min=min(s)
    print(f"#{tc} {min} {s.count(min)}")
    