N = int(input())
traveller = list(map(int, input().split()))

max_temp = 0
max_i = 0
for i in set(traveller):
    temp = traveller.count(i)
    if max_temp >= temp:
        max_temp = temp
        max_i = i
