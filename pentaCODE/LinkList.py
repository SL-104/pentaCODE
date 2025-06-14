class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def printLinkedList(self):
        movies = []
        current_node = self.head
        while current_node:
            movies.append(current_node.data)
            current_node = current_node.next
        return movies

    def remove_beginning(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return removed_data

    def remove_at_end(self):
        if not self.head:
            return None
        if self.head == self.tail:
            removed_data = self.head.data
            self.head = None
            self.tail = None
            return removed_data
        current_node = self.head
        while current_node.next != self.tail:
            current_node = current_node.next
        removed_data = self.tail.data
        self.tail = current_node
        self.tail.next = None
        return removed_data

    def remove_at(self, data):
        if not self.head:
            return None
        if self.head.data == data:
            return self.remove_beginning()
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next
        if not current_node.next:
            return None
        removed_data = current_node.next.data
        if current_node.next == self.tail:
            self.tail = current_node
        current_node.next = current_node.next.next
        return removed_data

