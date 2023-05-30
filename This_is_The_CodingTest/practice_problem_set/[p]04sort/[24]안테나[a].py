n = int(input())
houses = list(map(int, input().split()))
houses.sort()

median = houses[(n-1)//2]
print(median)
