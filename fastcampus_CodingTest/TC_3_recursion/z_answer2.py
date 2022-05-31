N, r, c = map(int, input().split())


def Z(sz, x, y):
    if sz == 1:
        return 0
    sz //= 2
    for i in range(2):
        for j in range(2):
            if x < sz * (i+1) and y < sz * (j+1): #4분면찾기
                return (i*2 + j) * sz*sz + Z(sz, x-sz*i, y-sz*j) #return값으로 값 출력하기


print(Z(2**N, r, c))
