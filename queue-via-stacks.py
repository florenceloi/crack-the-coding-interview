class Stack(object):

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, item):
        self.stack.append(item)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception('Stack is empty')
        self.size -= 1
        return self.stack.pop()

    def peek(self):
        if self.size == 0:
            raise Exception('Stack is empty')
        return self.stack[-1]

    def is_empty(self):
        return self.size == 0


class My_Queue(object):

    def __init__(self):
        self.original = Stack()
        self.temp = Stack()

    def __repr__(self):
        return "Original: %s \nTemp: %s" % (self.original.stack,
                                            self.temp.stack[::-1])

    def enqueue(self, item):
        if not self.temp.is_empty():
            self.transfer_all(self.temp, self.original)
        self.original.push(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        if not self.original.is_empty():
            self.transfer_all(self.original, self.temp)
        return self.temp.pop()

    def transfer_all(self, give, take):
        while not give.is_empty():
            item = give.pop()
            take.push(item)

    def is_empty(self):
        return self.original.is_empty() and self.temp.is_empty()


###############################################################################
if __name__ == '__main__':

    # Test Stack class
    nums = Stack()
    nums.push(1)
    nums.push(2)
    nums.push(3)
    print nums.stack
    nums.peek()
    print nums.pop()
    print nums.stack
    print nums.is_empty()
    print nums.pop()
    print nums.pop()
    print nums.is_empty()

    print "\n", "=" * 10

    # Test My_Queue class
    more_nums = My_Queue()
    more_nums.enqueue(1)
    more_nums.enqueue(2)
    more_nums.enqueue(3)
    print "\n", more_nums, "\n"
    print more_nums.dequeue()
    print "\n", more_nums, "\n"
    print more_nums.is_empty()
    print more_nums.dequeue()
    print more_nums.dequeue()
    print more_nums.is_empty()
