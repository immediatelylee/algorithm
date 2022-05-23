# https://www.acmicpc.net/problem/2739
N = int(input())

for i in range(9):
    print(N, "*", i+1, "=", N*(i+1))
