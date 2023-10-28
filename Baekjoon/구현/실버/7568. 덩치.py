# 메모리: 31120  kb, 시간: 40 ms, 코드길이: 282 Bytes
'''실버5, 시간제한:1초
2 ≤ N ≤ 50
10 ≤ x, y ≤ 200
'''
import sys
n=int(sys.stdin.readline())
s=[tuple(map(int,sys.stdin.readline().split())) for _ in range(n)]
for i in s:
    rank = 1
    for another_student in s:
        if i[0] < another_student[0] and i[1] < another_student[1]: #키몸무게비교
                rank += 1
    print(rank, end = " ")

'''
입력예시)
5
55 185
58 183
88 186
60 175
46 155
출력예시)
2 2 1 2 5
'''