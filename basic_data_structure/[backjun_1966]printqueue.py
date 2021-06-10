# https://www.acmicpc.net/problem/1966
# 큐,구현,그리디

testcase = int(input())

for i in range(testcase):
    count = 1
    N, Q = map(int, input().split())
    priority = list(map(int, input().split()))
    checkout = [False for i in range(N)]

    checkout[Q] = True

    while max(checkout):
        if priority[0] == max(priority):
            if checkout[0] == True:
                break
            priority.pop(0)
            checkout.pop(0)
            count += 1
        else:
            priority.append(priority.pop(0))
            checkout.append(checkout.pop(0))

    print(count)
