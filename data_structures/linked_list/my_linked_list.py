"""
Get head / tail -> O(1)
append / prepend -> O(1)
deletion head/tail-> O(1)
Get in general -> O(N)
Insertion/Deletion in the middle -> 2 operations -> O(N) + O(1)
"""
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: Node | None = None

class MyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.length = 0

    def get(self, index):
        node = self._get_node(index)

        if not node:
            return None

        return node.data

    def append(self, data):
        if self.is_empty():
            self.head = Node(data)
            self.length += 1
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = Node(data)

        self.length += 1

    def prepend(self, data):
        if self.is_empty():
            self.head = Node(data)
            self.length += 1
            return

        old_head = self.head

        self.head = Node(data)
        self.head.next = old_head

        self.length += 1

    def insert_at(self, index, data):
        if index == 0:
            self.prepend(data)
            self.length += 1
            return

        current_node = self._get_node(index - 1)

        new_node = Node(data)
        next_node = current_node.next

        current_node.next = new_node
        new_node.next = next_node

        self.length += 1

    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self.length -= 1
            return

        current_node = self.head
        while current_node.next is not None:
            last_node = current_node
            current_node = current_node.next

            if current_node.data == data:
                next_node = current_node.next

                current_node.next = None
                last_node.next = next_node

                self.length -= 1

                return

    def remove_at(self, index):
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        current_node = self._get_node(index - 1)
        node_to_be_removed = current_node.next
        new_next_node = node_to_be_removed.next

        node_to_be_removed.next = None
        current_node.next = new_next_node
        self.length -= 1

    def _get_node(self, index):
        current_node = self.head

        for i in range(index):
            if current_node.next is None:
                return None
            current_node = current_node.next

        return current_node

    def is_empty(self):
        return self.length == 0