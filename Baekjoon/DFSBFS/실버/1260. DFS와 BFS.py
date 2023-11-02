# 메모리: 34096  kb, 시간: 72 ms, 코드길이: 1142 Bytes
'''실버2, 제한시간:2초,
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다
단, 정점만 찾아나가는 방식으로 구현할 경우 낮은 숫자부터 탐색하라고 되어있으니 오름차순 정렬이 필요하다.
'''
import sys
from collections import deque
def dfs(graph, v, visited):
    visited[v]=True #현재 노드 방문 처리
    print(v,end=' ')
    for i in graph[v]: #현재노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]:
            dfs(graph, i , visited)
def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True #현재 노드 방문처리
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]: #아직 방문하지 않은 인접한 원소들을 큐에 삽입
                queue.append(i)
                visited[i]=True
n,m,v=map(int, sys.stdin.readline().split()) #n정점개수,m간선개수,v탐색시작정점번호
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph: #단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
    i.sort()

visited=[False]*(n+1)
dfs(graph,v,visited)
print()
visited=[False]*(n+1)
bfs(graph,v,visited)

'''
입력예시1)
4 5 1
1 2
1 3
1 4
2 4
3 4
출력예시1)
1 2 4 3
1 2 3 4
입력예시2)
5 5 3
5 4
5 2
1 2
3 4
3 1
출력예시2)
3 1 2 5 4
3 1 4 2 5
입력예시3)
1000 1 1000
999 1000
출력예시3)
1000 999
1000 999
'''