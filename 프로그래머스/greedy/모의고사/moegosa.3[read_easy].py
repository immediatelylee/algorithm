def answer_type(pattern, length):
    return pattern * (length // len(pattern)) + pattern[:length % len(pattern)]


def check_answer(p, a):
    return [(x == y) for x, y in zip(p, a)].count(True)


def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ps = [p1, p2, p3]
    anws = [answer_type(p, len(answers)) for p in ps]
    chks = [check_answer(a, answers) for a in anws]
    return [i+1 for i in range(len(ps)) if chks[i] == max(chks)]
