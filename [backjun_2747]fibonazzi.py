# https://www.acmicpc.net/problem/2747


Fibonazzi = [0, 1] + [0 for i in range(45)]
N = int(input())

for i in range(2, N+1):
    Fibonazzi[i] = Fibonazzi[i-1]+Fibonazzi[i-2]

print(Fibonazzi[N])
