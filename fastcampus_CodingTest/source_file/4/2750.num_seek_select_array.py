n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

for i in range(n):
    min_value = array[i]
    for j in range(i+1, n):
        if min_value > array[j]:
            min_value, array[j] = array[j], min_value

    print(min_value, end='\n')
