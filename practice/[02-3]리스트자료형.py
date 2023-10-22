''' 리스트 자료형 '''
a=list()
b=[]

n1=[1,2,3]
n2=[4,5,6]
print(n1+n2) #[1, 2, 3, 4, 5, 6]
print(n1*2) #[1, 2, 3, 1, 2, 3]

# del , remove() 리스트 요소 삭제
del n1[:1] 
print(n1) #[2, 3]
c=[1,2]
c.remove(1) #[2] , 괄호안에 있는 데이터값을 가장 먼저 나온 것만 삭제하는 것, 요소index삭제가 아니고 데이터삭제임!!


# append(), insert() 리스트에 요소 추가하기
n1.append('a')
print(n1) #[2, 3, 'a']
n1.insert(3,'b')
print(n1) #[2, 3, 'a', 'b']

# sort() 정렬, 정렬뒤집기는 reverse()
n2.reverse()
print(n2) #[6, 5, 4]

# pop() 리스트 요소 빼내기
n2.pop() #[6, 5], 맨뒤꺼 빼내기
n2.pop(0) #[5], 0번째 빼내기

# count() 리스트 데이터개수세기
print(n2.count('a')) #0
