# 메모리: 86552  kb, 시간: 1476 ms, 코드길이: 414 Bytes
'''골드2, 시간제한:1초,  (1 ≤ N, K ≤ 300,000) (0 ≤ Mi, Vi ≤ 1,000,000) (1 ≤ Ci ≤ 100,000,000)
메모리+시간 생각해서 list대신 tuple쓰기
jews랑 bags 오름차순정렬 후 bags에서 하나씩 꺼내서 jews의 첫번째 무게가 가방무게안에 들어오면 
가격들 다 while로 최대힙으로 저장해서 다끝나면 heap에서 -heappop최대힙으로 가격 젤 높은거 꺼내서 result에 더하기  
'''
import sys
import heapq
input=sys.stdin.readline
n,k = map(int,input().split())
jews = [tuple(map(int,input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
jews.sort();bags.sort()
result = 0;heap = [] 
for bag in bags:
    while jews and jews[0][0] <= bag: #가방무게보다 작은 보석무게이면,
        heapq.heappush(heap, -jews[0][1]) #힙에 보석가격 담기
        heapq.heappop(jews) #최소힙으로 jews 지금순서꺼 pop
    if heap: #힙에 들어가 있는 보석무게들 중 가장 큰것 result에 더하기
        result -= heapq.heappop(heap)
print(result)

'''
입력예시1)
2 1
5 10
100 100
11
출력예시1)
10

입력예시2)
3 2
1 65
5 23
2 99
10
2
출력예시2)
164
'''
