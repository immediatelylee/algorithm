
n,k = map(int,input().split())
data_a=sorted(list(map(int,input().split())))
data_b=sorted(list(map(int,input().split())),reverse=True)

for i in range(k):
    if data_a[i] <= data_b[i]:
        data_a[i] = data_b[i]

print(sum(data_a))