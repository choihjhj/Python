'''
최대 K번 더하여 M번의 덧셈으로 가장 큰 수 만들기
단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다.
예를 들어 s=[3,4,3,4,3]이고 M=7 K=2일 때, 4+4+4+4+4+4+4로 maxSum=28이다.
'''

# 풀이1
N,M,K=map(int,input().split()) #5 8 3
s=list(map(int,input().split())) #2 4 5 4 6
maxSum=0
s.sort(reverse=True) #[6,5,4,4,2]
count = ((M // (K + 1)) * K) + (M % (K + 1))
maxSum+=s[0]*count
maxSum+=s[1]*(M-count)
print(maxSum)  

# 풀이2 
N, M, K = map(int, input().split())
S = list(map(int, input().split()))
S.sort()
first = S[0]  # 가장 큰 수
second = S[1]  # 두 번째 큰 수
total = 0
while True:
    for i in range(K):
        if M == 0:
            break  # 더하기 전에 M 체크
        total += first
        M -= 1
    if M == 0:
        break  # 두 번째 수 더하기 전에 M 체크
    total += second
    M -= 1
print(total)