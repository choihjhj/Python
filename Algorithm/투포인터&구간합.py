### [알고리즘] 투 포인터 알고리즘(부분합) -완전탐색O(N^2)을 O(N)으로 개선
'''
* 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리하는 알고리즘 (정렬되어 있지 않음)*

구현방법)
1. 시작점(start)과 끝점(end)이 첫 번째 원소의 인덱스(0)을 가리키도록 한다.
2. 현재 부분합이 M과 같다면 카운트한다.
3. 현재 부분합이 M보다 작으면 end를 1 증가시킨다.
4. 현재 부분합이 M보다 크면 start를 1 증가시킨다.
5. 모든 경우를 확인할 때까지 2번부터 4번까지의 과정을 반복한다.

예시) [1,2,3,2,5] 에서 부분합이 5인 부분 연속 수열의 수는 몇개인지 계산해보기.
start,end 모두 1가라킴, M=5
interval_sum=0+1, end=1
interval_sum=0+1+2 end=2
interval_sum=0+1+2+3 end=3
while 조건식에 안맞고, if문도 안맞아서 그 아래 interval_sum=6-1
while 조건식에 안맞는데,if문 맞으니까 cnt=1 증가 후 아래 interval_sum=5-2
interval_sum=3+2, end=4
while 조건식에 안맞는데, if문 맞으니까 cnt=2, 아래 interval_sum=5-3
interval_sum=2+5, end=5
while 조건식에 안맞고, if문도 안맞아서 그 아래 interval_sum=7-2
while 조건식에 안맞는데, if문 맞으니까 cnt=3, 아래 interval_sum=5-5
print결과 cnt=3
'''
### 소스코드 구현
#풀이1) 
n,m=5,5 #n데이터개수, m찾고자하는부분합
data=[1,2,3,2,5]
cnt=0
interval_sum=0
end=0
for start in range(n):
    while end<n and interval_sum<m:
        interval_sum+=data[end]
        end+=1
    if interval_sum == m:
        cnt+=1
    interval_sum-=data[start]
print(cnt)          

#풀이2) -근데 이건 너무 복잡하고 오래걸림 풀이1로 하기
sum,cnt,start,end=0,0,0,0
data=[1,2,3,2,5]
n,m=5,5 #n데이터개수, m찾고자하는부분합
while end <= n:
    if sum == m:
        cnt += 1
        sum -= data[start]
        start += 1
    elif sum < m:
        if end < n:
            sum+=data[end]
        end+=1
    elif sum>m:
        sum-=data[start]
        start+=1
print(cnt)  #3      

# 정렬된 리스트 A,B 합치기-병합정렬에서도 쓰임, 시간복잡도O(n+m) -----------------------------------------------
'''
구현방법)
1. 정렬된 리스트 A,B를 입력받는다.
2. 리스트 A에서 처리되지 않은 원소 중 가장 작은 원소를 i가 가리키도록 한다.
3. 리스트 A에서 처리되지 않은 원소 중 가장 작은 원소를 j가 가리키도록 한다.
4. A[i]와 B[j] 중에서 더 작은 원소를 결과 리스트에 저장한다.
5. 리스트 A,B에서 더 이상 처리할 원소가 없을 때까지 2-4번의 과정을 반복한다.
'''
### 소스코드 구현)
n,m=3,4
a=[1,3,5]
b=[2,4,6,8]
result=[0]*(n+m)
i,j,k=0,0,0
while i<n or j<m:
    if j >=m or (i<n and a[i] <= b[j]):
        result[k]=a[i]
        i+=1
    else:
        result[k]=b[j]
        j+=1
    k+=1
print(*result)   #1 2 3 4 5 6 8



# 구간 합 계산 알고리즘----------------------------------------------------------------------------------------
'''
구현방법)
1. N개의 수에 대하여 접두사 합을 계산하여 배열 P에 저장한다.
2. 매 M개의 쿼리정보[L,R]을 확인할 때, 구간합은 P[R]-P[L-1]이다.
'''
### 소스코드 구현)
n=5 #데이터 개수
data=[10,20,30,40,50]
left,right=3,4 #3번째부터 4번째 구간 합
sum_value=0
prefix_sum=[0]
for i in data:
    sum_value +=i
    prefix_sum.append(sum_value)
print(prefix_sum[right]-prefix_sum[left-1])  #70
