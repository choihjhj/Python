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
