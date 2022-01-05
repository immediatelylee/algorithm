# https://leetcode.com/problems/different-ways-to-add-parentheses/
from typing import List

expression = "2*3-4*5"
# expression = "2-1-1"


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        def compute(left, right, op):
            results = []

            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))

            return results

        if expression.isdigit():
            return [int(expression)]

        results = []

        for index, value in enumerate(expression):
            if value in "-+*":
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index + 1:])

                results.extend(compute(left, right, value))
        return results


test = Solution()
test.diffWaysToCompute(expression)
