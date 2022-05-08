from hashlib import sha1

f = open("list1.csv", 'w')

for i in range(16593497, 99999999):

    result = str(i) + "salt_for_you"

    for j in range(0, 500):
        result = sha1(result.encode('utf-8')).hexdigest()

    print(str(i) + ", " + result)
    f.write(str(i) + ", " + result + "\n")

f.close()
