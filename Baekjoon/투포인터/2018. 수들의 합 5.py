'''실버5, 시간제한:2초, N(1 ≤ N ≤ 10,000,000)
입력된 자연수 N을 몇 개의 연속된 자연수의 합으로 나타내는 가지수를 출력하시오
O(nlogn)도 살짝 위험함. 따라서 투포인터O(n)을 사용해야함.
'''
# 메모리: 31120  kb, 시간: 3920 ms, 코드길이: 210 Bytes
'''풀이1)'''
import sys
n=int(sys.stdin.readline()) #15
sum,end,cnt=0,0,0
for start in range(1,n+1):
    while end<=n and sum<n: #숫자로 접근하는거니까 end<=n
        sum+=end
        end+=1
    if sum==n:
        cnt+=1
    sum-=start
print(cnt) #4           


# 메모리: 31120  kb, 시간: 4540 ms, 코드길이: 263 Bytes
''' 풀이2) '''
# import sys
# n = int(sys.stdin.readline())
# cnt,sum = 0,0
# start, end = 0,0
# while end<=n:
#     if sum < n:
#         end += 1
#         sum += end
#     elif sum > n:
#         sum -= start
#         start += 1
#     else:
#         cnt+=1
#         end+=1
#         sum+=end
# print(cnt)


# 메모리: 31120  kb, 시간: 4948 ms, 코드길이: 311 Bytes
''' 풀이3)'''
# import sys
# N=int(sys.stdin.readline())
# start,end,sum=1,1,1 #N이 1부터시작하니까 sum=1
# cnt=1 #자기자신 카운트
# while end!=N:
#     if sum==N:
#         cnt+=1
#         end+=1
#         sum+=end
#     elif sum>N:
#         sum-=start
#         start+=1
#     else:
#         end+=1
#         sum+=end
# print(cnt)  #4      

'''
입력예시)
15
출력예시) #15,7+8,4+5+6,1+2+3+4+5
4
'''