# 풀이1) 재귀
def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
    
print(gcd(192,162))    #6

# 풀이2) math.gcd() 이용
import math
print(math.gcd(192,162)) #6