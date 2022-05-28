# 시간초과  n의 범위가 15까지여서 pyhton으로 풀면 모두 시간초과 나는듯. 
# 사람들 15까지의 정답을 그냥 리스트에 담아서 print하는식으로 통과함
# https://www.acmicpc.net/problem/9663
def check(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        if abs(row[x] - row[i]) == x-i:
            return False
    return True


def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        # x번째 행의 각 열에 Queen을 둔다고 가정
        for i in range(n):
            row[x] = i
            if check(x):
                dfs(x+1)


n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)
