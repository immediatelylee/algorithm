# 제한사항 인쇄작업 중요도는 숫자가 클수록 중요하다.
# location은 0이상 이하의 값을 가지며 대기목록의 가장앞에 있으면 0
# 두번째에 있으면 1
# 입출력을 봤을때 그냥 몇번째에 출력하는지만 나옴.
priorities = [3, 1, 4, 2]
location = 2


def solution(priorities, location):
    # 입력받은 location 자리가 오면 종료하기 위한 변수값 설정
    answer = 0
    location_check = [False]*len(priorities)
    location_check[location] = True
    

    while priorities:
        # 맨 앞에 있는 원소가 우선순위가 가장 높을 경우
        #그중에서 location으로 입력받은 순서인 경우 인쇄하고 종료
        if priorities[0] == max(priorities):
            if location_check[0] == True:
                priorities.pop(0)
                answer += 1
                break
            # 그러지 않으면 인쇄 다시 반복문
            else:
                priorities.pop(0)
                location_check.pop(0)
                answer += 1
        #우선순위가 높지 않은 경우, 원소를 대기열 맨뒤로 보내기
        else:
            location_check.append(location_check[0])
            location_check.pop(0)
            priorities.append(priorities[0])
            priorities.pop(0)
    
    return answer


solution(priorities, location)
