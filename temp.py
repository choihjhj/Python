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