import heapq

n = int(input())
cards = [int(input()) for _ in range(n)]

heapq.heapify(cards)

result = 0
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    sum_value = a + b
    result += sum_value
    heapq.heappush(cards, sum_value)

print(result)


'''
Heapify란 배열(Array)을 이진 트리(Binary tree)의 자료구조를 갖는 힙(Heap)을 생성하는 과정이다.

실패 1
fn = 2(fn-3 + fn-2) + fn-1 이런식으로 구하려다가 실패
'''
