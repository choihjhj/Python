# 메모리: 31120 kb, 시간: 40 ms, 코드길이: 504 Bytes
'''골드 4, 시간제한:2초,  N은 50보다 작은 자연수 , 수열의 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다. 
수를 합이 최대가 나오게 묶었을 때 합을 출력한다. 
문제풀이)
최적의 해를 구하는 그리디 문제이다.
이 문제는 양수와 음수, 0과 1을 생각해 주어야한다.
-양수의 경우 가장 큰 수를 기준으로 정렬하여 곱했을 때, 큰 값이 나온다.
-음수의 경우 가장 작은 수를 기준으로 정렬하여 곱했을 때, 큰 값이 나온다. (-3, -2, -1,.. 순)
-1은 무조건 더해주는 것이 수를 크게 만든다.
-0의 경우는 음수들을 다 묶고 남은 것이 있을 때 그 값을 더하게 되면 결과값이 작아지므로 마지막으로 남은 음수값을 0과 곱한다.
남은 음수값과 0을 곱하기 위해선 0을 음수 데이터 배열에 넣어주면 된다. 가장 끝에 배치되므로 0이 남으면 더해지고 남는 음수값이 생기면 자동으로 곱해진다.
'''
import sys
result=0
def sol(arr):
    global result
    for i in range(0, len(arr), 2): 
        if i+1 >= len(arr):
            result += arr[i]
        else:
            result += (arr[i] * arr[i+1])
N=int(sys.stdin.readline())
plus=[]
minus=[]
for _ in range(N):
    n=int(sys.stdin.readline())
    if n>1:
        plus.append(n)
    elif n <= 0:
        minus.append(n)
    else: #1 일 때는 그냥 더하기
        result+=n
plus.sort(reverse=True)
minus.sort()
sol(plus)
sol(minus)
print(result)

'''
입력예시1)
4
-1
2
1
3
출력예시1)
6

입력예시2)
6
0
1
2
4
3
5
출력예시2)
27

입력예시3)
1
-1
출력예시3)
-1

입력예시4)
3
-1
0
1
출력예시4)
1

입력예시5)
2
1
1
출력예시5)
2
'''
        
