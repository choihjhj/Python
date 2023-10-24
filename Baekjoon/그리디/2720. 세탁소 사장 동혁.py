# 메모리: 31120  kb, 시간: 84 ms, 코드길이: 143 Bytes
T=int(input())
dan=[25,10,5,1]
for _ in range(T):
    C=int(input())
    for i in dan:
        print(C//i,end=" ")       
        C-=(i*(C//i))