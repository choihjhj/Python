# 메모리: 31352  kb, 시간: 76 ms, 코드길이: 194 Bytes
'''실버5, 시간제한:2초
'''
import sys
input=sys.stdin.readline
n=int(input())
cnt=n
for _ in range(n):
    s=input().strip()
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            pass
        elif s[i] in s[i+1:]:
            cnt-=1
            break
print(cnt)
'''
입력예시1)
3
happy
new
year
출력예시1)
3
입력예시2)
4
aba
abab
abcabc
a
출력예시2)
1
입력예시3)
5
ab
aa
aca
ba
bb
출력예시3)
4
입력예시4)
2
yzyzy
zyzyz
출력예시4)
4
입력예시5)
1
z
출력예시5)
1
입력예시6)
9
aaa
aaazbz
babb
aazz
azbz
aabbaa
abacc
aba
zzaz
출력예시6)
2
'''