# 메모리: 125296  kb, 시간: 2652 ms, 코드길이: 1160 Bytes
'''골드4, 시간제한:2초,(3 ≤ N, M ≤ 8)
BFS문제
얻을 수 있는 안전 영역의 최대 크기를 출력한다.
0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다.2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
빈 칸의 개수는 3개 이상이다.
문제링크: https://www.acmicpc.net/problem/14502
설명링크:
https://jie0025.tistory.com/209
https://great-park.tistory.com/104
'''
from collections import deque
import copy
import sys
input = sys.stdin.readline

d = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs():
    queue = deque()
    #queue에 2의 위치 전부 append
    test_map = copy.deepcopy(lab_map) #원래 map은 유지
    for i in range(n): #바이러스 큐에 넣기
        for k in range(m):
            if test_map[i][k] == 2:
                queue.append((i,k))

    while queue: #탐색 시작
        r,c = queue.popleft()

        for i in range(4):
            dr = r+d[i][0]
            dc = c+d[i][1]

            if (0<=dr<n) and (0<=dc<m): #범위 확인
                if test_map[dr][dc] == 0: #감염 가능여부 확인
                    test_map[dr][dc] =2
                    queue.append((dr,dc))

    global result
    count = 0
    for i in range(n):
        for k in range(m):
            if test_map[i][k] == 0:
                count +=1

    result = max(result, count)


def make_wall(count):
    if count == 3: #벽3개가 세워지면 바이러스를 퍼트려 본다.
        bfs()
        return
    for i in range(n):
        for k in range(m):
            if lab_map[i][k] == 0: #빈 공간이라면 벽 세우기 가능
                lab_map[i][k] = 1 #벽을 세우고
                make_wall(count+1) #다시 두번째 벽 세우러 감
                lab_map[i][k] = 0 #다시 벽을 허무는 과정(백트래킹)


n, m = map(int,input().split())
lab_map = [list(map(int,input().split())) for _ in range(n)]

result = 0
make_wall(0)

print(result)
'''
입력예시1)
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
출력예시1)
27
입력예시2)
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
출력예시2)
9
입력예시3)
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
출력예시3)
3
'''