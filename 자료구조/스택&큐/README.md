# [자료구조] 스택 & 큐


### 스택 (stack)
LIFO(Last In First Out)
  
파이썬 내장모듈에서는 따로 스택 라이브러리가 존재하지 않는다.
보통 덱 라이브러리를 import 해서 스택 대신 사용한다.

from collections import deque

dq=deque() # 덱 생성   
dq.append() # 덱의 가장 오른쪽에 원소 삽입    
dq.popleft() # 가장 왼쪽 원소 반환    
dq.appendleft() # 덱의 가장 왼쪽에 원소 삽입   
dp.pop() # 가장 오른쪽 원소 반환   
dp.clear() # 모든 원소 제거   
dp.copy() # 덱 복사   
dp.count(x) #x와 같은 원소의 개수를 계산    
 
'''공식문서 : https://docs.python.org/3.8/library/collections.html#collections.deque'''


### 큐 (stack)
FIFO(First In First Out) 선착순   
queue   
dequeue : stack+ queue   


### 우선순위 큐 (Priority Queue)

from queue import PriorityQueue    
📚 우선순위 큐 생성 (Priority Queue는 내부적으로 heap 모듈을 사용함)

que = PriorityQueue()   
limitedQue = PriorityQueue(maxsize=10) #크기 제한이 있는 우선순위 큐   
📚 원소 삽입 - 정수

que.put(item)   
que.put(1)   
que.put(2)   
📚 원소 삽입 - 튜플 (우선순위,값)

que.put((priority, item))   
que.put((2,'hello'))   
que.put((1,'world'))   
📚 원소 삭제 및 반환 -> 크기 순서대로 삭제됨   

print(que.get())   
print(que,get()[1]) # tuple에서 값 반환   

예시 - 백준 1715.카드 정렬하기 문제

