# 1,0의 그룹중에 count가 낮은것을 출력하면될듯
data = list(map(int, input()))
zero_cnt = 0
one_cnt = 0

if data[0] == 0:
    zero_cnt += 1
else:
    one_cnt += 1


for i in range(1, len(data)):
    if data[i-1] == 0 and data[i] == data[i-1]:
        continue
    elif data[i-1] == 0 and data[i] != data[i-1]:
        one_cnt += 1
    elif data[i-1] == 1 and data[i] == data[i-1]:
        continue
    elif data[i-1] == 1 and data[i] != data[i-1]:
        zero_cnt += 1

print(min(zero_cnt, one_cnt))
