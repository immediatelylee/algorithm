# https://www.acmicpc.net/problem/2437
# knapsack과 유사
N, Iron = int(input()), sorted(list(map(int, input().split())))

ans = 0
# 추의 무게 <= 여태까지의 추의합 +1
# 성립하지 않으면 구현하지 못한다.
for i in Iron:
    if i <= ans + 1:
        ans += i
    else:
        break

print(ans + 1)

'''
1   : 1
2   : 2  
3   : 3
4   : 1+3
5   : 2 +3
6   : 6
7   : 7
8   : 6+2
9   : 7+2
10  : 7+3
11  : 7+1+3
12  : 7+2+3
13  : 7+6
14  : 7+6+1
15  : 7+6+2
16  : 7+6+3
17  : 7+6+3+1
18  : 7+6+3+2
19  : 7+6+3+2+1
20  : 7+6+3+2+1+1
21  :


'''
