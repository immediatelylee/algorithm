# 진법 n        리스트에 결과를 미리 저장할건데 어떤 결과를 저장할지
# 미리구할 숫자의 개수  t   내가가저야 할숫자를 가지는  반복문 몇 번 돌릴껀지  (전체 숫자)
# 게임에 참가하는 인원  m  몇번 주기로 자기의 차례가 돌아오는지
# 튜브의 순서 p

# 2,8,10,16 진법  3진법 이런것도 구현해야 하나?
n, t, m, p = 2, 4, 2, 1


num_list = []
if n == 2:
    for i in range(t*m):  # 어디까지 구해야 하나했는데 그냥 이렇게 구했다.
        num_list.append(str(bin(i)))

elif n == 8:
    for i in range(t*m):
        num_list.append(str(oct(i)))
elif n == 10:
    for i in range(t*m):
        num_list.append(str(i))
elif n == 16:
    for i in range(t*m):
        num_list.append((hex(i)))

print(num_list)
