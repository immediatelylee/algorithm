# 삼성 공채에서 비슷한 문제가 나옴
# 그림이 많고 이것을 구현할수 있는가?

# 파이썬에서 변수 = 했을때 값이 있는객체의 주소값만 복사하므로 ??  정확히 왜 deepcopy를 써야하지?
# 회전하기 위해서 새로운 배열을 만들고 원래 배열에서 회전한 위치를 새로운 배열에 저장하게 된다.
# 이때 deepcopy를 안하면 주소값만 저장이 되고 실제 새로운 배열이 생기지 않아서 원래의 배열의 값이 변경된다.
from copy import deepcopy

# 2048판 회전

# 탐색문제 1024 가지 경우 탐색
# 탐색을 할때 동서남북 으로 따로 움직이는것이 맞는 움직임일까요?
# 시간복잡도를 고려하지 않으면 다 고려해도 되지만 시간제한이 있으니 적합하지 않다.
# 동서남북으로 움직이는 것 보다 맵을 돌리는것이 더 효율적이다.
# 방향을 하나로 이미 지정해 놓고  맵만 조금 씩 돌려버리는것이다.
# 이번 코딩에서 배열을 회전해서 다 합치는 방식으로 진행할 예정
# 왼쪽으로 슬라이드를 짜는데 위로 가는 것 90도 돌린것에서 왼쪽으로 슬라이드 180도에서 왼쪽으로 슬라이드...


def rotate90(B, N):
    NB = deepcopy(B)
    for i in range(N):
        for j in range(N):
            NB[j][N-i-1] = B[i][j]    # row 를 column 으로 column은 역순으로 증가한다  N-1 -i
    return NB
# 외우는것이 좋다.
# 한줄을 swip했을 때 변화


def convert(lst, N):
    new_list = [i for i in lst if i]  # 0이 아닌 숫자만
    for i in range(1, len(new_list)):
        if new_list[i-1] == new_list[i]:
            new_list[i-1] *= 2
            new_list[i] = 0  # 새로운값을 0 으로 만들고 이전의 값을 2배로 한다
    new_list = [i for i in new_list if i]
    return new_list + [0] * (N-len(new_list))


# dfs로 다음 상태로 옮김
def dfs(N, B, count):
    ret = max([max(i) for i in B])
    if count == 0:
        return ret
    for _ in range(4):
        X = [convert(i, N) for i in B]
        if X != B:
            ret = max(ret, dfs(N, X, count-1))
        B = rotate90(B, N)
    return ret


if __name__ == '__main__':
    N = int(input())
    Board = [list(map(int, input().split())) for i in range(N)]
    print(dfs(N, Board, 5))
