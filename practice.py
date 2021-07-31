# fn = fn-1 1 + fn-2 00
N = int(input())

f = [0 for i in range(1000001)]
f[1] = 1
f[2] = 2

for i in range(3, N+1):
    f[i] = (f[i-1] + f[i-2]) % 15746

print(f[N])
