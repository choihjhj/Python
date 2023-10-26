'''골드 4, 시간 제한:2초, (1 ≤ N ≤ 100,000) 
제한시간 2초니까 1초에 20,000,000번이니까 2초니까 40,000,000번 이내로 알고리즘을 짜야 한다.
N의 최대가 100,000이니까 O(NlogN) 알고리즘을 택해서 풀어야 한다.
O(logN) 힙,우선순위큐
O(N) 투포인터
O(NlogN) sort(), heappush,heappop,get,put  

최소비교횟수를 구하는 문제니까,
최소힙인 heapq 자료구조를 이용해서 O(NlogN)로 풀면 된다.
물론, 우선순위큐 PriorityQueue도 있지만 되도록이면 heapq 사용하기!
'''

# 메모리: 33972 kb, 시간: 580 ms, 코드길이: 281 Bytes
'''예시1) heapq 이용'''
import sys
import heapq
N=int(sys.stdin.readline())
heap=[]
cnt=0
for _ in range(N):
    heapq.heappush(heap,int(sys.stdin.readline()))
while True:
    if len(heap)==1:break
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)
    cnt+=(a+b)
    heapq.heappush(heap,a+b)
print(cnt)


# 메모리: 37600 kb, 시간: 180 ms, 코드길이: 280 Bytes
'''예시2) PriorityQueue 이용'''
import sys
from queue import PriorityQueue
n=int(sys.stdin.readline())
que = PriorityQueue()
cnt=0
# qre = PriorityQueue(maxsize = 8)
for i in range(n):
    que.put(int(sys.stdin.readline()))
while True:
    if(que.qsize()==1):
        break
    a=que.get()
    b=que.get()
    cnt+=(a+b)
    que.put(a+b)
print(cnt)