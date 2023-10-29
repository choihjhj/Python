# 메모리: 34028  kb, 시간: 72 ms, 코드길이: 494 Bytes
'''실버3, 시간제한:2초,N(1 ≤ N ≤ 100),(0 ≤ M < N)'''
from collections import deque
import sys
T=int(input())
for _ in range(T):
    n,m=map(int,sys.stdin.readline().split())
    queue=deque(list(map(int, sys.stdin.readline().split())))
    count =0
    while queue:
        best = max(queue)
        front = queue.popleft()
        m -= 1 # 내 위치가 한 칸 당겨진다.
        if best == front:
            count += 1
            if m < 0: # m이 0이라는 것은 뽑은 숫자가 내 숫자라는 뜻.
                print(count)
                break
        else:
            queue.append(front)
            if m < 0: m= len(queue) - 1 # 제일 앞에서 뽑히면 제일 뒤로 이동




'''
입력예시)
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
출력예시)
1
2
5
'''