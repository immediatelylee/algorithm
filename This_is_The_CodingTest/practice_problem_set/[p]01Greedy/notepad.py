'''
모험가길드 [v][][]
곱하기 혹은 더하기 [x][][]
문자열 뒤집기 [v][][]
만들수 없는 금액 [x][][]
볼링공 고르기 [v][][]
무지의 먹방 라이브  [][][]
'''


def solution(food_times, k):
    min_food_times = min(food_times)
    if k >= min_food_times:
        for i in range(len(food_times)):
            food_times[i] -= min_food_times

    answer = 0

    return answer
