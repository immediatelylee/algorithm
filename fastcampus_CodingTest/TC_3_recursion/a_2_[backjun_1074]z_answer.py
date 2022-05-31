import sys
input = sys.stdin.readline
result = 0


def solve(n, x, y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y+1 == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y + 1 == Y:
            print(result)
            return
        result += 1
        return
    # 여기서 n은 2**N을 의미한다.
    solve(n/2, x, y)
    solve(n/2, x, y + n/2)
    solve(n/2, x + n/2, y)
    solve(n/2, x + n/2, y + n/2)


N, X, Y = map(int, input().split())
solve(2**N, 0, 0)
