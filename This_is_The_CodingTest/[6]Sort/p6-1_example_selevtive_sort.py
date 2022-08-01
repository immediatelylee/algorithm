'''
선택정렬
가장 낮은 데이터를 선택해 맨 앞에 데이터와 바꾸고 
그다음 작은 데이터를 선택헤 앞에서 두번째 데이터와 바꾸는과정

시간 복잡도 N^2 
for문을 두번 돌리니까
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[j] = array[j], array[i]

print(array)
