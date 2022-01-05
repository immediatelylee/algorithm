# https://leetcode.com/problems/fibonacci-number/


n = 4


class Solution:
    def fib(self, n: int) -> int:

        f = [0, 1]
        result = 0
        # fn = fn-1 + fn-2

        if n == 0:
            result = 0
            return result
        elif n == 1:
            result = 1
            return result
        else:
            for i in range(2, n+1):
                f.append(f[i-1]+f[i-2])

            result = f[-1]
            return result


test = Solution()
print(test.fib(n))
