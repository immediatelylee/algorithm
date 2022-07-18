# 파일명에 ' 가 붙으면 실행이 안되고 에러가 난다.  castle's Night로 파일명을 했더니 실행 안됨.
'''
1. 8x8 좌표평면에 특정한 한간에 나이트가 있음
2. 나이트는 L자로 형태로만 이동가능함 
3. 좌표가 설정되면 나이트가 이동할수있는 경우의 수를 출력

ex)
a1 -> 2

'''
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
