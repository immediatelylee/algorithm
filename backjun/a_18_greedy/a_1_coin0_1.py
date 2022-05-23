# https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
coin_list = [2, 4, 6]
cnt = 0

for i in range(n):
    coin_list.append(int(input()))


for i in coin_list[::-1]:

    cnt += (k//i)
    k %= i


print(cnt)


# if (k >= coin_list[i])
#     cnt += k / coin_list[i];
#     k = k % coin_list[i];
