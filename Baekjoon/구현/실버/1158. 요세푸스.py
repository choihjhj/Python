# 메모리: 31120  kb, 시간: 48 ms, 코드길이: 201 Bytes
'''실버4, 시간제한:2초, (1 ≤ K ≤ N ≤ 5,000)'''
N,K=map(int, input().split())
s=list(range(1,N+1))
index, result = 0, []
while len(s) > 0:
    index = (index + K - 1) % len(s) # 핵심 Point!!
    result.append(str(s.pop(index))) #str로 변환해서 결과에 넣어야 나중에 문자열 join 해서 출력가능
print('<' + ', '.join(result) + '>')

'''
입력예시)
7 3
출력예시)
<3, 6, 2, 7, 5, 1, 4>
'''

'''처음풀이-> while + for문 써서 시간초과
N,K=map(int, input().split())
s=list(range(1,N+1))
result=[]
while len(s)!=0:
    for _ in range(K-1):
        s.append(s.pop(0))
    result.append(str(s.pop(0))) 
print('<' + ', '.join(result) + '>')
'''