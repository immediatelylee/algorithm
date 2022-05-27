def is_available(candidate, current_col):
    # 각 행마다하나씩 들어가기 3번째 행이라면 len(candidate라면) 2 이고 인덱스이기 떄문에 0,1,2  2인덱스 이다
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            # candidate[queen-row] - current_col = 0    # candidate[queen_row]== queen_col
            return False  # 수직체크, 다각선 체크시에 조건에 맞으면 안되기 때문에 False
    return True


def DFS(N, current_row, current_candidate, final_result):
    if current_row == N:  # 배치가 다 끝나면
        # 배치도를 final_result 에 넣어준다. [:]를 한이유가 얇은 복사를 하기 위함이라고함
        final_result.append(current_candidate[:])
        return

    for candidate_col in range(N):  # 같은 행 체크
        # 이미 배치된 정보(current_candidate),이번 열의 번호 -> 수직체크,대각선체크가능
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row + 1, current_candidate, final_result)
            current_candidate.pop()  # 백트래킹


def solve_n_queens(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result
