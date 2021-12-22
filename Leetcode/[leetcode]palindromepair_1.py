# https://leetcode.com/problems/palindrome-pairs/

# Constrants

# 1 <= words.length <= 5000
# 0 <= words[i].length <= 300
# words[i] consists of lower-case English letters.

from typing import List
words = ["abcd", "dcba", "lls", "s", "sssll"]
# words = ["bat","tab","cat"]
# words = ["a",""]


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return word[:] == word[::-1]

        output = []

        # for i in range(len(words)):
        #     for j in range(i, len(words)):
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                if is_palindrome(word1 + word2):
                    output.append([i, j])

        return output


test = Solution()
print(test.palindromePairs(words))
