
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert_left(self, current_node, value):
        if current_node.left is None:
            current_node.left = Node(value)
        else:
            new_node = Node(value)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, value):
        if current_node.right is None:
            current_node.right = Node(value)
        else:
            new_node = Node(value)
            new_node.right = current_node.right
            current_node.right = new_node

    def inorder_traversal(self, start, traversal):
        """
        Perform in-order traversal of the binary tree.
        In-order traversal visits nodes in the following order:
        1. Traverse the left subtree.
        2. Visit the root node.
        3. Traverse the right subtree.
        Args:
            start (TreeNode): The starting node of the traversal.
            traversal (str): The string that accumulates the traversal result.
        Returns:
            str: The traversal result as a string with node values separated by '-'.
        """
        
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    def delete_node(self, root, key):
        """
        Deletes a node with the given key in the binary tree.
        Uses the in-order successor approach for node replacement.
        """
        if root is None:
            return root
        
        if key < root.value:
            root.left = self.delete_node(root.left, key)
        elif key > root.value:
            root.right = self.delete_node(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # Node with two children: get the in-order successor (smallest in right subtree)
            min_node = self.get_min(root.right)
            root.value = min_node.value
            root.right = self.delete_node(root.right, min_node.value)
        
        return root

    def get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, root, key):
        """
        Searches for a node with the given key in the binary tree.
        Returns the node if found, otherwise returns None.
        """
        if root is None or root.value == key:
            return root
        
        # Search in left subtree
        left_search = self.search(root.left, key)
        if left_search:
            return left_search
        
        # Search in right subtree
        return self.search(root.right, key)
       

    def create_expression_tree(self, expression):
        """
        Create an arithmetic expression tree from a list of tokens
        Args:
            expression: List of strings representing the expression in postfix notation
            Example: ["4", "5", "+", "7", "3", "-", "*"] for (4 + 5) * (7 - 3)
        """
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in expression:
            node = Node(token)
            if token in operators:
                # Operator node: pop two operands and attach them
                node.right = stack.pop()
                node.left = stack.pop()
            stack.append(node)
            
        self.root = stack[0]
        return self.root

    def evaluate_expression(self, node):
        """
        Evaluate the arithmetic expression tree
        Args:
            node: Root node of the expression tree
        Returns:
            float: Result of the expression
        """
        if node is None:
            return 0
        
        # Leaf node (operand)
        if node.left is None and node.right is None:
            return float(node.value)
        
        # Evaluate left and right subtrees
        left_val = self.evaluate_expression(node.left)
        right_val = self.evaluate_expression(node.right)
        
        # Apply operator
        if node.value == '+':
            return left_val + right_val
        elif node.value == '-':
            return left_val - right_val
        elif node.value == '*':
            return left_val * right_val
        elif node.value == '/':
            return left_val / right_val