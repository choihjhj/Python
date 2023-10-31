# 메모리: 31120  kb, 시간: 40 ms, 코드길이: 377 Bytes
'''골드5, 시간제한:2초
'''
from itertools import combinations
L, C = map(int, input().split())  # l: 암호 길이, c: 알파벳 개수
pwd = sorted(list(input().split()))
for c in combinations(pwd, L) :
    cnt = 0
    for i in c:
        if i in 'aeiou':
            cnt += 1
    if (cnt >= 1) and (cnt <= L-2):  # 암호 중에서 모음이 1자 이상, 자음이 2자 이상
        print(''.join(c))
'''
입력예시)
4 6
a t c i s w
출력예시)
acis
acit
aciw
acst
acsw
actw
aist
aisw
aitw
astw
cist
cisw
citw
istw
'''