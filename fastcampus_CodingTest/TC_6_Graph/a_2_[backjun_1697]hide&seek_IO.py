# https://www.acmicpc.net/problem/1697
from collections import deque
import sys

# input.txt
# 5 17

# 표준입력을 파일로 설정
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
MAX = 100001
n, k = map(int, input().split())
array = [0] * MAX

# bfs 재사용 안하니 변수 안놓고 실행만
# 입력값은 한번만 사용되므로 bfs() 에 n,k 로 구성한다.
# next_pos 가 0이 아니면 왔다간것이므로 제외한다.


def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return array[now_pos]
        for next_pos in (now_pos-1, now_pos+1, now_pos*2):
            if 0 <= next_pos < MAX and not array[next_pos]:
                array[next_pos] = array[now_pos] + 1
                q.append(next_pos)


print(bfs())
