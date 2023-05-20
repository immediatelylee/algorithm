'''
모험가길드 [v][x][]
곱하기 혹은 더하기 [x][v][]
문자열 뒤집기 [v][][]
만들수 없는 금액 [x][][]
볼링공 고르기 [v][][]
무지의 먹방 라이브  [][][]
'''


s = input()
cnt1 =0
cnt0 =0

if s[0]=='1':
    cnt1 +=1
else:
    cnt0+=1

for i in range(len(s)-1):
    if s[i] !=s[i+1]:
        if s[i+1] == '1':
            cnt0 +=1
        else:
            cnt1 +=1


print(min(cnt1,cnt0))