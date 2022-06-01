# [구현]

def binary_search(data, find):
    print(data)
    if len(data) == 1 and find == data[0]:
        return True
    if len(data) == 1 and find != data[0]:
        return False
    if len(data) == 0:
        return False

    medium = len(data) // 2
    if find == data[medium]:
        return True
    else:
        if find > data[medium]:
            return binary_search(data[medium + 1:], find)
        else:
            return binary_search(data[:medium], find)
