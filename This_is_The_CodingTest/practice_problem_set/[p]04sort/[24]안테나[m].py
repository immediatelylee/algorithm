n = int(input())

data = list(map(int,input().split()))
data.sort()

answer = data[(n-1)//2] 

print(answer)