N = int(input())
b = 0

for i in range(1, N):
    b = ' '*(N-i)+'*'*((2*i)-1)
    print(b)


for i in range(N, 0, -1):

    b = ' '*(N-i)+'*'*((2*i)-1)

    print(b)


# for i in range(1, N):
#     print(''.join(answer))
#     answer[i] = ' '
