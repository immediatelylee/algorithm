# https://www.acmicpc.net/problem/5397
# 스택,구현,그리디

test = int(input())

for _ in range(test):
    stack_L = []
    stack_R = []
    input_string = input()
    for i in range(len(input_string)):
        if input_string[i] == "-":
            if len(stack_L) == 0:
                continue
            else:
                stack_L.pop()

        elif input_string[i] == "<":
            if len(stack_L) == 0:
                continue
            else:
                stack_R.append(stack_L.pop())

        elif input_string[i] == ">":
            if len(stack_R) == 0:
                continue
            else:
                stack_L.append(stack_R.pop())
        else:
            stack_L.append(input_string[i])

    stack_L.extend(reversed(stack_R))
    print(''.join(stack_L))
