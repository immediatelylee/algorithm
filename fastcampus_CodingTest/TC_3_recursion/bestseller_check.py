n = int(input())

books = {}

for _ in range(n):
    book = input()
    if book not in books:
        books[book] = 1
        print("books:", books)
        print("books[book]:", books[book])
    else:
        books[book] += 1
        print("books:", books)
        print("books[book]:", books[book])

target = max(books.values())
array = []

for book, number in books.items():

    if number == target:
        array.append(book)
        print("array:", array)

print(sorted(array)[0])
