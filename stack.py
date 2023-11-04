class Stack:
    def __init__(self):
        self.keywords = []

    def is_empty(self):
        return self.keywords == []

    def empty(self):
        self.keywords.clear()

    def stack(self, element):
        self.keywords.append(element)

    def unstack(self):
        assert not self.is_empty(), 'Empty stack'
        return self.keywords.pop()

    def stack_top(self):
        assert not self.is_empty(), 'Empty stack'
        return self.keywords[-1]
