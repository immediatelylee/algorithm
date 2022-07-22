def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]


# 갈색 벽돌이랑 노란색 벽돌의 관계식을 세워서 해당 식을 만족하는 정수해를 찾으면 되는데,
# 만족하는 식이 해당 정수의 곱으로 표현되니까 약수를 다 찾는 과정에서 range(1,sqrt(n))이 나옵니다
