import random


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return value
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False


# test code
# head = Node(1)
# BST = NodeMgmt(head)
# BST.insert(2)
# BST.insert(3)
# BST.insert(0)
# BST.insert(4)
# BST.insert(8)
# print(BST.search(-1))
# print(BST.search(8))

def delete(self, value):
    searched = False
    self.current_node = self.head
    self.parent = self.head
    while self.current_node:
        if self.current_node.value == value:
            searched = True
            break
        elif value < self.current_node.value:
            self.parent = self.current_node
            self.current_node = self.current_node.left
        else:
            self.parent = self.current_node
            self.current_node = self.current_node.right

    if searched == False:
        return False

    # case1 삭제후 봉인
    if self.current_node.left == None and self.current_node.right == None:
        if value < self.parent.value:
            self.parent.left = None

        else:
            self.parent.left = None
        del self.current_node

    # case2
    if self.current_node.left != None and self.current_node.right == None:
        if value < self.parent.value:
            self.parent.left = self.current_node.left
        else:
            self.parent.right = self.current_node.left
    elif self.current_node.left == None and self.current_node.right != None:
        if value < self.parent.value:  # value값이 작다면 (부모노드의 왼쪽노드가 current)
            self.parent.left = self.current_node.right

        else:                                               # value 값이 크다면 부모노드의 오른쪽 노드가 current
            self.parent.right = self.current_node.right

    if self.current_node.left != None and self.current_node.right != None:  # case3  삭제할 노드의  child 두개가 있을때
        # 삭제할 노드 위치 왼쪽 + 왼쪽에서 가장큰 노드의 child가 x
        if value < self.parent.value:
            self.change_node = self.current_node.left
            self.change_node_parent = self.current_node.left

            while self.change_node.right != None:
                self.change_node.parent = self.change_node
                self.change_node = self.change_node.right

            if self.change_node.left != None:
                self.change_node_parent.right = self.change_node.left

            else:
                self.change_node_parent.right = None
            self.parent.right = self.change_node
            self.change_node.left = self.current_node.left
            self.change_node.right = self.current_node.right
