# https://www.acmicpc.net/problem/1920

# dictionary 형
N, A = int(input()), {i: 1 for i in map(int, input().split())}
M = int(input())

for i in list(map(int, input().split())):
    print(A.get(i, 0))
    # print(1 if i in A else 0) # 삼항식으로 풀이

# key 에러가 출력된다. , dictionary는 키 값이 없으면 key error 이 나기 때문
# for i in list(map(int,input().split())):
#   print(A[i])


# dic에 어떻게 집어넣지?
# {i: 1 for i in map(int, input().split())}

# ddict = dict()
# for i in map(int, input().split()):
#     ddict[i] = 1

# print(ddict)
