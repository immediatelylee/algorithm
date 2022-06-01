
N = int(input())
G = [list(map(int, input().split())) for i in range(N)]


ans = 10000
dx, dy = [0, 0, 0, 1, -1], [0, 1, -1, 0, 0]  # 가만히 있는것도 추가한다.
# 3


# 2
def ck(lst):  # 꽃이 a,b,c에 있을때 비용
    ret = 0
    flow = []  # 꽃이 들어가는 것을 리스트로 저장
    for flower in lst:
        x = flower // N  # x (0~n-1)
        y = flower % N
        if x == 0 or x == N-1 or y == 0 or y == N-1:
            return 10000
        for w in range(5):
            flow.append((x+dx[w], y + dy[w]))  # 튜플로 진행 좌표평면에 set으로 진행하기 위해서
            ret += G[x+dx[w]][y + dy[w]]  # 위치와 꽃잎을 더함.
    if len(set(flow)) != 15:  # 겹치는것이 없어야 15칸이 된다.
        return 10000
    return ret

    # 1
for i in range(N*N):
    for j in range(i+1*N):
        for k in range(j+1, N*N):
            ans = min(ans, ck([i, j, k]))  # ck를 리스트로 받는다.

print(ans)
# 0*N + 0


# N의 제한이 10이고
# 꽃1개가 있을수 있는 전수조사 범위는 10*10 = 100 꽃이 3개가 있으려면 100 ^3  = 1000000
# 백만정도의 시간 복잡도는 전수조사를 하라는것임.


# x,y 를 표현할때 6중for 문으로 처리할수도 있지만
# 하나의 숫자로 표현한다면 3중 for 문으로 처리할수도 있다.
# 단일 반복문으로 진행할수도 있지만 가독성이 떨어지므로 하지 않은다.
