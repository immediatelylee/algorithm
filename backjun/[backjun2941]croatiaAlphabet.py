# https://www.acmicpc.net/problem/2941

'''
크로아티아 알파벳 찾는 문제
find를 활용할 예정 
find 찾아서 하려그랬는데 전처리로 변환을 시켜야 할것 같아서 
크로아티아 알파벳에 해당아는것들 위에는 공백을 집어넣기로 하였다. 
replace 사용


'''

string = input()

string = string.replace("c=", "*")
string = string.replace("c-", "*")
string = string.replace("dz=", "*")
string = string.replace("d-", "*")
string = string.replace("lj", "*")
string = string.replace("nj", "*")
string = string.replace("s=", "*")
string = string.replace("z=", "*")
print(len(string))

# a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# alpha = input()

# for t in a:
#     alpha = alpha.replace(t, '*')

# print(alpha)
