N, M = map(int, input().split())
A, B = input().split()

alp = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1,
       3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

AB = ''
min_len = min(N, M)
for i in range(min_len):
    AB += A[i] + B[i]

AB += A[min_len:] + B[min_len:]

lst = [alp[ord(i)-ord('A')] for i in AB]

for i in range(N+M-2):   # 밑에 2자리 가 남으니까 2번을 덜 계산함 (밑으로)
    # i가 0일때 부터 시작하고 더하기를 할때 뒤엣것을 더하고 맨마지막은 계산하지 않으므로.
    for j in range(N+M-1-i):
        lst[j] += lst[j+1]

print("{}%".format(lst[0] % 10*10 + lst[1] % 10))
