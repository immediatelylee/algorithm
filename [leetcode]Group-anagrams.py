import collections
# https://leetcode.com/problems/group-anagrams/

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = collections.defaultdict(list)

# for word in strs:
#     print(sorted(word))
for word in strs:
    anagrams[''.join(sorted(word))].append(word)

print(anagrams.values())

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagrams = collections.defaultdict(list)

#         for word in strs:
#             anagrams[''.join(sorted(word))].append(word)

#         return anagrams.values()
