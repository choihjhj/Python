''' 딕셔너리 자료형 
{key,value} 
순서 없음
key에 리스트[] 쓸 수 없음
'''
a=dict()
b={}
print(type(a),type(b)) #<class 'dict'> <class 'dict'>

# 딕셔너리에 쌍 추가하기
a={1:'a'}
a[2]='b'
print(a) #{1: 'a', 2: 'b'}

# del 딕셔너리에 요소 삭제하기
del a[2]
print(a) #{1: 'a'}

# list(keys()) 키들로 리스트 만들기, list(values()) 값으로 리스트 만들기
n={'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(list(n.keys())) #['name', 'phone', 'birth']
print(list(n.values())) #['pey', '010-9999-1234', '1118']
print(list(n)) #['name', 'phone', 'birth']

# items() Key, Value 쌍 얻기
print(n.items()) #dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')])

# clear() Key: Value 쌍 모두 지우기
n.clear()
print(n) #{}

# get() key로 value 얻기
'''print(n['name'])''' #오류발생
print(n.get('name')) #none

# 키 in dict 딕셔너리안에 키 있는지 없는지 true,false 리턴
print('a' in n) #False
