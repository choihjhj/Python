# 메모리: 57716  kb, 시간: 440 ms, 코드길이: 462 Bytes
'''실버3, 시간제한:2초'''
import sys
from collections import Counter
n=int(sys.stdin.readline())
s=tuple(int(sys.stdin.readline()) for _  in range(n))
s=sorted(s)
print(round(sum(s)/len(s))) #산술
print(s[len(s)//2]) #중앙값
counter=Counter(s).most_common(2)
if len(counter) == 1:
    result = counter[0][0]
elif counter[0][1] == counter[1][1]: #최빈값 같으면 두번째꺼 print
    result = counter[1][0]
else:
    result = counter[0][0]
print(result) #최빈값 두번째꺼
print(max(s)-min(s)) #최대최소차이


'''
입력예시1)
5
1
3
8
-2
2
출력예시1)
2
2
1
10
입력예시2)
1
4000
출력예시2)
4000
4000
4000
0
입력예시3)
5
-1
-2
-3
-1
-2
출력예시3)
-2
-2
-1
2
입력예시4)
3
0
0
-1
출력예시4)
0
0
0
1
'''