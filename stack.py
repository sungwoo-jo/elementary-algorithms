class Node:
    def __init__(self, data):       # data 넣어주고 next는 None으로 초기화
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None             # 초기 스택의 top은 None

    def push(self, data):           # push
        node = Node(data)           # 새로운 노드 생성
        if self.top is None:        # 스택에 데이터가 없다면
            self.top = node         # 새로 생성한 노드를 top에 넣기
        else:                       # 스택에 데이터가 있다면
            node.next = self.top    # 새로운 노드의 next를 top으로 잡아줌
            self.top = node         # top에 새로운 노드를 넣어주기

    def pop(self):                  # pop
        if self.top is None:        # 스택에 데이터가 없다면
            return None             # None 반환
        node = self.top             # node에 top의 데이터를 담아줌
        self.top = node.next        # top에 다음 노드의 주소를 담아줌
        return node.data            # 노드의 값 반환

    def peek(self):                 # peek
        if self.top is None:        # 스택에 데이터가 없다면
            return None             # None 반환
        return self.top.data        # 데이터 반환

    def is_empty(self):             # is_empty
        return self.top is None     # top이 비어있는 지 확인

if __name__ == "__main__":
    s = Stack()

    for i in range(3):
        s.push(chr(ord("A") + i))
        print(f"Push data = {s.peek()}")
    print()

    while not s.is_empty():
        print(f"Pop data = {s.pop()}")
    print()

    print(f"Peek data = {s.peek()}")

    print(f"is_empty = {s.is_empty()}")