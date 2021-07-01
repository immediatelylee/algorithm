class Reader:
    def __init__(self, file):
        self.file = open(file, 'r')
        self.is_done = False

    def read_char(self):
        # 이곳에 들어갈 코드를 작성하세요
        pass

        # day3.txt 내용:
        # a1b22c333d4444


reader = Reader('day3.txt')
while not reader.is_done:
    print(reader.read_char(), end='')

# 출력:
# abcd

# 답
    # with open('./day3.txt', 'r') as f:
    #     c = f.read()
    #     c = c.replace('1', '')
    #     c = c.replace('2', '')
    #     c = c.replace('3', '')
    #     c = c.replace('4', '')

    #     self.is_done = True
    #     return c
