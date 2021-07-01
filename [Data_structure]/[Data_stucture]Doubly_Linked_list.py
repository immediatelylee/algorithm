class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert_before(self, data, before_data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.next = node
            return True

    def insert_after(self, data, after_data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.head
            while node.data != after_data:
                node = node.next
                if node == None:
                    return False
            new = Node(data)
            after_new = node.next
            new.next = after_new
            new.prev = node
            node.next = new
            if new.next == None:
                self.tail = new
            return True

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


# 연습1: 위 코드에서 노드 데이터가 2인 노드 삭제해보기

# node_mgmt.delete(2)
# node_mgmt.desc()

# 연습2: 위 코드에서 노드 데이터가 특정 숫자인 노드를 찾는 함수를 만들고, 테스트해보기
# 테스트: 임의로 1 ~ 9까지 데이터를 링크드 리스트에 넣어보고, 데이터 값이 4인 노드의 데이터 값 출력해보기

# # 테스트
# node_mgmt = NodeMgmt(0)
# for data in range(1, 10):
#     node_mgmt.add(data)

# node = node_mgmt.search_node(4)
# print (node.data)


# 연습3: 위 코드에서 노드 데이터가 특정 숫자인 노드 앞에 데이터를 추가하는 함수를 만들고, 테스트해보기
# - 더블 링크드 리스트의 tail 에서부터 뒤로 이동하며, 특정 숫자인 노드를 찾는 방식으로 함수를 구현하기
# - 테스트: 임의로 0 ~ 9까지 데이터를 링크드 리스트에 넣어보고, 데이터 값이 2인 노드 앞에 1.5 데이터 값을 가진 노드를 추가해보기

# double_linked_list = NodeMgmt(0)
# for data in range(1, 10):
#     double_linked_list.insert(data)
# double_linked_list.desc()


# 연습4: 위 코드에서 노드 데이터가 특정 숫자인 노드 뒤에 데이터를 추가하는 함수를 만들고, 테스트해보기
# - 더블 링크드 리스트의 head 에서부터 다음으로 이동하며, 특정 숫자인 노드를 찾는 방식으로 함수를 구현하기
# - 테스트: 임의로 0 ~ 9까지 데이터를 링크드 리스트에 넣어보고, 데이터 값이 1인 노드 다음에 1.7 데이터 값을 가진 노드를 추가해보기

# node_mgmt = NodeMgmt(0)
# for data in range(1, 10):
#     node_mgmt.insert(data)

# node_mgmt.desc()

# node_mgmt.insert_after(1.5, 1)
# node_mgmt.desc()
