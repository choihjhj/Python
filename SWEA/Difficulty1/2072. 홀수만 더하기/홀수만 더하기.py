T = int(input())
for test_case in range(1, T + 1):
    s=list(map(int, input().split()))
    sum=0
    for i in s:
        if i%2==1:
            sum+=i
    print('#'+str(test_case),str(sum))  
