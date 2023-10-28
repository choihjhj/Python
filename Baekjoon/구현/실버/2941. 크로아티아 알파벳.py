# 메모리: 30840  kb, 시간: 72 ms, 코드길이: 150 Bytes
s=input()
cro=['c=','c-','dz=','d-','lj','nj','s=','z=']
for x in cro:
    if x in s:       
        s=s.replace(x,"*") # replace는 반환으로 받아줘야 함        
print(len(s))  
