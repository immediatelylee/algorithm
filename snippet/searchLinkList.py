
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)
