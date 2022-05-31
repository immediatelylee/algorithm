n = int(input())
books = dict()
array = []
for i in range(n):
    book = input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

target = max(books.values())

for name, idx in books.items():
    if idx == target:
        array.append(name)

array.sort()
print(array[0])

'''n = int(input())

books = {}
for i in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] = books[book] + 1

target = max(books.values())
print()
result = []
array = books.items()
for i, idx in array:
    if idx == target:
        result.append(i)
        print(result)

data = result.sort()

print(data)
'''

# Traceback (most recent call last):
#     File "c:\Users\k\k 백업\Desktop\learn-javascript-master\learn-javascript-master\notes\python\6\bestseller_me.py", line 19, in <module>
#         print(data[0])
# TypeError: 'NoneType' object is not subscriptable
# case1
# 5
# top
# top
# top
# top
# kimtop
# None

# case 2
# data = result.sort()

# print(data)

# ['top']
# None

# case 3
# data = sorted(result)

# ['top']
# ['top']

# 원인 파악
# sort() 함수의 리턴값은 None 이다. 정렬된 값이 리턴되지 않고 원본 리스트 값이 정렬된 값으로 수정되어버림.
