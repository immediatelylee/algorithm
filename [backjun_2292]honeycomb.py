# https://www.acmicpc.net/problem/2292
'''
핵심은 범위이다.
1~7까지는 2칸
8~19까지는 3칸이다.

범위 증가가 6-12-18 순으로 늘어난다 

등차수열 일반항 구현한다고 헤매다가
그냥 변수 두개 돌리고 추가하면 된다는 것을 깨달았다

'''

Num= int(input())
n_stack=1
cnt =1
while Num > n_stack:
    n_stack += 6*cnt 
    cnt += 1

print(cnt)
    


