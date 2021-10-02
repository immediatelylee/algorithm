import re
import collections
# https://leetcode.com/problems/most-common-word/


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# paragraph.split()

words = [word for word in (
    re.sub("[^\w ]", '', paragraph)).lower().split() if word not in banned]

counts = collections.Counter(words)
print(counts.most_common(1))
