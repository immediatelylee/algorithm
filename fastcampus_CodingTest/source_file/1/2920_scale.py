scale = list(map(int, input().split()))

ascending = True
descending = True

for i in range(1, 8):
    if scale[i] > scale[i-1]:
        descending = False
    else:
        ascending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')
