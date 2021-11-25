word1 = " "+input()
word2 = " "+input()
length1 = len(word1)
length2 = len(word2)
DP = [[0 for _ in range(length2)] for _ in range(length1)]

for i in range(1, length1):
    for j in range(1, length2):
        if word1[i] == word2[j]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])

print(DP[len(word1)-1][len(word2)-1])
