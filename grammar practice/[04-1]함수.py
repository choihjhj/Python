''' 함수
def 함수_이름(매개변수):
    수행할_문장1
    수행할_문장2
    return 리턴값
*매개변수 는 매개변수여러개들어올때    
'''

# **kwargs 키워드 매개변수는 ‘keyword arguments’의 약자
def print_kwargs(**kwargs):
    print(kwargs) #{'age': 3, 'name': 'foo'}
print_kwargs(name='foo', age=3)    

def add_and_mul(a,b):
    return a+b, a*b
a,b=add_and_mul(2,5) #(,) 하나의 튜플로 반환
print(a,b) #7 10


# lambda 람다 , def 대신 쓰는 것
add = lambda a, b: a+b
print(add(1,2)) #3