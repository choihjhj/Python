# 메모리: 31120 kb, 시간: 44 ms, 코드길이: 403 Bytes
'''골드 4,시간제한: 2초,  N(1 ≤ N ≤ 10)
N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.
알파벳은 최대 10개이고, 수의 최대 길이는 8이다
'''
import sys
input=sys.stdin.readline
s=[input().rstrip() for _ in range(int(input()))]
dict = {}
for w in s:
    cnt=len(w)-1
    for ww in w:
        if ww not in dict:
            dict[ww]=pow(10, cnt)
        else:
            dict[ww]+=pow(10, cnt)
        cnt -= 1
dict = sorted(dict.values(), reverse=True)
result = 0
num = 9
for v in dict:
    result += v*num
    num -= 1
print(result)          
'''
입력예시1)
2
AAA
AAA
출력예시1)
1998
입력예시2)
2
GCF
ACDEB
출력예시2)
99437
입력예시3)
10
A
B
C
D
E
F
G
H
I
J
출력예시3)
45
입력예시4)
2
AB
BA
출력예시4)
187
''' 