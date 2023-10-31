# 메모리: 31120  kb, 시간: 344 ms, 코드길이: 274 Bytes
'''실버2, 시간제한:2초, (1 ≤ N ≤ 20, |S| ≤ 1,000,000)
combinations 함수를 호출해 배열에서 뽑을 수 있는 모든 조합을 구해준다.
'''
import sys
from itertools import combinations
n,s=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
cnt = 0
for i in range(1, n+1):
    comb = combinations(arr, i)
    for x in comb:
        if sum(x) == s:
            cnt += 1
print(cnt)
'''
입력예시)
5 0
-7 -3 -2 5 8
출력예시)
1
'''