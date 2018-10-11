#! /usr/env/python

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '{0.x!s}, {0.y!s}'.format(self)

p = Pair(10, 0.21)
print(p)
p

_formats = {
    'ymd' : '{d.year} - {d.month} - {d.day}',
    'mdy' : '{d.month} - {d.day} - {d.year}',
    'dmy' : '{d.day} - {d.month} - {d.year}'
}

class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def __format__(self, format_spec):
        if format_spec is None:
            format_spec = 'ymd'
        fmt = _formats[format_spec]
        return fmt.format(d=self)

d = Date('12', '12', '2020')
print("{:ymd}".format(d))

from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError("Already selfected.")
        self.sock = socket(self.family, self.type)
        self.sock.selfect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None


from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.conections = []

    def __enter__(self):
        s = socket(self.family, self.type)
        s.selfect(self.address)
        self.conections.append(s)
        return s

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.selfections.pop().close()

class Date:
    __slots__ = ['year', 'day', 'month']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return '{d.year}-{d.month}-{d.day}'.format(d=self)

d = Date(2012, 12, 12)
print(hasattr(d, 'year'))
setattr(d, 'year', 'chandrseh')
print(d)

class B:
    def __init__(self):
        self.__private_value = 10

    def __private_method(self):
        print("B's private method")

    def _override_b_method(self):
        print("C' private method")

class C(B):
    def __init__(self):
        super().__init__()
        self.__private_value = 11

    def __private_method(self):
        print("C' private method")

    def _override_b_method(self):
        print("B's method got overriddent by me.")

c = C()

class Structure:
    _fields = []
    def __init__(self, *args):
        if len(args) < len(self._fields):
            raise Exception("Expected more args")

        self.__dict__.update(zip(self._fields, args))

class A(Structure):
    _fields = ['name', 'size']

a = A('chandresh', 10)
print(a.name)
print(a.size)


def init_from_locals(self):
    import sys
    locs = sys._getframe(1).f_locals
    for k, v in locs.items():
        if k != self:
            setattr(self, k, v)

class B:
    def __init__(self, name, size):
        init_from_locals(self)

b = B('chandresh', 10)
print(b.size)


# Create abstract base classes.

from abc import ABC, ABCMeta, abstractmethod

class ISocket(metaclass=ABCMeta):
    def __init__(self):
        pass
    @abstractmethod
    def readsfds(self):
        pass

    @abstractmethod
    def send(self, size):
        pass

import io

ISocket.register(io.IOBase)

f = open("foo.txt", "w")
isinstance(f, ISocket)

from abc import ABCMeta, ABC

class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        self.name = value

    @name.getter
    @abstractmethod
    def name(self):
        return self.name

    @classmethod
    @abstractmethod
    def whatever(self):
        pass

    @staticmethod
    @abstractmethod
    def aila():
        pass

import collections

class A(collections.Iterable):
    def __init__(self):
        pass

import collections
import bisect

class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial else []

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def add(self, item):
        bisect.insort(self._items, item)

items = SortedItems([4,1,2])
print(list(items))

for item in items:
    print(item)

# Delegate attribute access

class A:
    def spam(self, x):
        print("Class A spams")

    def foo(self, y):
        print("FooA")

class B:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        return self._a.spam(x)

    def foo(self, y):
        return self._a.foo(y)

    def bar(self):
        pass

class C:
    def __init__(self):
        self._a = A()

    def bar(self):
        print("B Bar")

    def __getattr__(self, item):
        return getattr(self._a, item)

c = C()
c.foo(12)
c.bar()

# Create a proxy class

class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        print("getattr:", name)
        return getattr(self._obj, name)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            super().__setattr__(key, value)
        else:
            setattr(self._obj, key, value)

    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            delattr(self._obj, name)

a = A()
p = Proxy(a)

p.spam(1)
p.foo(1)

class A:
    def spam(self):
        print("A.spam")

    def foo(self):
        print("A.foo")

class B(A):
    def spam(self):
        print("B.spam")
        super().spam()

    def foo(self):
        print("B.foo")

class C:
    def __init__(self):
        self._a = A()

    def spam(self):
        self._a.spam()

    def foo(self):
        print("C.foo")
c = C()
c.spam()
c.foo()

b = B()
b.spam()

class ListLike:
    def __init__(self):
        self._items = []

    def __getattr__(self, name):
        return getattr(self._items, name)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, key, value):
        self._items[key] = value


    def __len__(self):
        return len(self._items)

l = ListLike()
l.insert(0, 1)
l.append([2,3,4,5])
print(l._items)
print(l[0], len(l))
l[0] = 12
print(l._items)


# Define more than one constructors in the class.
import time
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "{}/{}/{}".format(self.month, self.day, self.year)

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


d = Date(12, 12, 12)
print(d)
d = Date.today()
print(d)

class Newdate(Date):
    pass

n = Newdate.today()
print(n)

class DateVar:
    def __init__(self, *args):
        if len(args) == 0:
            t = time.localtime()
            args = (t.tm_year, t.tm_mon, t.tm_mday)
        self.year, self.month, self.day = args

d = DateVar(2012, 12, 21)
d1 = DateVar()

print(d)
print(d1)


# Create an instance without invoking init
d = Date.__new__(Date)
t = time.localtime()
setattr(d, 'year', 12)
setattr(d, 'month', 12)
setattr(d, 'day', 12)
print(d)

# Mixin classes.

class Logged:
    __slots__ = ()

    def __getitem__(self, item):
        print("Getting item.")
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        print("Setting item")
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print("Deleting item")
        return super().__delitem__(key)

class SetOneMappingMixin:
    __slots__ = ()
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + 'already set')
        super().__setitem__(key, value)

class LoggedSetOneDict(Logged, SetOneMappingMixin, dict):
    pass

ld = LoggedSetOneDict()
ld['x'] = 12
ld['y'] = 13


class LoggedDict(Logged, dict):
    pass

d = LoggedDict()
d['x'] = 12
print(d['x'])

def LoggedMapping(cls):
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self, key):
        print("Getting")
        return cls_getitem(self, key)

    def __setitem__(self, key, value):
        print("Setting")
        return cls_setitem(self, key, value)

    def __delitem__(self, key):
        print("Deleting")
        return cls_delitem(self, key)
    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__

    return cls

@LoggedMapping
class LoggedDict(dict):
    pass

l = LoggedDict()
l['x'] = 12
print(l['x'])

# Implement a stateful objects or state machines.

class Connection:
    def __init__(self):
        self.state = 'CLOSED'

    def read(self):
        if self.state != 'OPEN':
            raise RuntimeError('Non Open')
        print('reading')

    def write(self):
        if self.state != 'OPEN':
            raise RuntimeError('Not Open')
        print('writing')

    def open(self):
        if self.state == 'OPEN':
            raise RuntimeError('Already open')
        self.state = 'OPEN'

    def close(self):
        if self.state == 'CLOSED':
            raise RuntimeError('Already closed')
        self.state = 'CLOSED'

class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, newstate):
        self.__class__ = newstate

    def read(self):
        raise NotImplementedError()

    def write(self, data):
        raise NotImplementedError()

    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

class ConnectionState:
    @staticmethod
    def read(self):
        raise NotImplementedError()

    @staticmethod
    def write(self, data):
        raise NotImplementedError()

    @staticmethod
    def open(self):
        raise NotImplementedError()

    @staticmethod
    def close(self):
        raise NotImplementedError()

class ClosedConnectionState(Connection):
    def read(self):
        raise NotImplementedError()

    def write(self, data):
        raise NotImplementedError()

    def open(self):
        self.new_state(OpenConnectionState)

    def close(self):
        raise NotImplementedError()

class OpenConnectionState(Connection):
    def read(self):
        raise NotImplementedError()

    def write(self, data):
        raise NotImplementedError()

    def open(self):
        raise NotImplementedError()

    def close(self):
        self.new_state(ClosedConnectionState)


c = Connection()
c.open()
print(c)
c.close()
print(c)

# Calling a method of an object give the name as string.

import math
import operator
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:}, {!r})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)

p = Point(2, 3)
d = getattr(p, 'distance')(0, 0)
d = operator.methodcaller('distance', 0, 0)(p)
print(d)

# Implementing visitor pattern.

class Node:
    pass

class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand

class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOperator):
    pass

class Sub(BinaryOperator):
    pass

class Mul(BinaryOperator):
    pass

class Div(BinaryOperator):
    pass

class Negate(UnaryOperator):
    pass

class Number(Node):
    def __init__(self, value):
        self.value = value

# 1 + 2 * (3 - 4) / 5
t1 = Sub(Number(3), Number(4))
t2 = Mul(Number(2), t1)
t3 = Div(t2, Number(5))
t4 = Add(Number(1), t3)
t5 = Negate(t4)

class NodeVisitor:
    def visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name___))


class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)

    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)

    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)

    def visit_Negate(self, node):
        return -node.operand

e = Evaluator()


class StackNode(NodeVisitor):
    def generate_code(self, node):
        self.instructions = []
        self.visit(node)
        return self.instructions

    def visit_Number(self, node):
        self.instructions.append(('PUSH', node.value))

    def binop(self, node, instruction):
        self.visit(node.left)
        self.visit(node.right)
        self.instructions.append((instruction,))

    def visit_Add(self, node):
        self.binop(node, 'ADD')

    def visit_Sub(self, node):
        self.binop(node, 'SUB')

    def visit_Mul(self, node):
        self.binop(node, 'MUL')

    def visit_Div(self, node):
        self.binop(node, 'DIV')

    def unaryop(self, node, instruction):
        self.visit(node.operand)
        self.instructions.append((instruction, ))

    def visit_Negate(self, node):
        self.unaryop(node, 'NEG')

s = StackNode()
print(s.generate_code(t4))


def get_result():
    y = yield [x for x in [1] * 10]
    print(y)


# Managing memory in cyclic data structures.

import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __del__(self):
        print("Deleted..")

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    @property
    def parent(self):
        return None if self._parent is None else self._parent

    @parent.setter
    def parent(self, node):
        self._parent = node

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

root = Node("parent")
c1 = Node("child")

class Data:
    def __del__(self):
        print("Data.__del__")


class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    def add_child(self, node):
        self.children.append(node)
        node.parent = self

a = Node()
a.add_child(Node())
del a






















