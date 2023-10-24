''' 조건1,2를 통해 n을 1로 만드는 최소횟수 구하기
조건1. n에서 1을 뺀다
조건2. n을 k로 나눈다
'''
n,k=map(int,input().split()) #25 3
result=0
while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 1씩 빼기
    target = (n // k) * k # n을 k로 가장 나누어 떨어지는데 가까운 수로 target저장
    result += (n - target) # 조건1을 수행했으면 target과 n의 차이가 1이 되므로(target은 n이k로 나누어떨어지는 가장 가까운수니까) result가 +1이 된다.
                           # 만약 n이 k로 나누어 떨어지면 n-target이 0이므로 result는 +0이 되어 카운트가 안된다.
    n = target             # n을 일단 target 즉 n을 k로 나누기 가장 좋은 수로 변경

    # n이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break               #마지막에 target=(1//k)*k 하면 target이 0이 되는 시점이 온다. 그럼 0<k이므로 break

    result += 1  # k를 나누는 연산을 수행하므로 1번 추가, 아래의 조건2 수행하니까 수행횟수 증가
    n //= k                                             #조건2 수행

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

'''
예) n=25, k=5 [결과 2]

반복문 실행1
target=(25//5)*5 #25
result=0+(25-25) #0
n=25
if 25<5 아니므로 수행X
result=0+1 #1
n=25//5 #5
반복문 실행2
target=(5//5)*5 #5 
result=1+(5-5) #1
n=5
if 5<5 아니므로 수행X
result=1+1 #2
n=5//5 #1
반복문 실행3
target=(1//5)*5 #0
result=2+(1-0) #3
n=0
if 0<5 이므로 while문 break
	
result=3+(0-1) #2
print(result) #2
'''

'''
예) n=17, k=4 ,결과 3
반복문 실행1
target=(17//4)*4 #16
result=0+(17-16) #1
n=16
if 16<4 아니므로 수행X
result=1+1 #2
n=16//4 #4
반복문 실행2
target=(4//4)*4 #4
result=2+(4-4) #2
n=4
if 4<4 아니므로 수행X
result=2+1 #3
n=4//4 #1
반복문 실행3
target=(1//4)*4 #0
result=3+(1-0) #4
n=0
if 0<4이므로 while문 break

	
result=4+(0-1) #3
print(result) #3
'''