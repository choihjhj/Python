'''실버4, 시간제한:1초, (1 ≤ K ≤ 100,000)
첫 번째 줄에 정수 K가 주어진다.
이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며, 
정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
재민이가 최종적으로 적어 낸 수의 합을 출력한다. 최종적으로 적어낸 수의 합은 231-1보다 작거나 같은 정수이다.
'''
'''풀이1)'''
# 메모리: 31900  kb, 시간: 88 ms, 코드길이: 208 Bytes
import sys
k=int(sys.stdin.readline())
s=[]
for _ in range(k):
    num=int(sys.stdin.readline())
    if len(s)!=0 and num==0: s.pop()
    elif num==0 and len(s)==0: pass
    else: s.append(num)
print(sum(s))   
 
'''풀이2)'''
# 메모리: 31900  kb, 시간: 80 ms, 코드길이: 172 Bytes
import sys
k=int(sys.stdin.readline())
s=[]
for _ in range(k):
    num=int(sys.stdin.readline())
    if num: 
        s.append(num)
    else:
        s.pop()
print(sum(s)) 


'''
입력예시1)
4
3
0
4
0
출력예시1)
0
입력예시2)
10
1
3
5
4
0
0
7
0
0
6
출력예시2)
7
'''