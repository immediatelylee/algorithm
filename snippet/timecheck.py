import time
from datetime import timedelta

start = time.process_time()

# // 구현부
# sum = 0
# for i in range(10000000):
#     sum += i

end = time.process_time()

print("Time elapsed: ", end - start)  # seconds
print("Time elapsed: ", timedelta(seconds=end-start))
