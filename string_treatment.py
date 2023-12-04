import stack
import operators

class Token:
    def __init__(self, string_input):
        self.tokens = string_input.split(" ")         

    def verify_brackets(self):
        brackets_stacks = stack.Stack()
        for token in self.tokens:
            if token == '[' or token == '(':
                brackets_stacks.stack(token)
            elif token == ')':
                if (not brackets_stacks.is_empty()) and (brackets_stacks.stack_top() == '('):
                    brackets_stacks.unstack()
                else:
                    return False
            elif token == ']':
                if (not brackets_stacks.is_empty()) and (brackets_stacks.stack_top() == '['): 
                    brackets_stacks.unstack()
                else:
                    return False
        return brackets_stacks.is_empty()
    
    
