memo = [0] * 100


def fibo(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    if memo[x] != 0:
        return memo[x]
    memo[x] = fibo(x - 1) + fibo(x - 2)
    return memo[x]


fibo(6)
