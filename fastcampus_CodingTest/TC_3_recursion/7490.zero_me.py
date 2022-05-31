import copy
test_case = int(input())
operators_list = []


def recursive(array, n):
    if len(array) == n:
        operators_list.append(copy.deepcopy(array))
        return

    array.append(' ')
    recursive(array, n)
    array.pop()

    array.append('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()


test_case = int(input())
for _ in range(test_case):
    operators_list = []
    n = int(input())
    recursive([], n-1)
    interger = [i for i in range(1, n+1)]

    for operators in operators_list:
        string = ""
        for i in range(n-1):
            string += str(interger[i]) + operators[i]
        string
