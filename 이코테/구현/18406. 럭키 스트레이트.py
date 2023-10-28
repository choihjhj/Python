# 메모리: 31120  kb, 시간: 40 ms, 코드길이: 105 Bytes
'''풀이1)'''
n=list(map(int,input()))
if sum(n[:len(n)//2]) == sum(n[len(n)//2:]): print('LUCKY')
else: print('READY')


# 메모리: 31120  kb, 시간: 40 ms, 코드길이: 132 Bytes
'''풀이2)'''
n=input()
s1=sum(int(x) for x in n[:len(n)//2])
s2=sum(int(x) for x in n[len(n)//2:])
if s1==s2: print('LUCKY')
else: print('READY')