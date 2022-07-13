import heapq
jobs = [[0, 3],  [2, 6], [1, 9]]


def solution(jobs):
    count, last, answer = 0, -1, 0
    heap = []
    print("presort:", jobs)
    jobs.sort()
    print("jobs:", jobs)
    # 시작시간 초기화
    time = jobs[0][0]
    print("time:", time)
    while count < len(jobs):
        print("len(jobs):", len(jobs))
        print("count:", count)
        for s, t in jobs:
            print("s,t:", s, t)
            if last < s <= time:
                print("last,s,time:", last, s, time)
                # 작업 소요시간으로 min heap을 만들기 위해 (t, s) 푸시
                heapq.heappush(heap, (t, s))
                print("heap:", heap)
        # 바로 수행할 수 있는 작업이 있는 경우
        if len(heap) > 0:
            count += 1
            print("count:", count)
            last = time
            print("time:",time)
            print("last:", last)
            term, start = heapq.heappop(heap)
            print("term,start:", term, start)
            time += term
            print("time:", time)
            answer += (time - start)
            print("answer:", answer)
        # 바로 수행할 수 있는 작업이 없는 경우
        else:
            time += 1
    return answer//len(jobs)


solution(jobs)
