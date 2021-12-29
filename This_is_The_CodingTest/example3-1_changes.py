# https://www.acmicpc.net/problem/5585

# input1 = 380
# input2 = 1

money = 1000 - int(input())
count = 0
change = [500, 100, 50, 10, 5, 1]


for i in change:
    j = (money // i)
    count += j
    money -= i*j


print(count)
