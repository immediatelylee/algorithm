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
        for j in sorted(team[quest]):
            print(j)

# OK

# N,M = map(int,input().split())
# team_mem,mem_team = {},{}
# for i in range(N):
#     team_name,mem_num = input(),int(input())
#     team_mem[team_name]= []
#     for j in range(mem_num):
#         name = input()
#         team_mem[team_name].append(name)
#         mem_team[name]= team_name
# for i in range(M):
#     name,q = input(),int(input())
#     if q:
#         print(mem_team[name])
#     else:
#         for mem in sorted(team_mem[name]):
#             print(mem)
