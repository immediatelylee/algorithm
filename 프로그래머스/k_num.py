# import sys
# input = sys.stdin.readline
# array = int(input())
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# print(sorted(array[2:6]))
for c in range(len(commands)):
    answer = []
    i, j, k = commands[c]  # 핵심표현 3
    print(i, j, k)
    # if j != len(array):
    #     j = j + 1
    cut_array = sorted(array[i-1:j])
    print(cut_array)
    answer.append(cut_array[k-1])
    print(answer)
    # print(cut_array)
    # print(cut_array[k-1])
# print(cut_array[3])
# print(cut_array[k])
# print(cut_array[k])
# answer = []
# answer.append(sorted(array)[3])  # 핵심표현1

# print(answer)
# print(len(commands))  #핵심표현2


# def k_num(array, commands):
#     answer = []
#     for c in range(len(commands)):
#         i, j, k = commands[c]
#         # if j != len(array):
#         #     j = j + 1
#         cut_array = array[i-1:j-1]
#         answer.append(sorted(cut_array)[k-1])

#     return answer
#     print(answer)


# #
# k_num(array, commands)
