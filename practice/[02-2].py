# ** 제곱 연산자
# /  나눗셈 연산자
# %  나머지 연산자
# // 몫 연산자 

# 문자열*숫자 하면 문자열에 숫자 곱한만큼 나옴
print(len('a'*5)) #aaaaa로 5나옴

a = "Life is too short, You need Python"
print(a[:4],a[5:],a[:]) #Life is too short, You need Python Life is too short, You need Python출력

n=10
day="three"
print("I ate %d apples. so I was sick for %s days." % (n, day)) #I ate 10 apples. so I was sick for three days.
print(f"I ate {n} apples. so I was sick for {day} days.")

d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

# %10s 오른쪽정렬후 10칸 나머지공백
# %-10s 왼쪽정렬후 10칸 나머지공백
print("%-10sjane." % 'hi') #hi        jane.
print(f'{"hi":=<10}') #왼쪽정렬 후 공백 '=' 채우기,    hi========
print(f'{"hi":=>10}') #오른쪽정렬 후 공백 '=' 채우기,  ========hi
print(f'{"hi":=^10}') #가운데정렬 후 공백 '=' 채우기,  ====hi====

# %전체글자수.소수점자리까지표현f
print("%10.4f" % 3.42134234) #    3.4213

''' 문자열관련함수'''
# len() 문자열 길이 함수 
# %% 퍼센트 출력하고 싶으면 두개써야함

# count() 문자 개수 세기
print('abbc'.count('b')) #2 출력

# find(), index() 위치 알려 주기
print('abbc'.find('b')) #1 출력, 처음나온위치출력, 없으면 -1반환
print('abc'.index('b')) #1 출력, 처음나온위치출력, 없으면 오류발생

# join() 문자열 삽입
print(','.join('abcd')) #a,b,c,d 출력

# upper() 소문자를 대문자로 바꾸기
# lower() 대문자를 소문자로 바꾸기
print('hi'.upper(), 'HI'.lower()) #HI hi

# lstrip() 왼쪽공백지우기, rstrip() 오른쪽공백지우기, strip() 양쪽공백지우기
print(' hi '.lstrip()+","+' hi '.rstrip()+','+' hi '.strip()) #hi , hi,hi

# replace() 문자열 바꾸기
print('Life is too short'.replace('Life','Time')) #Time is too short

# split() 문자열 나누기
print("Life is too short".split()) #['Life', 'is', 'too', 'short'], 괄호안에 지정 안해주면 공백or엔터or탭 기준으로 나눔
print("a:b:c:d".split(':')) #['a', 'b', 'c', 'd']