# https://www.acmicpc.net/problem/1712
'''
순수익이 조금이라도 있어야 고정비용을 갚을수 있다.
c-b가 0보다 커야한다.
'''

a,b,c = map(int,input().split())

net = c-b

if net <= 0:
    print(-1)
else:
    print((a // net )+1)