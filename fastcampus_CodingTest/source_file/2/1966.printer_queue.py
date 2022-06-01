n = int(input())

cnt = 0

for i in range(n):
    t_num, Print = map(int, input().split())
    priority = list(map(int, input().split()))
    priority = [(i, idx) for idx, i in enumerate(priority)]

    while priority[Print] in priority:

        if priority[Print] == max(priority):
            cnt += 1
            priority.pop(0)
        else:
            cnt += 1
            priority.append(0)
            priority.pop(0)
    print(cnt)


# print('11')
