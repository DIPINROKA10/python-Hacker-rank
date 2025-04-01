class QueueUsingTwoStacks:
    def __init__(self):
        self.stack_enqueue = []  # Stack for enqueue operations
        self.stack_dequeue = []  # Stack for dequeue operations
    
    def enqueue(self, x):
        self.stack_enqueue.append(x)
    
    def dequeue(self):
        self._shift_stacks()
        if self.stack_dequeue:
            self.stack_dequeue.pop()
    
    def front(self):
        self._shift_stacks()
        if self.stack_dequeue:
            print(self.stack_dequeue[-1])
    
    def _shift_stacks(self):
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())

# Read input
q = int(input())
queue = QueueUsingTwoStacks()

for _ in range(q):
    query = input().split()
    if query[0] == '1':
        queue.enqueue(int(query[1]))
    elif query[0] == '2':
        queue.dequeue()
    elif query[0] == '3':
        queue.front()
