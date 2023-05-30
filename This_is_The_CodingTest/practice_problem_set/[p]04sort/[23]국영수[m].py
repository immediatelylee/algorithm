n = int(input())  

students = []  

for _ in range(n):
    name,K,E,M = input().split()
    students.append((name,int(K),int(E),int(M)))

result = sorted(students,key=lambda student: (-student[1],student[2],-student[3],student[0]))

for i in range(n):
    print(result[i][0])


