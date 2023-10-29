# 메모리: 31120  kb, 시간: 680 ms, 코드길이: 778 Bytes
'''골드5, 시간제한:1초
문제가...이해가..잘 안됨.. 순열조합을 공부해서 이 문제 다시 풀어보기!
문제링크:https://www.acmicpc.net/problem/15686
소스링크:https://codesyun.tistory.com/185
M개를 무작위로 골라서 모든 경우를 찾아야 하기 때문에 완전탐색+dfs 즉, 조합 문제이다.
'''
import sys
from itertools import combinations
n,m=map(int,sys.stdin.readline().split())
city =[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = 999999
house = []      # 집의 좌표
chick = []      # 치킨집의 좌표

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chick.append([i, j])

for chi in combinations(chick, m):  # m개의 치킨집 선택
    temp = 0            # 도시의 치킨 거리
    for h in house: 
        chi_len = 999   # 각 집마다 치킨 거리
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)

print(result)
 

'''
입력예시1)
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
출력예시1)
5
입력예시2)
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
출력예시2)
10
입력예시3)
5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
출력예시3)
11
입력예시4)
5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
출력예시4)
32
'''