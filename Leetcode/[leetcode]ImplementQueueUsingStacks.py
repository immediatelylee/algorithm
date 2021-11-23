# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []


class MyQueue1:
    def __init__(self):
        self.input = []

    def push(self, x):
        self.input.append(x)

    def pop(self):

        return self.input.pop(0)

    def peek(self):
        # output이 없으면 모두 재입력

        return self.input[0]

    def empty(self):
        return self.input == []
