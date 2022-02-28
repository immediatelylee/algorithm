# https://www.acmicpc.net/problem/1316

# result = 0
# for i in range(int(input())):
#     word = input()
#     if list(word) == sorted(word, key=word.find):
#         result += 1
# print(result)

word = input()
print(sorted(word, key=word.find))
