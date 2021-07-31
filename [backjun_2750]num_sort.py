# https://www.acmicpc.net/problem/2750

# N = int(input())
# array = []

# for i in range(N):
#     array.append(int(input()))

# for i in sorted(array):
#     print(i)


# Select Sort

N = int(input())
array = []


for i in range(N):
    array.append(int(input()))


for i in range(N-1):

    for j in range(i, N):
        if array[j] < array[i]:
            array[i], array[j] = array[j], array[i]


for i in array:
    print(i)
