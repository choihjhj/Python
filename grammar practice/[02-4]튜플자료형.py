''' 튜플 자료형 
리스트와 달리 수정, 삭제 안됨
그래서 보통 리스트를 더 많이 씀
''' 
t1=()
t2=tuple()
t3=1,2,3 #괄호 없어도 됨
print(t3*2) #(1, 2, 3, 1, 2, 3)
print(t3+(1,2,3)) #(1, 2, 3, 1, 2, 3)
