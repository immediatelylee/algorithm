n = int(input())

count = 1
stack = []
result = []

for i in range(1, n+1):
    print("i:", i)
    data = int(input())
    print("data :", data)
    while count <= data:
        print("count <= data", count, "<=", data)
        print("result", result)
        stack.append(count)
        print("stack:", stack)
        count += 1
        result.append('+')
        print("result", result)
        print("count : data", count, data)
    if stack[-1] == data:
        print("'stack[-1] == data'", stack[-1], "==", data)
        stack.pop()
        result.append('-')
        print("result:", result)
        print("stack_pop", stack)
    else:
        print("NO")
        exit(0)

print('\n'.join(result))
