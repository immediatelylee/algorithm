s = input()

count0 = 0
count1 = 0

if s[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(1, len(s)):
    if s[i-1] != s[i]:
        if s[i] == '1':
            count0 += 1
        else:
            count1 += 1

result = min(count0, count1)
print(result)
