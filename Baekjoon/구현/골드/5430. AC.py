'''골드5, 시간제한: 1초
<주의사항>
R 명령이 들어온다고 진짜로 배열의 모든 원소를 뒤집으면 절대로 안 됩니다. N개의 원소의 순서를 정말로 바꾸면 당연히 그 원소 수만큼 시간이 걸리고, 그걸 최대 10만 번 수행해야 하니 테스트 케이스 1개만으로도 100억번의 연산이 수행됩니다. R 명령의 핵심은 실제로 원소를 뒤집지 않고도 뒤집힌 것과 같은 효과를 내도록 구현하는 것입니다. C++의 std::reverse(), Python의 a[::-1] 역시 사용해서는 안 됩니다.
D 명령에 대해서 보통 배열의 맨 앞 원소를 무작정 지워서는 안 됩니다. C++의 vector::erase(), Java의 ArrayList.remove(), Python의 list.pop() 등으로 배열의 첫 번째 원소를 지울 시, 그 뒤에 있는 모든 원소들을 전부 한 칸씩 앞으로 당겨오게 되므로, 그 시간 역시 원소의 수에 비례하여 소요됩니다. 라이브러리 함수는 호출만 하면 N개의 원소를 기적같이 O(1)에 처리해주는 마법사가 아닙니다. 저렇게 원소를 당겨오는 작업 없이도 D의 기능을 구현할 수 있어야 합니다.
빈 배열은 []로 출력해야 합니다. 아무것도 출력하지 않거나, error를 출력하거나, 무조건 원소를 하나 출력하고 시작하려고 하면 안 됩니다.
배열이 비어있는데 R을 하는 건 에러가 아닙니다. D만 에러입니다. 처음에 수가 0개여도 D가 없다면 error가 아닐 수 있습니다.
테스트 케이스마다 초기화가 잘 됐는지 확인하세요. 그리고 매 케이스마다 개행 문자를 항상 출력하는지 확인하세요.
처음 배열의 상태에 대한 문자열의 길이는 최대 400001자입니다. 입력 문자 배열 크기를 잘 설정하세요.
처음 배열의 상태로 빈 배열이 주어지는 경우를 조심하세요. 수가 무조건 하나 이상 있다고 가정하고 코드를 작성하면 이런 경우를 제대로 처리하지 못할 수 있습니다.
조건문 안에 strlen(str) 를 절대로 넣지 마세요. strlen은 문자열의 처음부터 널 문자가 나올 때까지 한 글자씩 확인하므로, 반복문을 한 바퀴 돌 때마다 문자열의 길이만큼의 시간이 걸립니다.
R과 D의 개수만 세고 나중에 몰아서 처리하면 안 됩니다. R을 할 때마다 D를 했을 때 지워지는 원소가 달라지기 때문입니다. [1,2,3] 배열에서 DRD 명령을 수행하면 어떻게 되어야 할지 생각해 보세요.
배열에 들어있는 수는 최대 100입니다. 무조건 한 글자로 가정하고 구현하면 안 됩니다. 참고로, 예제에도 두자리의 수가 하나 등장하지만 어차피 지워지는 원소이기 때문에 잘 나오는 것처럼 보일 수도 있으므로 실제로 두 자릿수를 정확하게 출력하는지 직접 예시를 만들어 출력해보아야 합니다. 대표적인 실수로, 답을 통째로 문자열로 저장해놓고 R 명령시 그대로 뒤집는 것이 있습니다. 이렇게 하면 각 수의 자릿수까지 잘못 뒤집어지게 되는 불상사가 발생합니다.
입출력 양식은 공백의 유무까지 정확하게 고려해야 합니다. 예제 입출력을 확인해 보세요. 배열의 수들 사이에는 공백이 없으며, 입력받을 때 공백이 있어야만 입력받을 수 있는 방밥을 쓰거나 출력할 때 임의로 공백을 삽입해서 출력하면 안 됩니다. 대표적인 예시로, Python에서 print(list)를 하면 원소들 사이에 불필요한 공백이 출력되어 틀립니다.

deque 안쓰고 그냥 list에 pop(0)이런식으로 쓰면
메모리: 41596  kb, 시간: 3624 ms, 코드길이: 742 Bytes 나옴.
확실히 deque이 list보다 훨씬 빠름. 스택이나 큐 이용해야할 때 되도록이면 deque 사용하기!!
'''

# 메모리: 42344  kb, 시간: 160 ms, 코드길이: 781 Bytes
'''풀이1)'''
import sys
from collections import deque

for test_case in range(int(sys.stdin.readline())):
    error = False
    reverse = False

    command_list = sys.stdin.readline().strip()
    num_cnt = int(sys.stdin.readline())
    num_list = deque(sys.stdin.readline().strip()[1:-1].split(","))

    if num_cnt == 0:
        num_list = deque()

    for command in command_list:
        if command == "R":
            if reverse:
                reverse = False
            else:
                reverse = True

        else:
            if num_list:
                if reverse:
                    num_list.pop()
                else:
                    num_list.popleft()
            else:
                error = True
                break

    if error:
        print("error")
    elif reverse:
        num_list.reverse()
        print("["+",".join(num_list)+"]")
    else:
        print("["+",".join(num_list)+"]")

'''풀이2)'''
# 메모리: 45536  kb, 시간: 204 ms, 코드길이: 662 Bytes
from collections import deque
T=int(input())
for _ in range(T):
    P=input()
    N=int(input())
    s=input()[1:-1].split(',') 
    queue = deque(s)
    flag = 0
    if N == 0:
        queue = []
    for i in P:
        if i =='R': flag += 1
        elif i=='D':
            if len(queue) == 0:
                print("error")
                break
            else:
                if flag % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    else:
        if flag % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")        
'''
입력예시)
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
출력예시)
[2,1]
error
[1,2,3,5,8]
error

'''
