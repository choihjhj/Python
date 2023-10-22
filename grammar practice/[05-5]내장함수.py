''' 내장함수 '''

# chr() 숫자를 문자로
print(chr(97)) #a

# ord() 문자를 숫자로
print(ord('a')) #97

# enumerate는 ‘열거하다’라는 뜻이다. 이 함수는 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
'''
0 body
1 foo
2 bar '''    

# filter(함수, 반복_가능한_데이터) 걸러내는함수, map(함수, 반복가능한데이터) 
a= list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))
b= [x for x in [1, -3, 2, 0, -5, 6] if x>0]
c= list(map(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))
print(a,c) #[1, 2, 6] [True, False, True, False, False, True]

# round(3.14) 반올림 round(3.14,0)과 같은의미 소수점0번째자리까지만 표시 나머지 반올림, round(3.143,2)은 3.14나옴
# floor(4.99) 내림함수 결과 4
# ceil(3.14) 올림함수 결과 4

# id() 주소반환
# oct() 8진수, hex() 16진수 
# sqrt(16) 4 제곱근함수

print(list(range(0, -10, -1))) #[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

# 리스트등.sort() vs sorted(리스트 등)
'''
리스트.sort() 하면 알아서 정렬해서 리스트에 저장되고,
sorted(리스트) 는 값이 저장 안 되기 때문에
리스트 = sorted(리스트) 라고 해줘야 한다.
'''

# randint(a,b) a<=~<=b
from random import *
print(randint(1,10)) #1부터10사이 아무숫자 나옴


# map()함수 여러개 데이터 한줄로 들어올 때 예:1 2 3 4 5
s=list(map(int,input().split()))
a,b=map(int, input().split())

# input() 문자열로 저장되니까 int면 int(input())으로 형변환해서 변수에 저장하기
