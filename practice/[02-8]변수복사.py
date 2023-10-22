'''자료형의 값을 저장하는 공간, 변수'''

# 얕은복사b=a vs 깊은복사c=b[:]
a=[1,2,3]
b=a #a,b 같은 주소
c=b[:] # 새로운 리스트 생성 , c,b주소다름
print(a is  b) #true ,같은주소니까(얕은복사)
print(a is c) #False ,다른주소니까(깊은복사)
a[0]=0
print(a,b,c) #[0, 2, 3] [0, 2, 3] [1, 2, 3]


[a, b] = ['python', 'life']
print(a,b) #python life

# 값 바꾸기
a,b=b,a
print(a,b) #life python