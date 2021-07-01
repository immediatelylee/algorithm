def prob10(x, y):
    if x % y == 0:  # 나눠진다면
        if x == y:
            return True
        else:
            x = x//y
            prob10(x, y)
    else:
        return False


prob10(9, 3)


# 일반적인 형태1
# def function(입력):
#     if 입력 > 일정값: # 입력이 일정 값 이상이면
#         return function(입력 - 1) # 입력보다 작은 값
#     else:
#         return 일정값, 입력값, 또는 특정값 # 재귀 호출 종료


# def function(입력):
#     if 입력 <= 일정값:              # 입력이 일정 값보다 작으면
#         return 일정값, 입력값, 또는 특정값              # 재귀 호출 종료
#     function(입력보다 작은 값)
#     return 결과값
