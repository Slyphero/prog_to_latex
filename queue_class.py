class Queue:
    def __init__(self):
        self.keywords = []

    def is_empty(self):
        return self.keywords == []

    def empty(self):
        self.keywords.clear()

    def queue(self, element):
            self.keywords.insert(0, element)

    def unqueue(self):
        assert not self.is_empty(), 'Empty queue'
        return self.keywords.pop()

    def queue_first(self):
        assert not self.is_empty(), 'Empty queue'
        return self.keywords[-1]


