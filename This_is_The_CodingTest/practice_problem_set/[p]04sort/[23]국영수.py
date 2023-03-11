n = int(input())  # 학생 수 입력

students = []  # 학생 정보를 저장할 리스트

# 학생 정보 입력
for i in range(n):
    name, kor, eng, math = input().split()
    students.append((name, int(kor), int(eng), int(math)))

# 조건에 따라 학생 정보 정렬
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

# 정렬된 학생 정보 출력
for student in students:
    print(student[0])
