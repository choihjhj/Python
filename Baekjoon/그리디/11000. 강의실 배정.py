# 메모리: 86516  kb, 시간: 444 ms, 코드길이: 307 Bytes
'''골드 5 제한시간:1초,  (1 ≤ N ≤ 200,000)
1초니까 20,000,000번이내 여야 함
따라서 O(NlogN)이내여야 한다.
sort()는 O(NlogN)
heap은 O(logN), heappush랑 heappop은 O(nlogn)

-> 이 문제의 총 시간복잡도는 n(입력)+ nlogn(sort)+nlogn(heappush,heappop)이다.

최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 
회의실은 가장 빨리 시작하는 순으로 정렬한다.
그래야 heap을 강의 끝나는 시간을 갱신할때, 다른 비교없이 heappop만으로 끝낼 수 있기 때문이다.

'''
import sys
import heapq
N=int(sys.stdin.readline()) #회의수
s = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
s.sort(key=lambda x:(x[0],x[1])) #시작시간 기준으로 오름차순 정렬
heap = []
heapq.heappush(heap,s[0][1]) #제일 첫번째로 시작하는 수업의 종료시간을 우선순위큐(최소힙)에 삽입
for i in range(1,N):
    if heap[0] <= s[i][0]:
        heapq.heappop(heap) #종료시간갱신
    heapq.heappush(heap,s[i][1]) #강의추가
print(len(heap))

'''
입력예시)
3
1 3
2 4
3 5
출력예시)
2
'''

