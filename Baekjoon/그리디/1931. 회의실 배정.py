# 메모리: 59068  kb, 시간: 4296 ms, 코드길이: 235 Bytes
''' 최대 사용할 수 있는 회의의 최대 개수를 출력한다.
끝나는 시간 오름차순 정렬해서 푸는 것이 회의개수를 최대화 할 수 있다.
'''
N=int(input()) #회의수
s = [list(map(int, input().split())) for _ in range(N)]
#s = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
s.sort(key=lambda x:(x[1],x[0])) #0번째 x부터 가져와서 끝시간기준으로 오름차순 정렬하라는 뜻, 우선순위 넣기위해 x[1],x[0]이라고 한 것
last_end = 0 
cnt=0
for start, end in s:
     if start >= last_end:
        cnt += 1
        last_end = end
print(cnt)        

