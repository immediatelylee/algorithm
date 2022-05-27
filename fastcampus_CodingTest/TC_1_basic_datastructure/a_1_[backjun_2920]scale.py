# https://www.acmicpc.net/problem/2920
# 배열,구현문제

scale = list(map(int, input().split()))

ascending = False
descending = False


for i in range(1, len(scale)):
    if scale[i-1] < scale[i]:
        ascending = True
    elif scale[i-1] > scale[i]:
        descending = True

if ascending and descending == True:
    print("mixed")
elif ascending == True:
    print("ascending")
else:
    print("descending")
