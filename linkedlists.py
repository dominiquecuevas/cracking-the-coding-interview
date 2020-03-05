class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"<LLNode data={self.data}>"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        current = self.head
        print("List: ")
        while current != None:
            print(current)
            current = current.next

    def find(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def append(self, data):
        new_node = LLNode(data)

        if self.head is None:
            self.head = new_node
        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    def remove(self, data):
        current = self.head
        if current.data == data:
            self.head = current.next
            if self.head is None:
                self.tail = None
            return
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                return
            current = current.next

    def size(self):
        nodes = 0
        stack = [self.head]
        while stack:
            current = stack.pop()
            nodes += 1
            if current.next:
                stack.append(current.next)
        return nodes

    def __repr__(self):
        return f"<LinkedList>"