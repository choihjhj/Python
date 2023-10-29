'''실버5, 시간제한:1.5초
시간초과가 너무 타이트해서 반복문안에서의 실행을 최대한 신경써서 줄여야 한다.
집합이라고 나와있지만 꼭 set말고 list로 구현해도 된다.
for문 속 str() 이런거 있으면 또 그만큼 반복돼서 시간초과 발생 
최대한 반복문 내에서의 실행이나 중복코드는 바깥으로 빼거나 줄여야 한다.
'''
# 메모리: 31120  kb, 시간: 3332 ms, 코드길이: 655 Bytes
'''풀이1) '''
import sys
M=int(sys.stdin.readline())
s=[]
for _ in range(M):
    command=sys.stdin.readline().strip().split()
    if len(command)==1:
        if command[0]=='all':
            s=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
        else: #empty
            s=[]
    else:
        cmd,x=command[0],command[1]
        if cmd == 'add': 
            if x not in s: s.append(x)
        elif cmd == 'remove': 
            if x in s: s.remove(x)
        elif cmd == 'check': 
            print('1' if x in s else '0')
        elif cmd == 'toggle': 
            if x in s: s.remove(x)
            else: s.append(x)
# 메모리: 31120  kb, 시간: 3820 ms, 코드길이: 600 Bytes
'''풀이2) '''
import sys
M=int(sys.stdin.readline())
s=set()
for _ in range(M):
    command=sys.stdin.readline().strip().split()
    if len(command)==1:
        if command[0]=='all':
            s=set(range(1,21))
        else: #empty
            s=set()
    else:
        cmd,x=command[0],command[1]
        x = int(x)
        if cmd == 'add': 
            if x not in s: s.add(x)
        elif cmd == 'remove': 
            if x in s: s.discard(x)
        elif cmd == 'check': 
            print('1' if x in s else '0')
        elif cmd == 'toggle': 
            if x in s: s.discard(x)
            else: s.add(x)
'''
입력예시1)
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1
출력예시1)
1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0
'''