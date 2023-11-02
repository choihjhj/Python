import sys
from collections import deque
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4): #상하좌우 1 체크
            nx=x+d[i][0]
            ny=y+d[i][1]
            if nx<0 or ny<0 or nx>=n or ny>=m: continue
            if graph[nx][ny]==0: continue
            if graph[nx][ny]==1: #해당노드를 처음 방문하는 경우에만 최단거리 기록
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1] #가장 오른쪽 아래까지의 최단거리 반환            
n,m=map(int,sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
d=[(-1,0),(1,0),(0,-1),(0,1)] #상하좌우
print(bfs(0,0))
'''
for x in graph:
    print(*x)
3 0 5 0 7 0
2 3 4 5 6 7
0 0 0 0 0 8
14 13 12 11 10 9
15 14 13 12 11 10
'''    
'''
입력예시)
5 6
101010
111111
000001
111111
111111
출력예시)
10
'''