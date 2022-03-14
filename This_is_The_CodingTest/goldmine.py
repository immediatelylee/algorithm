

t = int(input())


for _ in range(t):
    n, m = map(int, input().split())
    gold_mine = [[] for _ in range(n)]
    input_gold = list(map(int, input().split()))
    for index, gold in enumerate(input_gold):
        gold_mine[index // m].append(gold)

result = 0
