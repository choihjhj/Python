'''
DFS/BFS는 경로탐색, 네트워크, 조합만들기 문제가 많이 나옴
보통 쉬운 문제들은 DFS로 구현하고, 어려워 보이는 문제들은 BFS로 구현하기.
한 문제를 DFS/BFS로 구현해보면서 연습하기.
'''
### [알고리즘] DFS 깊이우선탐색 (그래프 탐색 알고리즘)
''' 깊은 부분을 우선적으로 탐색하는 알고리즘 '''

# 구현방법)
#- 스택
#- 재귀 

'''
1. 탐색 시작 노드를 스택에 삽입하고 방문처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리한다.
방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 더이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
'''
# DFS 구현코드)
def dfs(graph, v, visited):
    visited[v]=True #현재 노드 방문 처리
    print(v,end=' ')
    for i in graph[v]: #현재노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]:
            dfs(graph, i , visited)
graph=[
    [],
    [2,3,8], #해당 노드에 인접한 리스트, 즉 1과 연결된 숫자들
    [1,7],   #2와 연결된 숫자들
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]            
visited=[False]*9
dfs(graph,1,visited) #1 2 7 6 8 3 4 5 

'''
프로그래머스 관련 문제
- 타겟넘버
'''
### [알고리즘] BFS 너비우선탐색 (그래프 탐색 알고리즘)------------------------------------------------------------
'''그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘'''

#구현방법)
#큐, 연결리스트로 구현

'''
1. 탐색 시작 노드를 큐에 삽입하고 방문처리를 한다.
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리한다.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
'''

# BFS 구현코드)
from collections import deque
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
graph=[
    [],
    [2,3,8], #해당 노드에 인접한 리스트, 즉 1과 연결된 숫자들
    [1,7],   #2와 연결된 숫자들
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]            
visited=[False]*9
bfs(graph,1,visited) #1 2 3 8 7 4 5 6

'''
프로그래머스 관련 문제
- 여행경로
'''