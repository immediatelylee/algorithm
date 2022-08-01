'''
데이터 크기 범위가 제한되어 정수의 형태로 표현 할수 있을때만 사용가능

0,1,2,3,4,5,6,7,8,9 로 십진수는 이루워 져있고 이 숫자의 개수를 카운팅하여 
큰순서대로 나열 작은 순서대로 나열을 하는것이다. 

시간복잡도는 
O(N+K) 최대값의 크기를 k라고 한다면 
'''

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]  # 피벗은 첫 번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
