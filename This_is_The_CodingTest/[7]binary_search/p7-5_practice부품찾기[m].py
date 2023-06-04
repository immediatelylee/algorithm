import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort()

target_number = int(input())
target_list = list(map(int, input().split()))

def binary_search(array, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return target
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

result = []

for target in target_list:
    if binary_search(array, target, 0, n-1) == target:
        result.append("yes")
    else:
        result.append("no")

print(result)