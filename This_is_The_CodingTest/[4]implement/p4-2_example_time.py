'''
1. 정수 n이 입력되면 00시00분00초 부터 n시 59분59초까지 
모든 시각중에 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램

'''

n = int(input())
count = 0

for H in range(0, n+1):
    for M in range(0, 60):
        for S in range(0, 60):
            if '3' in str(H) + str(M) + str(S):
                count += 1

print(count)
