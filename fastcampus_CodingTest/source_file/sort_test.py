mee = [(1, 1), (2, 1), (2, -1), (3, 4), (3, -1)]

array = sorted(mee, key=lambda x: (x[0], -x[1]))
print(array)

