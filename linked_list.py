class Node:
    def __init__(self, data):
        self.data = data    # data는 값을 가리키는 변수(속성, attribute)
        self.next = None    # next는 다음 노드를 가리키는 변수

class Linked_list:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):              # Linked list의 길이를 구하는 __len__ 메서드
        return self.length

    def __str__(self):              # print 함수로 출력할 수 있는 __str__ 메서드
        if self.head is None:       # 기존 노드가 없을 때
            return "Empty List"
        node = self.head            # 노드가 head를 가리키게 함
        string = ""                 # 결과를 담아줄 빈 문자열 생성
        while node.next:            # 가장 마지막 노드로 이동
            string += str(node.data) + " -> " # 노드의 data를 -> 문자를 구분으로 string에 담아줌
            node = node.next        # 다움 노드로 이동
        return string + str(node.data) # 결과를 문자열로 반환

    def appendleft(self, data):     # 가장 앞에 노드를 추가
        node = Node(data)           # 노드 생성
        if self.head is None:       # 기존 노드가 없을 때
            self.head = node        # 헤드가 새 노드를 가리키게 함
        else:                       # 기존 노드가 있을 때
            node.next = self.head   # 새 노드의 next가 head를 가리키게 함
            self.head = node        # head가 새 노드로 옮김
        self.length += 1            # 연결 리스트의 길이를 증가시킴

    def append(self, data):         # 가장 뒤에 노드를 추가
        node = Node(data)           # 노드 생성
        if self.head is None:   # 기존 노드가 없을 때
            self.head = node    # head가 현재 노드를 가리킴
        else:                   # 기존 노드가 있을 때
            prev = self.head    # head를 prev로 옮김
            while prev.next:    # 마지막 노드로 이동
                prev = prev.next
            prev.next = node    # prev의 next가 새 노드를 가리킴
        self.length += 1            # 연결 리스트의 길이를 증가시킴

    def display(self):              # 연결 리스트의 원소를 출력하는 print 관련 메서드
        if self.head is None:       # 기존 노드가 없을 때
            print("Empty List")

        else:
            node = self.head        # node에 head가 가리키는 곳을 담아줌
            while node.next:        # 마지막 노드로 이동
                print(node.data, end=" -> ") # 노드의 데이터 출력
                node = node.next    # 다음 노드로 이동(next->head.next)
            print(node.data)

    def __contains__(self, data):   # in과 not in 연산자의 사용이 가능한 __contains__ 메서드
        node = self.head            # node에 head가 가리키는 곳을 담아줌
        while node:
            if node.data == data:
                return True
            else:
                node = node.next
        return False

    def popleft(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        self.length -= 1
        return node.data

    def pop(self):
        if self.head is None:       # 빈 리스트면 None을 반환
            return None
        node = self.head            # 노드 변수를 만들고 head를 가리킴
        if self.head.next is None:  # 노드가 하나이면 head를 None으로 만듬
            self.head = None
        else:                       # 노드가 두 개 이상이면
            while node.next:
                prev = node         # 이전 노드의 정보를 담아줌
                node = node.next    # 노드 변수를 마지막 노드까지 이동
            prev.next = None        # 이전 노드의 next가 None을 가리키게 함
        self.length -= 1            # 리스트의 길이를 줄임
        return node.data            # 노드 변수의 data를 반환

    def insert(self, index, data):
        if index <= 0:              # 인덱스가 0 이하인 경우
            self.appendleft(data)   # appendleft 메서드로 가장 앞에 삽입
        elif index >= self.length:  # 인덱스가 리스트의 길이를 넘어서는 경우
            self.append(data)       # append 메서드로 가장 뒤에 삽입
        else:
            prev = self.head        # head가 가리키는 곳을 prev에 담아줌
            for _ in range(index-1):# index 전까지 prev를 이동
                prev = prev.next
            node = Node(data)       # 새로운 노드를 생성
            node.next = prev.next   # node의 next가 prev의 next를 가리키게 함
            prev.next = node        # prev의 next에 새로운 노드를 담아줌
            self.length += 1        # 리스트의 길이를 증가시킴

    def remove(self, data):
        if self.head.data == data:  # 삭제할 노드가 head이면
            self.popleft()          # popleft 메서드를 호출
            return True
        prev = self.head            # head가 가리키는 값을 prev에 담아줌
        while prev.next:            # prev의 next가 None이 아닐때까지 진행
            if prev.next.data == data: # 삭제할 값을 찾은 경우
                prev.next = prev.next.next # 이전 노드의 next가 삭제하 노드의 next가 가리키는 노드를 가리키도록 함
                self.length -= 1    # 리스트의 길이를 줄임
                return True
            prev = prev.next        # 다음 노드를 살펴봄
        return False

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next
        return False

# mylist = Linked_list()
# mylist.append("a")
# mylist.append("b")
# mylist.append("c")

# print(mylist.length)

# mylist = Linked_list()
# mylist.append("a")
# mylist.append("b")
# mylist.append("c")
# print(mylist.__len__())

# Linked_list.display(mylist)

# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
#
# node = head
#
# while node.next:
#     node = node.next
# node.next = Node(4)
#
# node = head
#
# while node:
#     print(node.data, end=" ")
#     node = node.next

mylist = Linked_list()

for data in (1, 2, 3, 4):
    # mylist.display()
    if data % 2:
        mylist.appendleft(data)
    else:
        mylist.append(data)
# mylist.display()
print(mylist)

for data in (1, 4, 5):
    if data in mylist:
        print(f"There is {data}")
    else:
        print(f"There is no {data}")

mylist = Linked_list()
for data in (1, 2, 3, 4):
    mylist.append(data) # 1, 2, 3, 4 추가

for _ in range(len(mylist) + 1):
    print(mylist.popleft(), end=" ") # 데이터 순차적으로 꺼내기

print()

mylist = Linked_list()
for data in (1, 2, 3, 4):
    mylist.append(data)

for _ in range(data + 1):
    print(mylist.pop(), end=" ")

print()

mylist = Linked_list()
for data in (1, 2, 3, 4):
    mylist.append(data)

insert_data = ((0, 0), (2, 20), (5, 50), (7, 70))
for i, data in insert_data:
    mylist.insert(i, data)
    print(f"인덱스 {i}에 {data} 삽입:", end = " ")
    print(mylist)

mylist = Linked_list()
for data in (1, 2, 3, 4, 5, 6):
    mylist.append(data)

print(mylist)

remove_data = (1, 3, 6, 7)
for data in remove_data:
    if mylist.remove(data):
        print(f"{data} is removed.", mylist)
    else:
        print(f"There is no {data}")

# search 메서드 테스트
print("search() 메서드 테스트")
mylist = Linked_list()

for data in (1, 2, 3, 4):
    if data % 2:
        mylist.appendleft(data)
    else:
        mylist.append(data)

print(mylist)

for data in (1, 4, 5):
    if mylist.search(data):
        print(f"There is {data}")
    else:
        print(f"There is no {data}")