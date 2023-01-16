n = input()
left = 0
right = 0
mid = int((len(n)/2))
end = len(n)


for i in range(mid):
    left += int(n[i])

for j in range(mid, end):
    right += int(n[j])


if left == right:
    print("LUCKY")
else:
    print("READY")
