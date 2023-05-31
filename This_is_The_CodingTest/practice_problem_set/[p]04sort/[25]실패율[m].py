def solution(n,stages):

    answer = []
    total_players = len(stages)

    # 실패율 구하기 
    for i in range(1,n+1):
        staying_players = stages.count(i)

        if total_players == 0:
            failure_rate = 0
        else:
            failure_rate = staying_players / total_players


        # answer 리스트에 스테이지 번호와 실패율 추가
        answer.append((i, failure_rate))

        # 해당 스테이지에 머물러 있는 플레이어 수를 전체 플레이어 수에서 뺀다.
        total_players -= staying_players

    # 실패율을 기준으로 내림차순 정렬
    answer.sort(key=lambda x: (-x[1], x[0]))

    
    # 스테이지 번호만 answer_list에 추가하고 반환
    return [i[0] for i in answer]