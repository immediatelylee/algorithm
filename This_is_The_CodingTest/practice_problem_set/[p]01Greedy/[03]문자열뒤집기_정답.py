s = input()
count0 = 0  # 모두 0으로 뒤집기
count1 = 0  # 모두 1로 뒤집기

# 첫 번째 원소에 대해서 처리
if s[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(s)-1):
    if s[i] != s[i+1]:  # 다음 수에서 1로 바뀌는 경우
        if s[i+1] == '1':
            count0 += 1
        else:  # 다음 수에서 0으로 바뀌는 경우
            count1 += 1

print(min(count0, count1))

'''
다솜이는 모든 숫자를 전부 같게 만드는 것이 목적이다. 
따라서 전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에서 
더 적은 횟수를 가지는 경우를 계산하면 된다. 이를 구현할 때는 
전체 리스트의 원소를 앞에서부터 하나씩 확인하며, 0에서 1로 변경하거나 1에서 0으로 
변경하는 경우를 확인하는 방식으로 해결할 수 있다.
'''
