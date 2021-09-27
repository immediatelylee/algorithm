# https://www.acmicpc.net/problem/1152
'''
띄어쓰기갯수만 세서 단어개수를 출력했는데 틀렸다고 나온다.
얍샙이들을 막는 케이스가 있나보다.

공백이 아닌 글자를 인식하면  카운트를 올리고 그다음 공백이 나올때까지 count를 유보하다가 공백이 나오고 다음 글자가 나오면 count를 올리고십다.

'''

import sys
s = input().strip()
if not s:
    print("0")
else:
    print(len(s.split(" ")))

print(s.split(" "))

# blank = string.count(' ')
# if string[0] == ' ':
#     print(blank)
# else:
#     print(blank+1)
