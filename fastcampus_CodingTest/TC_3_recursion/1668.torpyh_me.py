n = int(input())
array = []
for i in range(n):
    array.append(int(input()))


def asending(array):
    now = array[0]
    count = 1
    for i in range(1, len(array)):
        if now < array[i]:
            now = array[i]
            count += 1

    return count


print(asending(array))
array.reverse()
print(asending(array))

'''n = int(input())
array = []
count = 1

for i in range(n):
    array.append(int(input()))

now = array[0]
for k in range(1, len(array)):

    if now < array[k]:
        count += 1
        now = array[k]

print(count)
array.reverse()

count = 1
now = array[0]
for j in range(1, len(array)):

    if now < array[j]:
        count += 1
        now = array[j]

print(count)
'''
