import time
start = time.time()


N, M = map(int, input().split())

array = [min(list(map(int, input().split()))) for i in range(N)]

print(max(array))

print(time.time()-start)
