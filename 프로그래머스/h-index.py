citations = [3, 0, 6, 1, 5]
citations.sort(reverse=True)
print(citations)
# h-index는 n개를 초과 할수 없다.
# i보다 큰 수를 list에 넣고 갯수가 i개 이상인지확인


for n_id, n in enumerate(citations):
    print("i:", n_id, "n:", n)
    if n <= n_id:
        print(n_id)
print("len:", len(citations))
