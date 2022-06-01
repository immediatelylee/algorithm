def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return target
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


n = int(input())
array = list(map(int, input().split()))
array.sort()
c = int(input())
c_array = list(map(int, input().split()))

for i in c_array:
    target = i
    result = binary_search(array, target, array[0], n-1)
    # result = binary_search(array, target, 0, n-1)
    if result == None:
        # print('no')
        print('no', end=' ')
    else:
        # print('yes')
        print('yes', end=' ')
