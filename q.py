class Q():
    """
        A FILO queue implemented using two stacks
    """
    def __init__(self):
        self.stack_one = []
        self.stack_two = []

    def enqueue(self, item):
        while self.stack_two:
            self.stack_one.append(self.stack_two.pop())
        self.stack_two.append(item)
        while self.stack_one:
            self.stack_two.append(self.stack_one.pop())

    def dequeue(self):
        return self.stack_two.pop()
