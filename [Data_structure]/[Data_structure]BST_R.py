import random

# 이진 트리와 이진 탐색 트리의 차이
# 이진 트리: 노드의 최대 Branch가 2인 트리
# 이진 탐색 트리 (Binary Search Tree, BST): 이진 트리에 다음과 같은 추가적인 조건이 있는 트리
#   왼쪽 노드는 해당 노드보다 작은 값, 오른쪽 노드는 해당 노드보다 큰 값을 가지고 있음!


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# node를 만들고 nodemgmt에 넣는식으로 진행


class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:  # 입력된 값이 head보다 작다면 왼쪽으로 보냄
                if self.current_node.left != None:  # 왼쪽에 값이 있다면
                    # 비교대상을 바꿈 current -> current_node.left
                    self.current_node = self.current_node.left
                else:  # 왼쪽에 값이 없다면 연결
                    self.current_node.left = Node(value)
                    break

            else:  # 입력된 값이 head보다 크다면 오른쪽으로 보냄
                if self.current_node.right != None:  # 오른쪽에 값이 있다면
                    # 비교대상을 바꿈 current -> current_node.right
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head  # 헤드 설정
        while self.current_node:
            if self.current_node.value == value:  # value 값을 찾으면 반환
                return value
            elif value < self.current_node.value:  # 밸류값이 작으면
                self.current_node = self.current_node.left  # current -> current.left
            else:  # value 값이 크면
                self.current_node = self.current_node.right  # current -> current.right
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
            if self.current_node.value == value:  # 삭제하기로한 value와 head value가 맞으면
                searched = True
                break
            elif value < self.current_node.value:  # 삭제하기로한 value가 작으면 head보다
                self.parent = self.current_node  # 부모를 현재 노드로 바꾸고
                self.current_node = self.current_node.left  # 현재노드는 왼쪽으로 current -> current.left
            else:
                self.parent = self.current_node  # 부모를 현재도느로 바꾸고
                # 현재노드는 오른쪽으로 current -> current.right
                self.current_node = self.current_node.right

        if searched == False:
            return False

        # self.current_node 가 삭제할 Node, self.parent는 삭제할 Node의 Parent Node인 상태
        # 삭제할 노드가 leaf 노드라면(No child)
        # case 1
        if self.current_node.left == None and self.current_node.right == None:
            # value가 부모노드보다 작다면(삭제할노드의 1level 위의노드)
            if value < self.parent.value:
                self.parent.left = None  # 왼쪽 노드 연결 끊기

            else:  # value가 부모노드 보다 크다면
                self.parent.right = None                        # 오른쪽 연결 끊기
            del self.current_node                               # 없어도 되지만 클린코드를 위해 삭제를 명시
        # case 2
        if self.current_node.left != None and self.current_node.right == None:  # 삭제할 노드가 왼쪽에 child가 있을때
            if value < self.parent.value:  # value값이 작다면 (부모노드의 왼쪽노드가 current)
                self.parent.left = self.current_node.left       # 삭제할 노드의 자식노드를 부모 노드와 연결

            else:                                               # 부모노드의 오른쪽 노드가 current
                # value 값이 크다면 (부모노드 의 오른쪽 노드가 current)
                self.parent.right = self.current_node.left

        elif self.current_node.left == None and self.current_node.right != None:  # 삭제할 노드의 오른쪽에 child가 있을때
            if value < self.parent.value:  # value값이 작다면 (부모노드의 왼쪽노드가 current)
                self.parent.left = self.current_node.right

            else:                                               # value 값이 크다면 부모노드의 오른쪽 노드가 current
                self.parent.right = self.current_node.right

        if self.current_node.left != None and self.current_node.right != None:  # case3  삭제할 노드의  child 두개가 있을때

            # case3-1    change_node 설정하는 방식은 두가지
            # 1. 삭제 후에 삭제할 노드의 오른쪽 자식중 가장 작은 노드가 삭제할 노드를 대체하는 경우   <- 여기서는 1번케이스를 사용
            # 2. 삭제 후에 삭제할 노드의 왼쪽 자식중 가장 큰 노드가 삭제할 노드를 대체하는 경우
            # 왼쪽 child인 경우에는 그 자체가 작은 값이므로 change_node가 된다.
            if value < self.parent.value:

                self.change_node = self.current_node.right
                # 순회 초기이므로 change_node == change_node_parent (삭제할 노드(current)의 오른쪽 오드)
                self.change_node_parent = self.current_node.right

                # 왼쪽에 있는 노드 순회  - 삭제할 노드의 오른쪽 부분에서 가장 작은 값을 current과 변경할것이기 때문
                while self.change_node.left != None:
                    # 아래로 가기위한 변경 change_parent -> change_node
                    self.change_node_parent = self.change_node
                    # change_node -> change_node_left
                    self.change_node = self.change_node.left

                if self.change_node.right != None:                  # change_node 오른쪽 노드가 있다면
                    # change_parent노드의 왼쪽에 연결한다.
                    self.change_node_parent.left = self.change_node.right

                else:                                               # change_node에 child 노드가 없다면
                    # change_parent 의왼쪽 노드를 None으로 둔다
                    self.change_node_parent.left = None
                # 삭제할 위치에 노드에 change_node로 변경해주고
                self.parent.left = self.change_node
                # change_node 오른쪽에 삭제할 노드의 오른쪽 노드를 연결
                self.change_node.right = self.current_node.right
                # change_node 왼쪽에 current_node.left
                self.change_node.left = self.current_node.left

            # case 3-2
            else:    # 삭제할 노드가 head 오른쪽
                self.change_node = self.current_node.right   # 순회 초기 세팅
                self.change_node_parent = self.current_node.right

                # 순회  오른쪽 노드중에서 가장 크기가 작은 노드 선택
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left

                # 선택한 노드가 오른쪽 노드를 가지고 있는 경우
                if self.change_node.right != None:
                    # 오른쪽 노드를 change_node부모의 왼쪽노드로 연결
                    self.change_node_parent.left = self.change_node.right
                else:  # 자식 노드가 없는 경우
                    self.change_node_parent.left = None  # change_node의 부모 왼쪽 노드 봉인
                self.parent.right = self.change_node  # 삭제할노드를 변경노드로 변경
                self.change_node.right = self.current_node.right  # 변경노드의 오른쪽으로 삭제할 노드의 오른쪽 노드로 변경
                self.change_node.left = self.current_node.left  # 변경노드의 왼쪽을 삭제할 노드의 왼쪽 노드로 변경

        return True


# test code
# 0 ~ 999 중, 100 개의 숫자 랜덤 선택
bst_nums = set()
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0, 999))
# print (bst_nums)

# 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함
head = Node(500)
binary_tree = NodeMgmt(head)
for num in bst_nums:
    binary_tree.insert(num)

# 입력한 100개의 숫자 검색 (검색 기능 확인)
for num in bst_nums:
    if binary_tree.search(num) == False:
        print('search failed', num)

# 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0, 99)])

# 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
        print('delete failed', del_num)
