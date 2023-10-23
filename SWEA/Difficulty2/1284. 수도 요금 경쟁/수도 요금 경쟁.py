T=int(input())
for tc in range(1,T+1):
    P, Q, R, S, W=map(int,input().split())
    #A사
    A=W*P
    #B사
    if W<=R:
        B=Q
    else:
        B=Q+(W-R)*S
    print(f"#{tc} {min(A, B)}")