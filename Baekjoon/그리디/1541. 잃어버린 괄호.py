# 메모리: 31120 kb, 시간: 44 ms, 코드길이: 144 Bytes
s=input().split('-')
sum=0
for i in s[0].split('+'):
    sum+=int(i)
for i in s[1:]:
    for j in i.split('+'):
        sum -= int(j)
print(sum)
'''
입력예시)
50-30-10-50+10
출력예시)
-50
'''