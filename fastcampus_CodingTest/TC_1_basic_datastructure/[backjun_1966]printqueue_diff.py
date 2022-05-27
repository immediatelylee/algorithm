test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split()))
    queue = list(map(int, input().split()))
    queue = [(i, idx) for idx, i in enumerate(queue)]

    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))

# enumerate 함수의 활용 , lambda를 통하여 2차원배열에서 0번째 원소 정렬
