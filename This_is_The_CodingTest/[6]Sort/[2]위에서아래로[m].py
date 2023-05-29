n=int(input())
data =[]
for _ in range(n):
    data.append(int(input()))

data.sort()
data.reverse()

for i in range(len(data)):
    print(data[i],sep=" ",end=" ")

'''
간단한 문제인데 파이썬 문법을 많이 까먹은 모양이다.

1.리버스 sort를 하기위해서 
sort -> revered 하기 보다는 옵션을 통하여 sorted(data,reverse=True)  이런식으로 진행하는 것이 좋다.

2.정답을 리스트에서 나열하는데 콤마와 리스트 형식 없이 출력하기 위해서 
print 의 end옵션만 쓰는것이 정답이다 나는 sep도 넣었는데 쓸데 없이 넣은것이다.
'''