# https://www.acmicpc.net/problem/11004


N, K = map(int, input().split())
array = list(map(int, input().split()))
array = sorted(array)

print(array[K-1])
