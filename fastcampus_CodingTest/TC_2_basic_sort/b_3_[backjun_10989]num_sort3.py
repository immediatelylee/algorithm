# https://www.acmicpc.net/problem/10989
import sys

input = sys.stdin.readline

result = [0 for i in range(10001)]


for i in range(int(input())):
    Num = int(input())
    result[Num] += 1

for i in range(10001):
    if result[i] != 0:
        for j in range(result[i]):
            print(i)
