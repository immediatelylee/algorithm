# 1. 논리 연산자 /비트 연산자 활용하기
# a, b = 10, 20

# if a > b:
#     print(a)

# 단순하게하게  중복되지 않게  깊게 반복문이 되면 안된다.
# boolean 값이 4개 이하로 되야 한다.

# and or not 정도를 활용하면 좋다.

# 비트 연산자.
# a, b

# 1 << 2, 1 & 1
# 1 | 1
# 1 ^ 1

# 이런 것들이 있으며 문제가 나왔을때 다시 설명할것이다.


# 2. 상태를 나타내는 자료 활용하기
# 소수 체크 하는 경우

# N = 71
# ck = False
# for i in range(1, N):
#     if N % i == 0:
#         print("Not Prime")
#         ck = True
#         break

# if not ck:
#     print("Prime")

# 여기서는 단일 숫자가 나왔지만 배열이 나올수도 있고, 중복 체크를 하는 set이 될수 도 있다.


# 3. 나눠서 진행하기

# -> 위의 구문을 나눠서 간결하게 표현


# def isPrime(N):
#     for i in range(2, N):
#         if N % i == 0:
#             return False
#     return True


# for N in range(10, 100):
#     if isPrime(N):
#         if isPrime("{} if Prime".format(N))
#     else:
#         print("Not Prime")

# 나중에 나오는 bfs dfs에는 2차원배열 3차원 배열을 탐색하는 과정이 나옴
# 조건문같은 것을 반복하는 것이 아니라 간단하게 함수를 만들어서 넣는다.


# def isRange(a, b, N, M):
#     return 0 <= a < N and 0 <= b < M


# 4. 여러 자료구조와 메서드, 함수 활용하기

# [펠린드롭 체크]
# S = "hello"

# for idx in S:
#     if S[idx] != S[len(S)-idx-1]:
#         print("Not Palin")


# -> >
# 파이썬 유저라면 이런식으로 쓸수 있다.
# S = "hello"

# if S == S[::-1]:  # 앞의 변수를 복사. [::]
#     print("isPalin")

# 다른 팁
# 배열에 있는 값이 모두 다르다 체크하려면


# def isUnique(ls):
#     return len(lst) == len(set(lst))


# 5. 미리 처리한 케이스와 처리할 케이스 정리하기

# # 1. 예제 케이스
# # 2. 조건 A 처리
# # 3. 조건 B 처리
# # 4. 조건 AB처리
# #


# 6. 예제 최소,최대,예외,랜덤케이스 만들기

# 1. 문제 조건에 따른 예제
# 2. 최소 조건 체크  0<N < 10000 이라면 0 부터 체크해봐야 한다.
# 3. 최대 조건 체크
# 4. 예외
# 5. 랜덤케이스 만들기   dp로 풀어야 하는 문제를 전수 조사로 답안을 만든뒤에 dp로 풀리는 지확인.
