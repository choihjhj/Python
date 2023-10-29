# 메모리: 39368  kb, 시간: 312 ms, 코드길이: 276 Bytes
'''실버3, 시간제한:2초
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
'''
import sys
M,N=map(int, sys.stdin.readline().split())
arr=[True for _ in range(N+1)]
arr[0],arr[1]=False,False
for i in range(2,int(N**0.5)+1):
    if arr[i]:
        for j in range(i*2,N+1,i):
            arr[j]=False          
for i in range(M,N+1):
    if arr[i] :print(i)          
'''
입력예시)
3 16
출력예시)
3
5
7
11
13
'''