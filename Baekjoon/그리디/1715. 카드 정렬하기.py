# 메모리: 37600 kb, 시간: 580 ms, 코드길이: 281 Bytes
'''골드 4 시간 제한:2초, (1 ≤ N ≤ 100,000) 
제한시간 2초니까 1초에 20,000,000번이니까 2초니까 40,000,000번이내로 알고리즘을 짜야 한다.
N의 최대가 100,000이니까 O(logN) or O(N)인 알고리즘을 택해서 풀어야 한다.
O(logN) 우선순위큐
O(N) 투포인터
O(NlogN) sort() 이므로 이 방법으로 풀어선 안 된다. 
따라서 결국 우선순위큐로 풀어야 함 
우선순위큐PriorityQueue의 get,put의 시간복잡도는 O(logN)
'''
import sys
from queue import PriorityQueue
n=int(sys.stdin.readline())
que = PriorityQueue()
# qre = PriorityQueue(maxsize = 8)
for i in range(n):
    que.put(int(sys.stdin.readline()))

cnt=0
while True:
    if(que.qsize()==1):
        break
    a=que.get()
    b=que.get()
    cnt+=(a+b)
    que.put(a+b)

print(cnt)