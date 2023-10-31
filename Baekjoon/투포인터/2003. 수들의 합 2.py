# 메모리: 32140  kb, 시간: 44 ms, 코드길이: 326 Bytes
'''실버4, 시간제한:0.5초'''
'''풀이1)'''
import sys
n,m=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().strip().split()))
end,cnt=0,0
interval_sum=0
for start in range(n):
    while end<n and interval_sum<m: #인덱스로 접근하는거니까 end<n
        interval_sum+=data[end]
        end+=1
    if interval_sum == m:
        cnt+=1
    interval_sum-=data[start]
print(cnt)

# 메모리: 32140  kb, 시간: 48 ms, 코드길이: 380 Bytes
# '''풀이2)'''
# import sys
# n,m=map(int,sys.stdin.readline().split())
# data=list(map(int,sys.stdin.readline().strip().split()))
# start,end,sum,cnt=0,0,0,0
# while end <= n:
#     if sum == m:
#         cnt += 1
#         sum -= data[start]
#         start += 1
#     elif sum < m:
#         if end < n:
#             sum+=data[end]
#         end+=1
#     elif sum>m:
#         sum-=data[start]
#         start+=1
# print(cnt)
'''
입력예시1)
4 2
1 1 1 1
출력예시1)
3
입력예시2)
10 5
1 2 3 4 2 5 3 1 1 2
출력예시2)
3
'''