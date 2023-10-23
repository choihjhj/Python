# 순열
from itertools import permutations
data=['A','B','C']
result=list(permutations(data,3)) #3개 뽑아 3P3 모든 순열 구하기
print(result) 
#[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# 조합
from itertools import combinations
data=['A','B','C']
result=list(combinations(data,2)) #2개 뽑아 3C2 모든 조합 구하기
print(result) #[('A', 'B'), ('A', 'C'), ('B', 'C')]

# 중복 순열
from itertools import product
data=['A','B','C']
result=list(product(data,repeat=2)) #2개를 뽑는 모든 순열 구하기(중복 허용)

# 중복 조합
from itertools import combinations_with_replacement
data=['A','B','C']
result=list(combinations_with_replacement(data,2)) #2개를 뽑는 모든 조합 구하기(중복 허용)
