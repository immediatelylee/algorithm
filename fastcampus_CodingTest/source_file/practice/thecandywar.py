# https://www.acmicpc.net/problem/9037

T, N = int(input()), int(input())


for l in range(T):
    arr = list(map(int, input().split()))
    cnt = 0
    # 초기 짝수 진행
    for i in range(N):
        hadd = [[] for j in range(N)]
        if arr[i] % 2 == 1:
            arr[i] += 1
        if len(set(arr)) == 1:
            print(cnt)
            break
    # 절반값 다른 리스트에 저장
        for i in range(1, N-1):
            hadd[i+1] = arr[i]/2
        hadd[0] = (arr[N]/2)
    # 사탕 절반 나누고, 다른 리스트값 더하기
        for i in range(1, N-1):
            arr[i] /= 2
            arr[i] += hadd[i]
        arr[0] /= 2
        arr[0] += hadd[0]
    # 홀수 다시 더하기
        if arr[i] % 2 == 1:
            arr[i] += 1
