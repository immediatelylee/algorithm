import sys

# 표준입력을 파일로 설정
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

# inputdata 예시
# 5 4 2
# 1 2
# 1 3
# 1 4
# 1 5

'''
n, m, v = map(int, input().split())
print((n, m, v))
for i in range(m):
    x, y = map(int, input().split())
    print((x, y))
'''

# file = open("./input.txt", "r")
# while True:
#     line = file.readline()
#     if not line:
#         break
#     print(line.strip())

# file.close()
