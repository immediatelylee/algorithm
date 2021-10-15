# https://www.acmicpc.net/problem/16165

team_num, problems = map(int, input().split())
team, member = dict(), dict()


for i in range(team_num):
    team_name = input()
    team[team_name] = []
    for j in range(int(input())):
        member_name = input()
        team[team_name].append(member_name)
        member[member_name] = team_name

for i in range(problems):
    quest = input()
    check = int(input())
    if check == 1:  # 팀이름 출력
        print(member[quest])
    else:  # 멤버 출력
        for j in team[quest]:
            print(j)
