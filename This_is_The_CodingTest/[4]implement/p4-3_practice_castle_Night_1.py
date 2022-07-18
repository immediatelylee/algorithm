# 파일명에 ' 가 붙으면 실행이 안되고 에러가 난다.  castle's Night로 파일명을 했더니 실행 안됨.
'''
1. 8x8 좌표평면에 특정한 한간에 나이트가 있음
2. 나이트는 L자로 형태로만 이동가능함 
3. 좌표가 설정되면 나이트가 이동할수있는 경우의 수를 출력

ex)
a1 -> 2

'''
input_data = input()
x = ord(input_data[0])-96
y = int(input_data[1])


# 마가 이동할수 있는 경우 벡터로
dx = [-1, 1, 2, 2, -1, 1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, 1, -1]


# 탐색
cnt = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    # 맵밖으로 나가는 경우 제외
    if nx > 8 or ny > 8 or nx <= 0 or ny <= 0:
        continue
    cnt += 1

print(cnt)
