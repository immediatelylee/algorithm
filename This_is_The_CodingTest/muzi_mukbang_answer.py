import heapq
# food_times = [3, 1, 2]
# k = 5
food_times = [8,6,4]
k = 15

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1)) # 음식 시간,음식 번호

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식시간

    length = len(food_times)

    # k는 전체 남은시간(끊기는 시간)
    # 왜 length만큼 빼냐하면 한번에 음식을 다 먹는것이 아니기 때문이다. 1번씩 번갈아 가며 먹는데 이때 최소힙에 나온값이기때문에 
    # 다른 음식을 다 먹는 시간보다는 작기때문이다. 
    # (8-1) (6-2) (4-3)   다먹는시간 - 음식번호 가 주어졌다면 
    # 최소힙에의해서 (4-3)이 상단이 있고  이를 다먹는시간은 4*3 = 12 이다. 
    # (한음식을 다 먹는시간)* 다른음식을 번갈아먹는 횟수(len(음식))


    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    # 남은 음식중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1])
    return result[(k-sum_value) % length][1]

test = solution(food_times, k)
print(test)

# 1.  sum_value 3  now 1