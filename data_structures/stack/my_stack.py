class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: Node | None = None

class MyStack:
    def __init__(self):
        self.head: Node | None = None
        self.length = 0

    def push(self, data):
        new_head = Node(data)

        if self.is_empty():
            self.head = new_head
            self.length += 1
            return

        old_head = self.head
        new_head.next = old_head
        self.head = new_head

        self.length += 1

    def pop(self):
        if self.is_empty():
            return None

        old_head = self.head
        new_head = old_head.next
        self.head = new_head

        self.length -= 1

        return old_head.data

    def peek(self):
        if self.is_empty():
            return None

        return self.head.data

    def is_empty(self):
        return self.length == 0