# 메모리: 32140  kb, 시간: 48 ms, 코드길이: 380 Bytes
'''실버4, 시간제한:0.5초'''
import sys
n,m=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().strip().split()))
start,end,sum,cnt=0,0,0,0
while end <= n:
    if sum == m:
        cnt += 1
        sum -= data[start]
        start += 1
    elif sum < m:
        if end < n:
            sum+=data[end]
        end+=1
    elif sum>m:
        sum-=data[start]
        start+=1
print(cnt)
'''
입력예시1)
4 2
1 1 1 1
출력예시1)
3
입력예시2)
10 5
1 2 3 4 2 5 3 1 1 2
출력예시2)
3
'''