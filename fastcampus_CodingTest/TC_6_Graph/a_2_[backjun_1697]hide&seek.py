# https://www.acmicpc.net/problem/1697
from collections import deque
from timeit import default_timer as timer
from datetime import timedelta


MAX = 100001
n, k = map(int, input().split())
start = timer()
array = [0] * MAX


def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return array[now_pos]
        for next_pos in (now_pos - 1, now_pos + 1, now_pos * 2):
            # 한번도 안가고 범위 벗어나지 않으면
            if 0 <= next_pos < MAX and not array[next_pos]:
                array[next_pos] = array[now_pos] + 1
                q.append(next_pos)


print(bfs())

end = timer()

print("Time elapsed: ", end - start)  # seconds
print("Time elapsed: ", timedelta(seconds=end-start))
