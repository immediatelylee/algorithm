result = 0


def z_move(n, x, y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        if x == X and y+1 == Y:
            print(result)
            return
        if x+1 == X and y == Y:
            print(result)
            return
        if x+1 == X and y+1 == Y:
            print(result)
            return
        return
    z_move(n/2, x, y)
    z_move(n/2, x, y+n/2)
    z_move(n/2, x+n/2, y)
    z_move(n/2, x+n/2, y+n/2)


N, X, Y = map(int, input().split())
z_move(2**N, 0, 0)
