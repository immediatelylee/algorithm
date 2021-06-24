# https://www.acmicpc.net/problem/1920
# 해시,배열,구현문제
N, A = int(input()), {i: 1 for i in map(int, input().split())}
M = int(input())

print(A)

for i in list(map(int, input().split())):
    print(A.get(i, 0))
    # print(1 if i in A else 0)

'''
dict 와 get함수 이용함
dict의 경우는 key값 을 i로 두고  value를 1로 초기화 하는데 쓰인 문법에 주목
python에서는 dictionary 자료형을 해시처럼 사용할수 있음.

'''
