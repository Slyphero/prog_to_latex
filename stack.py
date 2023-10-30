class Stack:
    def __init__(self):
        self.keywords = []

    def is_empty(self):
        return self.keywords == []

    def stack(self, element):
        self.keywords.append(element)

    def unstack(self):
        assert not self.is_empty(), 'Empty stack'
        return self.keywords.pop()

    def empty(self):
        while self.keywords != []:
            self.keywords.pop()

    def stack_top(self):
        assert not self.is_empty(), 'Empty stack'
        return self.keywords[-1]
    
    def last_index(self):
        return len(self.keywords) - 1
