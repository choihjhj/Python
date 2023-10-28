# 메모리: 31252  kb, 시간: 48 ms, 코드길이: 584 Bytes
import sys
n = int(sys.stdin.readline())
stack=[]
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
'''
입력예시1)
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
출력예시1)
2
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
7
pop
top
push 123
top
pop
top
pop
출력예시2)
-1
-1
123
123
-1
-1
'''