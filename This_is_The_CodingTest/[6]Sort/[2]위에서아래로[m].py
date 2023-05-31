n=int(input())
data =[]
for _ in range(n):
    data.append(int(input()))

data.sort()
data.reverse()

for i in range(len(data)):
    print(data[i],sep=" ",end=" ")

