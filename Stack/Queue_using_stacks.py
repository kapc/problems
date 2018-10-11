#! /usr/env/python

class StackFullException(Exception):
    pass
class StackEmptyException(Exception):
    pass

class QueueFullException(Exception):
    pass

class QueueEmptyException(Exception):
    pass

class Stack:
    def __init__(self, size):
        self._size = size
        self._elems = []

    def push(self, elem):
        if self.is_full():
            raise StackFullException("Stack is full.")
        self._elems.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackEmptyException("Stack is empty.")
        return self._elems.pop()

    def is_empty(self):
        return len(self._elems) == 0

    def is_full(self):
        return len(self._elems) >= self._size

    def __repr__(self):
        return "{}".format(self._elems)

class Queue:
    def __init__(self, size):
        self._stack_enqueue = Stack(size)
        self._stack_dequeue = Stack(size)

    def _rebalance_if_needed(self, source, target):
        while not source.is_empty():
            target.push(source.pop())

    def enqueue(self, elem):
        if self._stack_enqueue.is_empty():
            if not self._stack_dequeue.is_empty():
                self._rebalance(self._stack_dequeue, self._stack_enqueue)
        if self._stack_enqueue.is_full():
            raise QueueFullException()
        self._stack_enqueue.push(elem)

    def dequeue(self):
        if self._stack_dequeue.is_empty():
            if not self._stack_enqueue.is_empty():
                self._rebalance(self._stack_enqueue, self._stack_dequeue)
        if self._stack_dequeue.is_empty():
            raise QueueEmptyException()
        return self._stack_dequeue.pop()



q = Queue(50)

for i in range(0, 20):
    q.enqueue(i)

for j in range(0, 10):
    print(q.dequeue())

for k in range(21, 31):
    q.enqueue(k)

for l in range(0, 20):
    print(q.dequeue())
