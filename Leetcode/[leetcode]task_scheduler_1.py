# https://leetcode.com/problems/task-scheduler/
from typing import List
import collections

tasks = ["A", "A", "A", "B", "B", "B"]
n = 2


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counter = collections.Counter(tasks)
        result = 0
        # tasks = ["A", "A", "A", "B", "B", "B"]
        #  -> Counter({'A': 3, 'B':3})

        while True:
            sub_count = 0

            # 개수 순 추출
            for task, _ in counter.most_common(n+1):
                print(counter.most_common(n+1))
                # in most_common(n+1) 이므로 처음에는 A가 task
                sub_count += 1
                result += 1

                counter.subtract(task)
                # 0이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()
                print(collections.Counter())

            if not counter:
                break

            result += n - sub_count + 1

        return result


test = Solution()
print(test.leastInterval(tasks, n))
