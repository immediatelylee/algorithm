
from collections import deque

f, s, g, u, d = map(int, input().split())

visited = [0 for _ in range(f+1)]


def bfs():
    que = deque()
    que.append(s)
    visited[s] = 1

    while que:
        floor = que.popleft()
        if floor == g:
            return visited[g]-1
        # up
        if floor+u <= f and not visited[floor+u]:  # 조건 주의
            que.append(floor+u)
            visited[floor+u] = visited[floor]+1
        # down
        if floor-d >= 1 and not visited[floor-d]:
            que.append(floor-d)
            visited[floor-d] = visited[floor]+1

    return "use the stairs"


print(bfs())
