string = input()
word = input()
i = 0
length = len(word)
count = 0

while i < len(string):
    if string[i:i+length] == word:
        count += 1
        i += length
    else:
        i += 1
print(count)


'''
input_string = input()
input_word = input()

idx = 0
result = 0

# string을 탐색할때 한글자씩 이동하는 것이 아닌  단어 글자수대로 이동해야 한다.
while len(input_word) - idx >= len(input_word):
    if input_string[idx:idx + len(input_word)] == input_word:
        result += 1
        idx += len(input_word)
    else:
        idx += 1

print(result)
'''
