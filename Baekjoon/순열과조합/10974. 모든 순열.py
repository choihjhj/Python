# 메모리: 31120  kb, 시간: 152 ms, 코드길이: 124 Bytes
'''실버3, 시간제한:1초, N(1 ≤ N ≤ 8)
N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.
'''
import sys
import itertools
n=int(sys.stdin.readline())
for i in itertools.permutations(range(1,n+1),n):
    print(*list(i))

'''
입력예시)
3
출력예시)
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''