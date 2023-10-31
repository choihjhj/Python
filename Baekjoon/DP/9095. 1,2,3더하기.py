# 메모리: 31120  kb, 시간: 40 ms, 코드길이: 325 Bytes
'''실버3, 시간제한:1초
다이나믹 프로그래밍
패턴찾기
dp[1]=1
dp[2]=2
dp[3]=4  : 1+1+1,1+2,2+1,3
dp[4]=7  : 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1
dp[5]=13 : 1+1+1+1+1, 1+2*5개, 2+2+1*3개, 3+1+1*3개, 3+2
'''
import sys
T=int(sys.stdin.readline())
for _ in range(T):
    n=int(sys.stdin.readline())
    dp=[0]*(n+1)
    for i in range(1,n+1):
        if i == 1:
            dp[i]=1
        elif i ==2:
            dp[i]=2
        elif i==3:
            dp[i]=4
        else:
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[n])    

'''
입력예시)
3
4
7
10
출력예시)
7
44
274
'''