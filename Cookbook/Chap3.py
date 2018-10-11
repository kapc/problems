#!/usr/env/python

with open("/etc/passwd") as f:
    try:
        while True:
            line = next(f, None)
            if line is None:
                break
    except StopIteration as e:
        print("I am here")

items = [1,2,3]
it = iter(items)

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def add_children(self, child):
        self._children.append(child)

    def __repr__(self):
        return "Node{!r}".format(self._value)

    def __iter__(self):
        return iter(self._children)

n = Node(0)
n.add_children(1)
n.add_children(2)
n.add_children(3)

for i in n:
    print(i)

def frange(start, stop, increment):
    while start < stop:
        yield start
        start += increment

for f in frange(0, 4, 0.25):
    print(f)

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def add_child(self, child):
        self._children.append(child)

    def __repr__(self):
        return "Node({!r})".format(self._value)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))

print(list(root))
print(list(root.depth_first()))

a = [1,2,3,4,5,6,7]


f = open("/etc/passwd")

from collections import deque

class linehistory:
    def __init__(self, lines, hist_len=30):
        self._lines = lines
        self._history = deque(maxlen=hist_len)

    def __iter__(self):
        for lineno, line in enumerate(self._lines,1):
            self._history.append((lineno, line))
            yield line

    def clear(self):
        self._history.clear()

f = open("/etc/passwd")
l = linehistory(f)


# Taking a slice out of an iterator.

def count(n):
    i = 0
    while i < n:
        yield i
        i += 1

c = count(30)
import itertools

c = itertools.islice(c, 10, 20)

for i in c:
    print(i)

# Drop few items from the iterator either from the start or end.

from itertools import dropwhile

with open("/etc/passwd") as f:
    for line in dropwhile(lambda line: line.startswith("_a"), f):
        print(line)

from itertools import islice
items = [1, 2, 3, 4, 5]

for x in itertools.islice(items, 3, None):
    print(x)

p = lambda x: x
print(p(1000))

# Print all permutations and combinations of all the items.

from itertools import permutations, combinations
items = [1,2,3,4,5,6,7,8]
for x in permutations(items, 8):
    print(x)

for x in combinations(items, 3):
    print(x)

# Print index and value both for any sequence.

my_list = [1, 2, 3, 4, 5]
for idx, val in enumerate(my_list):
    print("{} {}".format(idx, val))

from collections import defaultdict

word_dict = defaultdict(list)

lines = []
with open("/etc/passwd") as f:
    lines = f.readlines()

for index, line in enumerate(lines):
    words = [word for word in line.split(" ")]
    for word in words:
        word_dict[word].append(index)
print(word_dict)

d = [(1,2), (3,4), (5,6), (7,8)]

for index, (x, y) in enumerate(d):
    print(index, x, y)

# Use both iterators simulatenously.

xpts = [1,2,3,4,5,6]
ypts = [6,5,4,]

l = list(zip(xpts, ypts))
print(l)

from itertools import zip_longest
l = list(zip_longest(xpts, ypts))
print(l)

d = dict(zip_longest(xpts, ypts))
print(d)

# Work with seperate containers as one.

a = [1,2,3,4,5]
d = {1 : 2, 2: 3, 4: 5}

from itertools import chain
for x in chain(a, d):
    print(x)


# Creating data processing pipelines:

import os
import re
import gzip
import bz2
import fnmatch
from collections import Iterable


def flatten(items, ignore_type=(str, bytes)):
    for it in items:
        if isinstance(it, Iterable) and not isinstance(it, ignore_type):
            yield from flatten(it)
        else:
            yield it

a = [[1,2,3], [1,2], "chnadres"]

for i in flatten(a):
    print(i)

import heapq
a = [1, 12,4, 9]
b = [2,3,6,7]
c = heapq.merge(a, b)

for i in c:
    print(i)

CHUNKSIZE=10
def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)

def reader(s):
    for data in iter(lambda: f.read(), b''):
        n = sys.stdout.write(chunk)


