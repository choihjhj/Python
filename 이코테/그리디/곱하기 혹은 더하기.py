'''난이도1, 시간제한:1초 ,(1<=S의 길이<=20)
+,x 를 이용해서 가장 큰 수 만들기
핵심은 0또는1 일때는 덧셈하고 나머지는 곱셈하면 큰 수 만들 수 있음
'''
'''내 풀이)'''
import sys
s=list(sys.stdin.readline().strip())
result1=0
result2=1
for i in s:
    i=int(i)
    if i<=1: #if i<=1 or result1<=1: 이렇게 했다가 result2변수 추가해서 없앰 
        result1+=i
    else:
        result2*=i
print(result1+result2)     

'''책 풀이)'''
import sys
s=list(sys.stdin.readline().strip())
result=int(s[0]) #이게 point
for i in s[1:]:
    i=int(i)
    if i<=1 or result<=1:
        result+=i
    else:
        result*=i
print(result) 

'''
입력예시1)
02984
출력예시1)
576
입력예시2)
567
출력예시2)
210
'''