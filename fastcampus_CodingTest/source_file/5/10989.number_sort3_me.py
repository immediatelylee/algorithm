n = int(input())

array = []
for i in range(n):
    array.append(int(input()))


for j in range(1, 10):
    for i in range(n):
        if array[i] == j:
            print(j)

# import sys

# n = int(sys.stdin.readline())

# array = []
# for i in range(n):
#     array.append(int(sys.stdin.readline()))


# for j in range(1, 10):
#     for i in range(n):
#         if array[i] == j:
#             print(j)
