n = int(input())
k = 1
count = 0
while n:
    if n < k:
        k = 1
    n -= k
    k += 1
    count += 1

print(count)

# total_bird = int(input())

# count = 0
# k = 1


# while total_bird != 0:
#     if k > total_bird:
#         k = 1

#     total_bird = total_bird - k
#     k += 1
#     count += 1
# print(count)
