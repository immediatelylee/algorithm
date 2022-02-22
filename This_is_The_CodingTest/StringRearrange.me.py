# isdigit으로 판별하고 두 리스트에 나눠서 담음
n = list(input())
letters, digits = [], []

number = 0
for i in n:
    if i.isdigit():
        digits.append(int(i))
    else:
        letters.append(i)

letters.sort()
print(''.join(letters)+str(sum(digits)))
# print(letters + str(sum(digits)))
# print(n.isdigit())
