# https://leetcode.com/problems/daily-temperatures/

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
length = len(temperatures)-1

for i in range(length):
    count = 1

    j = i

    if j+count > length:
        temperatures[i] = 0
        break

    elif j + count == length:
        if temperatures[j] >= temperatures[j+count]:
            temperatures[i] = 0
            break
        else:
            temperatures[i] = 1
            break
    else:
        while temperatures[j] >= temperatures[j+count]:
            if j+count == length:
                if temperatures[j] >= temperatures[j+count]:
                    count = 0
                    break

            else:
                count += 1
                if j+count == length:
                    count = 0
                    break
        temperatures[i] = count
temperatures[-1] = 0
print(temperatures)
