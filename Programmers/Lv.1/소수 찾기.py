'''풀이1) 에라토스테네스의 체 이용'''
def solution(n):
    arr=[True for _ in range(n+1)]
    answer=0
    for i in range(2,int(n**0.5)+1): #n제곱근이 n**0.5이므로
        if arr[i] :
            for j in range(i*2,n+1,i):
                arr[j]=False
    for i in range(2,n+1):
        if arr[i]: answer+=1
        
    return answer

'''풀이2) '''
def check_prime(num):
    if num == 1: return False
    else:
        for i in range(2,int(num**0.5)+1): #n제곱근이 n**0.5이므로
            if  num%i== 0: return False
    return True
def solution(n):
    answer=0   
    for i in range(2,n+1):
        if check_prime(i): answer+=1       
    return answer


'''풀이3) set() 이용'''
def solution(n):
    num=set(range(2,n+1)) # 2부터 n까지의 집합

    for i in range(2,n+1): 
        if i in num: # i가 num에 있으면
            num-=set(range(2*i,n+1,i)) # 집합 num에서 i의 배수 제외
    return len(num)


'''풀이4) list[] 이용'''
def solution(n):
    a = [False, False] + [True]*(n-1) # 0, 1 False(소수가 아니므로) / 2부터 소수라고 가정
    primes = [] # 소수
    
    for i in range(2, n+1):
        if a[i]: # 소수이면
            primes.append(i) 
            for j in range(2*i, n+1, i): # 2*i부터 n까지 i의 배수 False로 바꾸기
                a[j] = False
    return len(primes)