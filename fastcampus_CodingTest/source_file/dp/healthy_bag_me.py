# dic_test
'''
dic = {}

dic[int(1)] = int(1001)
dic[int(2)] = int(1002)

print(dic.keys())
print(type(dic.keys()))
print(dic.values())
print(type(dic.values()))
'''

n, k = map(int, input().split())
dic = {}
for i in range(n):
    w, v = map(int, input().split())
    dic[w] = v

