n = int(input())


for i in range(n):
    L_stack = []
    R_stack = []
    data = input()

    for i in data:
        if i == '-':
            if L_stack:
                L_stack.pop()
        elif i == '<':
            if L_stack:
                R_stack.append(L_stack.pop())

        elif i == '>':
            if R_stack:
                L_stack.append(R_stack.pop())
        else:
            L_stack.append(i)

    L_stack.extend(reversed(R_stack))
    print(''.join(L_stack))
