'''
기준값 피벗을 설정하고서 피벗보다 큰값과 작은 값의 위치를 바꾸는 방식 
모두 바꾸고 나면 그 가운데에 피벗을 놓고 세트 마무리
피벗값보다 작은쪽에서 다시 피벗을 설정하고 한세트 피벗값보다 큰쪽에서 다시 피벗같을 설정해서 한세트 

시간복잡도는 nlogn  n번 나누는데 나눌때마다 (n) 값이 절반으로 줄기 때문(logn)

'''
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right):  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
