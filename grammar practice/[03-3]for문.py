''' for문
for 변수 in 리스트(또는 튜플, 문자열):
    수행할_문장1
    수행할_문장2

변수 사용없는 반복문 실행할 땐, 변수대신 _언더바로 쓰기
for _ in range(3):
    print('hello')    
'''
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: 
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print('')        


# 리스트 컴프리헨션
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result) #[6, 12]

result=[i*j for i in range(2,10)
            for j in range(1,10)]
print(result) #[2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]
