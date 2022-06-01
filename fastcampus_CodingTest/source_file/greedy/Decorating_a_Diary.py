# https://www.acmicpc.net/problem/16676

N = input()
ans = 0

for i in range(len(N)):
    if int(N) < 11:
        ans = 1
    elif int(N) < int('1'*len(N)):
        ans = int(len(N)) - 1
    else:
        ans = int(len(N))

print(ans)

'''
0~10 : 1
11~110 : 2
111~1110: 3

N= input()
S = '1'*len(N)

if len(N) == 1:
    print(1)
elif int(N) >= int(S):
    print(len(N))
else:
    print(len(N)-1)



'''
