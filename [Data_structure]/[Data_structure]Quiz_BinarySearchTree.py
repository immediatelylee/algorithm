class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, comp=None):
        if comp is None:
            self.comp = lambda a, b: a-b
        else:
            self.comp = comp
        self.root = None

    def add(self, data):
        pass
        # self.current_

    def search(self, data):
        pass
        # self.current_node =


bst = BinarySearchTree(comp=lambda a, b: hash(a)-hash(b))
print(bst)

# for c in 'qwyhwef':
#     bst.add(c)


# for c in 'qwyhwefjdhfdve':
#     print(1 if bst.search(c) else 0, end='')
