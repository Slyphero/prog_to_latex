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
    
    def evaluate_binary(self, operator, operand1, operand2):
        if operator == "/":
            return operators.frac(operand1, operand2)
        if operator == "lim":
            return operators.lim(operand1, operand2)
        
    def evaluate_ternary(self, operator, operand1, operand2, operand3):
        if operator == "sum":
            return operators.sum(operand1, operand2, operand3)
        if operator == "prod":
            return operators.prod(operand1, operand2, operand3)
        
    def evaluate_other(self, operator):
        if operator == "in":
            return "\\in"
        if operator == "inc":
            return "\\subset"
        if operator == "nN":
            return "\\mathbb{N}"
        if operator == "zZ":
            return "\\mathbb{Z}"
        if operator == "qQ":
            return "\\mathbb{Q}"
        if operator == "rR":
            return "\\mathbb{R}"
        if operator == "cC":
            return "\\mathbb{C}"
        if operator == "forall":
            return "\\forall"
        if operator == "exists":
            return "\\exists"
        if operator == "*":
            return "\\times"
        if operator == "<=":
            return "\\leq"
        if operator == ">=":
            return "\\geq"
        if operator == "==>":
            return "\\implies"
        if operator == "<==>":
            return "\\iff"
        if operator == "!=":
            return "\\neq"

    def convert_others_operators(self):
        length = len(self.tokens)
        for i in range(length):
            if self.tokens[i] in operators.OTHER_OPERATORS.keys():
                self.tokens[i] = operators.OTHER_OPERATORS[self.tokens[i]]

    def infix_to_postfix(self):
        operators_stack = stack.Stack()
        postfix_stack = stack.Stack()

        for token in self.tokens:
            if token not in operators.OPERATORS:
                postfix_stack.stack(token)
            elif token == '[':
                operators_stack.stack(token)

        while not operators_stack.is_empty():
            postfix_stack.stack(operators_stack.unstack())

        return postfix_stack
