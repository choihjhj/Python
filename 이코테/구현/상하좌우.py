'''난이도1, 시간제한:1초
(1,1)에서 시작
L:왼쪽한칸이동
R:오른쪽한칸이동
U:위로한칸이동
D:아래로한칸이동
'''
move_types='LRUD'
dx=[0,0,-1,1] #L R U D
dy=[-1,1,0,0]
x,y=1,1
n=int(input())
plans=input().split()
for plan in plans:
    i=move_types.find(plan)
    if i != -1:
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>n or ny>n or nx<1 or ny<1: continue
        x,y=nx,ny
print(x,y)    
    

'''
입력예시)
5
R R R U D D
출력예시)
3 4
'''