# 메모리: 31120  kb, 시간: 40 ms, 코드길이: 94 Bytes
'''풀이1)'''
s=list(map(int,input()))
print("LUCKY" if sum(s[:len(s)//2])==sum(s[len(s)//2:]) else "READY")


# 메모리: 31120  kb, 시간: 40 ms, 코드길이: 132 Bytes
'''풀이2)'''
n=input()
s1=sum(int(x) for x in n[:len(n)//2])
s2=sum(int(x) for x in n[len(n)//2:])
if s1==s2: print('LUCKY')
else: print('READY')