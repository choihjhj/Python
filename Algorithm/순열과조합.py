'''
수학 기본 개념
nPr=n!/(n-r)! #일렬로 줄세우는 것, 순서있음
nPr=nCr*n!
nCr=nPr!*n!
    =(n!/(n-r)!)n!
0!=1
nP1=n
nP0=1=nC0
공식 잘 안씀, 그냥 아래처럼 구하기
7P3= 7*6*5 
7C3=7*6*5/3! =7C4
4C2=4*3/2!=6 
6C3=6*5*4/3!=20
'''

### [알고리즘] 순열-------------------------------------------------------------------------------------------
''' 서로 다른 n개에서 r개를 선택하여 일렬로 나열하는 것 '''

from itertools import permutations
data=[1,2]
for x in permutations(data,2):
    print(list(x))
#[1,2] [2,1]

### [알고리즘] 조합-------------------------------------------------------------------------------------------
''' 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것 '''

from itertools import combinations
data=[1,2,3]
for x in combinations(data,2):
    print(list(x))
#[1,2] [1,3] [2,3]

# 중복 순열---------------------------------------------------------------------------------------------------
from itertools import product
data=['A','B','C']
result=list(product(data,repeat=2)) #2개를 뽑는 모든 순열 구하기(중복 허용)

# 중복 조합---------------------------------------------------------------------------------------------------
from itertools import combinations_with_replacement
data=['A','B','C']
result=list(combinations_with_replacement(data,2)) #2개를 뽑는 모든 조합 구하기(중복 허용)