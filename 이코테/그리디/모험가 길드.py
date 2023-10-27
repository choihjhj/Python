'''난이도1, 시간제한:1초 ,(1<=N<=100,000)
공포도X에는 X명이상의 모험가가 참여해야 한다. 여행을 떠날 수 있는 그룹 수의 최댓값을 출력하라.
오름차순정렬 후 cnt하면서 참여자수가 새로운 공포도보다 크거나 같으면 그룹 체인지
'''
import sys
n=int(sys.stdin.readline())
s=list(map(int,sys.stdin.readline().split())) #공포도가진 사람들
s.sort()
cnt=0 #그룹 속 참여자수
result=0 #총 그룹수
for X in s: #1 2 2 2 3
    cnt+=1 #공포도X만큼 참여자수 계속 증가
    if cnt>=X: #공포도X만큼 인원이 차면 result,cnt 갱신        
        result+=1 # X가 1(0번째),2(2번째)일 때 증가함
        cnt=0 

print(result)  
'''
입력예시)
5
2 3 1 2 2
출력예시)
2
'''              
