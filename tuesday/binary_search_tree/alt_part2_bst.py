    def in_order_print(self, node):
        # Base case
        if node is None:
            return
        else:
            # Start printing from the far left(lowest # always furthest to the left)
            # Recursively print from low to high, left to right
            # (Print order not node values)
            #    4
            #  2   5
            # 1 3 6 7
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # BFT = FIFO = Queue
    def bft_print(self, node):
        # Instantiate the queue class
        queue = Queue()
        # Start the queue at the root node
        queue.enqueue(node)
        # While loop to check the size of the queue until its empty
        while queue.size > 0:
            # Pointer variable (updates beginning of each loop)
            current_node = queue.dequeue()
            # Iteratively print from high to low, left to right
            # (Print order not node values)
            #    1
            #  2   3
            # 4 5 6 7
            print(current_node.value)
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # DFT = LIFO = Stack
    def dft_print(self, node):
        # Instantiate the stack class
        stack = Stack()
        # Start the stack at the root node
        stack.push(node)
        # While loop to check the size of the stack until its empty
        while stack.size > 0:
            # Pointer variable (updates beginning of each loop)
            current_node = stack.pop()
            # Iteratively print from high to low, left to right
            # (Print order not node values)
            #    1
            #  2   5
            # 3 4 6 7
            print(current_node.value)
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)
    # Stretch Goals -------------------------
    # Note: Research may be required
    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # Base case
        if node is None:
            return
        else:
            # Start printing from the top
            # Recursively print from high to low, left to right
            # (Print order not node values)
            #    1
            #  2   5
            # 3 4 6 7
            print(node.value)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)
    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # Base case
        if node is None:
            return
        else:
            # Start printing from the far left(lowest # always furthest to the left)
            # Recursively print from low to high, left to right
            # (Print order not node values)
            #    7
            #  5   6
            # 1 2 3 4
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)

#alt dft_print

    def dft_print(self, node):
        stack = []
        stack.append(node)
        while stack:
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
            print(node.value)
            node = stack.pop()