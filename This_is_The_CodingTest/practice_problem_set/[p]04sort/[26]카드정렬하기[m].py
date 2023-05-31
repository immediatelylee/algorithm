import heapq

def minimum_comparisons(card_sizes):
    comparisons = 0
    heapq.heapify(card_sizes)  # 입력된 카드 묶음 크기를 우선순위 큐로 변환

    while len(card_sizes) > 1:
        # 가장 작은 두 묶음 선택
        smallest1 = heapq.heappop(card_sizes)
        smallest2 = heapq.heappop(card_sizes)

        # 선택한 묶음들을 합친 크기를 우선순위 큐에 삽입
        heapq.heappush(card_sizes, smallest1 + smallest2)

        # 비교 횟수 갱신
        comparisons += (smallest1 + smallest2)

    return comparisons


# 입력 받기
N = int(input())  # 묶음의 개수

card_sizes = []
for _ in range(N):
    size = int(input())  # 각 묶음의 크기
    card_sizes.append(size)

result = minimum_comparisons(card_sizes)
print(result)