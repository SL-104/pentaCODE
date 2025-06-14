class Stack:
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("The stack is empty.")
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("The stack is empty.")
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)


# Define operator precedence
operators = "+-*/^"
left_parenthesis = "("
right_parenthesis = ")"

def operator_precedence(operator):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    return precedence.get(operator, 0)

def shunting_yard_with_steps(expression):
    output = ""
    operator_stack = Stack()
    steps = []  # List to store each step

    for char in expression:
        if char.isalnum():  # If the character is an operand
            output += char
            steps.append(f"Output: {output}, Stack: {operator_stack.stack}")
        elif char == left_parenthesis:
            operator_stack.push(char)
            steps.append(f"Output: {output}, Stack: {operator_stack.stack}")
        elif char == right_parenthesis:
            while not operator_stack.is_empty() and operator_stack.peek() != left_parenthesis:
                output += operator_stack.pop()
                steps.append(f"Output: {output}, Stack: {operator_stack.stack}")
            operator_stack.pop()  # Remove the left parenthesis
            steps.append(f"Output: {output}, Stack: {operator_stack.stack}")
        elif char in operators:
            while (not operator_stack.is_empty() and
                   operator_stack.peek() != left_parenthesis and
                   operator_precedence(operator_stack.peek()) >= operator_precedence(char)):
                output += operator_stack.pop()
                steps.append(f"Output: {output}, Stack: {operator_stack.stack}")
            operator_stack.push(char)
            steps.append(f"Output: {output}, Stack: {operator_stack.stack}")

    while not operator_stack.is_empty():
        output += operator_stack.pop()
        steps.append(f"Output: {output}, Stack: {operator_stack.stack}")

    return output, steps

