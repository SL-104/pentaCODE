class Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self) -> bool:
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def bulk_queue(self, items:list):
        self.queue.extend(items)
    
    def dequeue(self):
        if self.is_empty():
            return Exception("Queue is empty, cannot dequeue")
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)

class Deque():
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def add_left(self, item):
        self.items.insert(0, item)
    
    def add_right(self, item):
        self.items.append(item)

    def bulk_left(self, items: list):
        for item in reversed(items): self.add_left(item)

    def bulk_right(self, items:list):
        self.items.extend(items)

    def remove_left(self):
        if self.is_empty():
            return Exception("Deque is empty, cannot remove front.")
        return self.items.pop(0)
    
    def remove_right(self):
        if self.is_empty():
            return Exception("Deque is empty, cannot remove rear.")
        return self.items.pop()
    
    def size(self):
        return len(self.items)




