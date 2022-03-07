# ' 균형잡힌 괄호 문자열'의 인덱스 반환
# p = ")("
p = "()))((()"
# 균형잡힌 괄호 문자열 인덱스 반환


def balanced_index(p):
    count = 0  # 왼쪽괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# '올바른 괄호 문자열' 판단


def check_proper(p):
    count = 0  # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True  # 쌍이 맞는 경우에 True 반환


def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # 올바른 괄호 문자열'이면 , v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    # 올바른 괄호 문자열' 이 아니라면 아래의 과정 수행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        # 첫 번째와 마지막 문자를 제거 (실제로 제거하는 것이 아니고 1번 인덱스 부터 마지막 -1 인덱스까지를 다시 저장하는것)
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer


test = solution(p)
print(test)
