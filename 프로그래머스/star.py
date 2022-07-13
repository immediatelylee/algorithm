import sys
A, B = map(int, sys.stdin.readline().split())
X = list(map(int, sys.stdin.readline().split()))

for i in range(len(X)):
    if B > X[i]:
        print(X[i], end=' ')
