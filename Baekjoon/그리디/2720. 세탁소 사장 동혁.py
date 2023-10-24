# 메모리: 31120  kb, 시간: 100 ms, 코드길이: 136 Bytes
T=int(input())
dan=[25,10,5,1]
for _ in range(T):
    C=int(input())
    for i in dan:
        print(C//i,end=" ")       
        C%=i