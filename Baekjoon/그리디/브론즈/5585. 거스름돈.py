# 메모리: 31120  kb, 시간: 40 ms, 코드길이: 97 Bytes
T=1000-int(input())
m=[500,100,50,10,5,1]
cnt=0
for i in m:
    cnt+=T//i
    T%=i
print(cnt)    