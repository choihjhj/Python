# 메모리: 31120  kb, 시간: 92 ms, 코드길이: 176 Bytes
case=1
while True:
    L,P,V=map(int,input().split())
    if L==0 and P==0 and V==0: break
    a=V//P
    b=V%P #남은일수
    if L<b: b=L #남은일수가 캠핑장을 이용할 수 있는 일수(L)보다 많이 남았다면 이용할 수 있는 날만큼만 이용하게 된다.
    print(f'Case {case}:',(L*a + b))
    case+=1