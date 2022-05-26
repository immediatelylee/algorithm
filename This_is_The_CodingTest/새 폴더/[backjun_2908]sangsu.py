# https://www.acmicpc.net/problem/2908
'''
거꾸로 하는 것 .reverse  찾아보니 배열을 꺼꾸로 하는것.
슬라이스인덱스[-1]

'''
a, b = input().split()
print(max(int(a[-1::-1]), int(b[-1::-1])))
# print(max(int(a).reverse(), int(b).reverse()))
