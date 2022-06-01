# https://www.acmicpc.net/problem/9037

# n이 별로 크지 않기 때문에 단순 구현문제
# 사탕수도 별로 크지 않기 때문에 조건에 맞춰서 구현만하면된다.

# 3
def check(N, candy):
    for i in range(N):
        if candy[i] % 2 == 1:
            candy[i] += 1

    return len(set(candy)) == 1

# 4
# 오른쪽으로 전달을 해줘야 하기떄문에
# 임시 리스트를 만들어서 전달해주기로 함.


def teacher(N, candy):
    tmp_lst = [0 for i in range(N)]
    # 여기서 enumberate를 써도 됨.
    for idx in range(N):
        if candy[idx] % 2:
            candy[idx] += 1
        # 와 깔끔하다.
        candy[idx] //= 2
        tmp_lst[(idx+1) % N] = candy[idx]

    for idx in range(N):
        candy[idx] += tmp_lst[idx]
    return candy


# 2
# 함수를 만들어서 풀것이다
# n개가 있고 candy리스트가 다음과 같을때 반복문이 돈다.
# 다 같은지 체크 할것이기 때문에 not check
# 정답이 cnt를 순환수를 출력해야하기 때문에 cnt
# candy 를 게속해서 갱신을 해줄것이에요
# 사탕의 숫자가 많다면 부하가 걸릴수 있지만 사탕수가 적기때메 괜찮습니다.


def process():
    N, candy = int(input()), list(map(int, input().split()))
    cnt = 0
    while not check(N, candy):
        cnt += 1
        candy = teacher(N, candy)
    print(cnt)


# 1 하나의 test case를 함수로 받아서 처리
for i in range(int(input())):
    process()
