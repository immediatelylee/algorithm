brown = 24
yellow = 24
answer = []
for n_1 in range(1, 40):

    for n_2 in range(1, 40):

        if ((n_1)*(n_2)) == yellow and 2*(n_1)+2*(n_2)+4 == brown and n_1 >= n_2:

            answer.append(n_1 + 2)
            answer.append(n_2 + 2)
            print(answer)
