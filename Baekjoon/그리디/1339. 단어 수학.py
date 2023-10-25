# 메모리: 31120 kb, 시간: 44 ms, 코드길이: 403 Bytes
'''골드 4'''
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