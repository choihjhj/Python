# [서브태스크] 결과: 100점, 메모리: 31120  kb, 시간: 56 ms, 코드길이: 151 Bytes
s = [ 5*60, 1*60, 10 ]
T = int(input())
result = []
for i in s:
    result.append(T//i)
    T %= i
if T == 0:
    print(*result)
else:
    print(-1)