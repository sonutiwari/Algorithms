class Stack(object):
    # create a new empty stack
    def __init__(self):
        self.stack = []

    # push items onto the stack
    def push(self, item):
        self.stack.append(item)
    

    # print the stack contents
    def print(self):
        print(self.stack)

    # pop an item off the stack
    def pop(self):
        return self.stack.pop()
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.print()
print(stack.pop())
stack.print()