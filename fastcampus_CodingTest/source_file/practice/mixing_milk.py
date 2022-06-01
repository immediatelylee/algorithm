C, M = list(), list()

for i in range(3):
    a, b = map(int, input().split())
    # C,M 따로 관리 하면 가독성이 높하진다.
    C.append(a)
    M.append(b)

# start지점은 중요하지 않다. 모듈러 연산을통해서 지정함.
for i in range(100):
    idx = i % 3
    nxt = (idx+1) % 3

    M[idx], M[nxt] = max(M[idx]-(C[nxt]-M[nxt]),
                         0), min(C[nxt], M[nxt] + M[idx])

for i in M:
    print(i)
