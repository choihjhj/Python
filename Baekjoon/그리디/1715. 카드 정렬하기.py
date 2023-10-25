# 메모리: 37600 kb, 시간: 580 ms, 코드길이: 281 Bytes
'''골드 4'''
import sys
from queue import PriorityQueue
n=int(sys.stdin.readline())
que = PriorityQueue()
for i in range(n):
    que.put(int(sys.stdin.readline()))

cnt=0
while(1):
    if(que.qsize()==1):
        break
    a=que.get()
    b=que.get()
    cnt+=(a+b)
    que.put(a+b)

print(cnt)