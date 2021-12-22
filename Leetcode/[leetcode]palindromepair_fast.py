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
        # create a mapping from a reversed word to the index
        worddict = {w[::-1]: i for i, w in enumerate(words)}

        res = set()
        for i, w in enumerate(words):
            for j in range(len(w)+1):
                prefix = w[:j]
                suffix = w[j:]
                if prefix in worddict and (index := worddict[prefix]) != i and suffix == suffix[::-1]:
                    res.add((i, index))
                if suffix in worddict and (index := worddict[suffix]) != i and prefix == prefix[::-1]:
                    res.add((index, i))

        return res


test = Solution()
print(test.palindromePairs(words))
