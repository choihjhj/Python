# 메모리: 31120  kb, 시간: 44 ms, 코드길이: 127 Bytes
'''k원을 만드는 데 필요한 동전 개수의 최솟값'''
n,k=map(int,input().split())
s=[int(input()) for _ in range(n)]
cnt=0
for i in s[::-1]:
    cnt+=k//i
    k%=i
print(cnt)    