h, m = map(int, input().split())
time = int(input())

m += time

while m >= 60:
    m -= 60
    h += 1

while h >= 24:
    h -= 24

print(h, m, sep=' ')
