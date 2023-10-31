'''브론즈1, 시간제한:2초
7난쟁이는 합이 100이다.
9명 중 진짜 7난쟁이를 찾는 문제. 
'''
# 메모리: 31120  kb, 시간: 40 ms, 코드길이: 200 Bytes
'''풀이1) combinations() 이용'''
import sys
import itertools
nan=[int(sys.stdin.readline()) for _ in range(9)]
for i in itertools.combinations(nan,7): #9명중 7명 뽑아서
    if sum(i)==100: #그중 합 100인 경우수 오름차순 후 출력
        for j in sorted(i):
            print(j)
        break

# 메모리: 31120  kb, 시간: 40 ms, 코드길이: 262 Bytes
'''풀이2) for문 이용'''   
import sys 
nan= [int(sys.stdin.readline()) for _ in range(9)]
sum=sum(nan)
for i in nan:
    for j in nan:
        if sum-i-j == 100 : #9난쟁이 중 2명뺀 키합이 100인 두명 찾기
            a=i
            b=j 
            break
nan.remove(a)
nan.remove(b)            
for i in sorted(nan):
    print(i)            

'''
입력예시)
20
7
23
19
10
15
25
8
13
출력예시)
7
8
10
13
19
20
23
'''