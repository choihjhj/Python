T = int(input())
don = [ [50000,0], [10000,0], [5000,0], [1000,0], [500,0], [100,0], [50,0], [10,0] ]
for tc in range(1,T+1):
    N=int(input())
    print(f"#{tc}")
    for m in don:
        m[1] = N//m[0]
        N -= m[0]*m[1]
        print(m[1],end=" ")
    print('')    
