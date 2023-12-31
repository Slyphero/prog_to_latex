import stack
import queue_class 
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
        operator_stack = stack.Stack()
        output = queue_class.Queue()

        for token in self.tokens:
            if token in operators.OPERATORS:
                operator_stack.stack(token)
            elif token == '[':
                operator_stack.stack(token)
            elif token == ']':
                while operator_stack.stack_top() != '[':
                    output.queue(operator_stack.unstack())
                operator_stack.unstack()
            else:
                output.queue(token)
        while not operator_stack.is_empty():
            output.queue(operator_stack.unstack())

        return list(reversed(output.keywords))
    