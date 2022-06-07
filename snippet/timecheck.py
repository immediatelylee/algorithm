from timeit import default_timer as timer
from datetime import timedelta

start = timer()

# // 구현부
# sum = 0
# for i in range(10000000):
#     sum += i

end = timer()

print("Time elapsed: ", end - start)  # seconds
print("Time elapsed: ", timedelta(seconds=end-start))
