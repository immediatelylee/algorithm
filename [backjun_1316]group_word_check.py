# https://www.acmicpc.net/problem/1316
'''
그룹단어
ccazzzzbb는 cazb가 모두 연속해서 나타나고 kin도 kin이 연속해서 나타나기때문에 그룹단어이지만
aabbbccb는 b가 떨어져 나타나기 때문에 그룹단어가 아니다.

단어에서 한글자가 출력될때 연속해서 출력되는 것이 아니면 그룹단어가 아니다.
abcbc (x)
set으로 중복을 제거한다음 
연속해서 나오는것은 true 인 상태로 두다가 true인상태에서 한번더 글자가 나오면 false가 되는 식으로 할것임.
연속이다라는 조건을 어떻게 걸지?
연속이다가 다른글자가 나오고 다시 같은 글자가 나올때 카운트를 올린다면 
카운트
'''

case = int(input())
answer = 0
for i in range(case):
    word = input()

    for j in range(len(word)):
        if j != len(word)-1:
            if word[j] == word[j+1]:
                pass
            elif word[j] in word[j+1:]:
                break
        else:
            answer += 1
print(answer)
