# answer = [1, 2, 3, 4, 5]
answer = [1, 3, 2, 4, 2]

supo = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
# 어떤방식으로 반복시키지?
# while 로무한반복시키려고도 했으나 굳이 그럴필요 없이 len(answer)로
# answer 개수를 계산해서 answer가종료되면 종료가되야함.
top_score = [0]
temp = 0
return_list = [0]
for n in supo:
    Repeat = len(n)
    Cnt = 0
    for i in range(len(answer)):
        if answer[i] == n[i % Repeat]:
            Cnt += 1

if return_list[0] == Cnt:
    return_list.append(Cnt)
elif return_list[0] < Cnt:
    return_list[0] = Cnt

print(return_list)
# cnt를 계산하는 것 까지는 했는데 순위 매기는것을 어떻게 효율적으로 할수 있을까?
# 리스트를 한번에 출력을 해야 하고   리스트에 넣기 전에 조건으로해서 넣어야함.
# temp를 써서 cnt를 넣고  이후
