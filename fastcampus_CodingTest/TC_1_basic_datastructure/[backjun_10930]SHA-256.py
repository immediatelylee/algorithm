# https://www.acmicpc.net/problem/10930

import hashlib

word = input()
data_hash = hashlib.sha256(word.encode())

print(data_hash.hexdigest())
