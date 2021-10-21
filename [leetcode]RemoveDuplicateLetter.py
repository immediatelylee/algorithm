# https://leetcode.com/problems/remove-duplicate-letters/

# s = "bcabc"
s = "cbacdcbc"
stack = []

for i in s:
    if i not in stack:
        stack.append(i)

    else:
        continue

result = sorted(stack)

print("".join(result))
