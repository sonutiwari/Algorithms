from collections import deque
class Queue(object):
    # create a new empty deque object that will function as a queue
    def __init__(self):
        self.queue = deque()

    # add some items to the queue
    def enqueue(self, item):
        self.queue.append(item)
    
    # pop an item off the front of the queue
    def dequeue(self):
        return self.queue.popleft()
    
    # print the queue contents
    def print(self):
        print(self.queue)
    

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.print()
queue.dequeue()
queue.print()