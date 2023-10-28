'''우선순위 큐 라이브러리를 활용한 힙정렬 구현 예제
heapq안에 PriorityQueue 내장되어 있음.
그래서 PriorityQueue으로 put(),get()해도 됨
'''
import sys
import heapq #기본적으로 최소힙으로 구현됨(내림차순)
input=sys.stdin.readline

def heapsort(iterable):
    h=[]
    result=[]
    for value in iterable:
        heapq.heappush(h,value) # heapq.heappush(h,-value) 최대힙(오름차순)

    for i in range(len(h)):
        result.append(heapq.heappop(h)) #result.append(-heapq.heappop(h)) 최대힙(오름차순)
    return result

n=int(input())
arr=[int(input()) for _ in range(n)]
res=heapsort(arr)
print(res)        

'''우선순위 큐 (Priority Queue) -참고만 하기 주로 import heapq 을 더 많이 사용함!!'''
from queue import PriorityQueue   # 우선순위 큐 생성 (Priority Queue는 내부적으로 heap 모듈을 사용함)
que = PriorityQueue()   
limitedQue = PriorityQueue(maxsize=10) #크기 제한이 있는 우선순위 큐    
que.put(1)   # 원소 삽입 - 정수 
que.put(2)   
que.put((2,'hello'))   #(우선순위,값)
que.put((1,'world'))   
print(que.get())   
# print(que,get()[1]) # tuple에서 값 반환   

''' 최소힙 관련 문제) [그리디/골드] 백준 1715.카드 정렬하기 문제'''