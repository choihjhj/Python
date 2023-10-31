'''난이도1.5, 시간제한:1초
0구멍뚫린부분, 1칸막이
한번에 만들 수 있는 아이스크림의 개수를 출력하라.
구현방법)
1. 특정한 지점의 주변 상하좌우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 
해당 지점 방문한다.
2. 방문한 지점에서 다시 상하좌우를 살펴보면서 방문을 진행하는 과정을 반복하면, 연결된 모든 지점을 방문할 수 있다.
3. 모든 노드에 대하여 1-2번의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트한다..
'''
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m: #범위 벗어나면 종료
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y) #상하좌우
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
import sys
n,m=map(int, sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result+=1
print(result)            
'''
입력예시)
4 5
00110
00011
11111
00000
출력예시)
3
'''