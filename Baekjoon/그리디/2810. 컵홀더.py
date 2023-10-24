# 메모리: 31120  kb, 시간: 40 ms, 코드길이: 169 Bytes
n = int(input()) # 좌석 수
seat = input() # 좌석 정보

couple = seat.count('LL') # 커플석의 개수

if couple <= 1: #만약 LL이 1개 또는 0개라면 사람의 수를 그대로 출력합니다. (모두 컵홀더 사용 가능)
    print(n)
else:
    print(n + 1 - couple) #만약 LL이 2개 이상이라면 count를 빼주고 1을 더해줍니다. (LL이 2개면 -1, LL이 3개면 -2 이므로)