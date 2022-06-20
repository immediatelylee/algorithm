n = list(map(int, input()))  # 스니핏에 넣어놓기

middle = (len(n) // 2)


a = sum(n[:middle])  # 왜 3이 나오지? [:3] = 0,1,2
b = sum(n[middle:])
if a == b:
    print('LUCKY')
else:
    print('READY')
