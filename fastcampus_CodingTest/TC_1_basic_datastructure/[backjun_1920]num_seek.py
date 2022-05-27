# https://www.acmicpc.net/problem/1920
# 해시,배열,구현문제
num = int(input())
data = list(map(int, input().split()))
num2 = int(input())
check = list(map(int, input().split()))
answer = [0 for i in range(len(data))]
print(answer)


for i in range(len(check)):
    print(i, "i")
    for j in range(len(data)):
        print(j, ":j")
        if check[i] == data[j]:
            answer[i] = 1


for i in range(len(answer)):
    print(answer[i])

'''
for i in x:
    if i not in array:
        print('0')
    else:
        print('1')

처럼 간편한 문법을 쓸것.
'''
