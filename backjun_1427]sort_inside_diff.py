n = input()

for i in range(9, -1, -1):
    for j in range(len(n)):
        if int(n[j]) == i:
            print(i, end='')
