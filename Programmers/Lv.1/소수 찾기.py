'''풀이1) '''
import math
n=26
def solution(n):
    arr=[True for _ in range(n+1)]
    answer=0
    for i in range(2,int(math.sqrt(n))+1):
        if arr[i] == True:
            j=2
            while i*j <= n:
                arr[i*j]=False
                j+=1
    for i in range(2,n+1):
        if arr[i]: answer+=1
        
    return answer


'''풀이2) set() 이용'''
def solution(n):
    num=set(range(2,n+1)) # 2부터 n까지의 집합

    for i in range(2,n+1): 
        if i in num: # i가 num에 있으면
            num-=set(range(2*i,n+1,i)) # 집합 num에서 i의 배수 제외
    return len(num)


'''풀이3) list[] 이용'''
def solution(n):
    a = [False, False] + [True]*(n-1) # 0, 1 False(소수가 아니므로) / 2부터 소수라고 가정
    primes = [] # 소수
    
    for i in range(2, n+1):
        if a[i]: # 소수이면
            primes.append(i) 
            for j in range(2*i, n+1, i): # 2*i부터 n까지 i의 배수 False로 바꾸기
                a[j] = False
    return len(primes)