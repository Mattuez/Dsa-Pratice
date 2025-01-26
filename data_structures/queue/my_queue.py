class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: Node | None = None

class MyQueue:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length = 0

    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return

        tail = self.tail
        tail.next = new_node
        self.tail = new_node
        self.length += 1

    def pop(self):
        if self.is_empty():
            return None

        data = self.head.data
        self.head = self.head.next
        self.length -= 1

        return data

    def peek(self):
        if self.is_empty():
            return None

        return self.head.data

    def is_empty(self):
        return self.length == 0