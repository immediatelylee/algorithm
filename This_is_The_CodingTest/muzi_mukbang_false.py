food_times = [3, 1, 2]
k = 5

result = 0
count = 0
i = 0
while count < k:
    if i == len(food_times):
        i = 0

    if food_times[i] != 0:
        food_times[i] -= 1
        i += 1
        count += 1
    else:
        i += 1

check = True
for j in range(len(food_times)):

    if food_times[j] != 0:
        check = False

if check == True:
    print(-1)
else:
    print((i+1) // len(food_times))
