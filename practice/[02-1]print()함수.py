''' print() 함수의  +,- 출력 '''

age = 3
name = "강아지"
is_asult= age>=3

# + 는 str()로 변수 묶어줘야 문자열 형태로 변환됨
print("우리집 "+name+" 나이는 "+str(age)+"살 입니다. "+str(is_asult)) 

# , 는 str로 안바꿔줘도 되는 대신 앞에 띄어쓰기 추가됨 
print("우리집",name,"나이는",age,"살 입니다.",is_asult)


# sep=""중간중간붙이기, end=""맽끝에붙이기
print('a','b','c',sep="::") #a::b::c 콤마끼리는 띄어쓰기인데 띄어쓰기 대신 '::'넣는것
print('a','b','c') # print('a','b','c',sep=" ") 라는 뜻
print('a','b','c',end="끝\n") #a b c끝
print('a','b','c',sep="::",end="끝") #a::b::c끝