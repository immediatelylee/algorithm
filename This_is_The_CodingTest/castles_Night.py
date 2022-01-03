# 파일명에 ' 가 붙으면 실행이 안되고 에러가 난다.  castle's Night로 파일명을 했더니 실행 안됨.

x, y = input()

move = [[-2, 1], [-2, -1], [2, 1], [2, -1], [1, 2], [1, -2], [-1, -2], [-1, 2]]

start_point = (ord(x)-96, int(y))

count = 0
for xx, yy in move:
    print(xx, yy)
    xx += start_point[0]
    yy += start_point[1]
    if xx < 1 or yy < 1 or xx > 9 or yy > 9:
        continue
    else:
        count += 1

print(count)
