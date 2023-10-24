# 힌트: 거슬러 줘야 할 동전의 최소 개수를 구하라.
'''큰 단위가 작은 단위의 배수 형태라 정당한 풀이
만약, d=[500,400,100]이고 N=800일 때,
아래 풀이로 하면 500,100,100,100 cnt=4가 나온다.
하지만 400,400 cnt=2가 나와야 하므로 작은 단위가 큰 단위의 배수형태가 아니라면
그리디 알고리즘이 아닌 다이나믹 프로그래밍으로 해결할 수 있다.
'''
d=[500,100,50,10] 
N=int(input()) #1260
cnt=0
for i in d:
    cnt += N//i
    N %= i
print(cnt) #6 500,500,100,100,50,10