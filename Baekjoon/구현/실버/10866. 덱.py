# 메모리: 31120  kb, 시간: 52 ms, 코드길이: 867 Bytes
'''실버4, 시간제한:0.5초
큐,스택은 모두 list로 구현하기, insert() append() pop()
'''
import sys
n=int(sys.stdin.readline())
queue = []
for _ in range(n):
    command=sys.stdin.readline().split()
    if command[0]=='push_back':
        queue.append(command[1])
    elif command[0]=='push_front':
        queue.insert(0,command[1])
    elif command[0]=='pop_front':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif command[0]=='pop_back':
        if queue:
            print(queue.pop(-1))
        else:
            print(-1)
    elif command[0]=='size':
        print(len(queue))
    elif command[0]=='empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command[0]=='front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0]=='back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
'''
입력예시1)
15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front
출력예시1)
2
1
2
0
2
1
-1
0
1
-1
0
3
입력예시2)
22
front
back
pop_front
pop_back
push_front 1
front
pop_back
push_back 2
back
pop_front
push_front 10
push_front 333
front
back
pop_back
pop_back
push_back 20
push_back 1234
front
back
pop_back
pop_back
출력예시2)
-1
-1
-1
-1
1
1
2
2
333
10
10
333
20
1234
1234
20
'''