n= int(input())
data =[]
for i in range(n):
    name,score = map(str,input().split())
    data.append((int(score),name))
    
data.sort()

for i in range(n):
    print(data[i][1],end=' ')

