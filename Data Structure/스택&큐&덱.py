# [자료구조] 스택 & 큐
''' 
# 스택 (stack)
LIFO(Last In First Out)
  
파이썬 내장모듈에서는 따로 스택 라이브러리가 존재하지 않는다.

# 큐 (queue)
FIFO(First In First Out) 선착순   


보통 스택과 큐는 list로 구현하여 사용한다. 하지만, list보다 deque 라이브러리가 훨씬 빠르기 때문에
웬만하면, 스택이든 큐든 append,pop해야할 때는 from collections import deque 사용하기!!!!
- dequeue은 stack+ queue 합친 것   
'''
# deque : list에서 앞뒤에서 삽입/삭제가 가능한 큐 (double-ended queue의 줄임말) ,list는 appendleft,popleft없음
from collections import deque
dq=deque() # 덱 생성  
dq.append('a') #dq.insert(0,'a') 랑 같은 뜻
dq.append('b') # dq=['a','b'] ,뒤로 삽입
dq.appendleft('c')  # dq=['c','a','b'] ,앞으로 삽입
dq.clear() # dq=[], 모든 원소 제거   

dq.append('*')
dq2=deque()
dq2=dq.copy() #dq2=['*'] ,얕은 복사

print(dq2.count('*')) #1

dq2.extend('t') #dq2=['*','t']
dq2.extendleft('a') #dq2=['a','*','t'] 

print(dq2.index('c',0,2)) #에러발생, index(x, start: int, stop: int) 없으면 에러

print(dq2.pop()) #t ,dq2=['a','*']
print(dq2.popleft()) #a ,dq2=['*']

dq2.reverse() #뒤집기 dq=['*']
 
'''공식문서 : https://docs.python.org/3.8/library/collections.html#collections.deque'''

