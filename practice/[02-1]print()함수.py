''' print() 함수의  +,- 출력 '''

age = 3
name = "강아지"
is_asult= age>=3

# + 는 str()로 변수 묶어줘야 문자열 형태로 변환됨
print("우리집 "+name+" 나이는 "+str(age)+"살 입니다. "+str(is_asult)) 

# , 는 str로 안바꿔줘도 되는 대신 앞에 띄어쓰기 추가됨 
print("우리집",name,"나이는",age,"살 입니다.",is_asult)