# https://www.acmicpc.net/problem/2531
# https://osnim.tistory.com/entry/%EB%B0%B1%EC%A4%80-2531-%ED%9A%8C%EC%A0%84-%EC%B4%88%EB%B0%A5-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys


def solve():
    left = 0
    right = 0
    dict = {}
    result = 0
    # k만큼 먹기
    while right < k:
        if arr[right] not in dict.keys():
            dict[arr[right]] = 1
        else:
            dict[arr[right]] += 1
        right += 1

    # c는 반드시 추가
    if c not in dict.keys():
        dict[c] = 1
    else:
        dict[c] += 1

    # 슬라이딩 윈도우
    while left < n:
        result = max(result, len(dict))
        # 1. 맨 왼쪽 초밥 제거
        dict[arr[left]] -= 1
        # 삭제된 왼쪽 초밥이 0 이면 dict 삭제
        if dict[arr[left]] == 0:
            del dict[arr[left]]
        if arr[right % n] not in dict.keys():
            dict[arr[right % n]] = 1
        else:
            dict[arr[right % n]] += 1
        left += 1
        right += 1

    print(result)
    return


if __name__ == "__main__":
    n, d, k, c = map(int, sys.stdin.readline().split())
    arr = [int(sys.stdin.readline()) for _ in range(n)]
    solve()
