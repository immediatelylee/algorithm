'''
삽입정렬
첫번째 원소는 정렬되어있다고 생각하고 두번째 원소부터 적절한 위치에 배치하여 정렬하는것

시간복잡도 N^2  최선의 경우 O(N)


'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
print(array)
