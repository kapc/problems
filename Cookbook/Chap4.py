#! /usr/env/python

lines = ""
with open("/etc/passwd", "rt") as f:
    lines = f.readlines()
    print(lines)

with open("/tmp/somefile.txt", "wt") as f:
    print("Chandersh", file=f)

print(1,3,3, sep="wtf", end="hell!")

a = (1,2,3)
print(*a, sep="-")

with open("/tmp/chandresh", "wt") as f:
    f.write("Chandresh")


import io

s = io.StringIO()
s.write("chandresh ")
s.write("palak")

print(s.getvalue())

import os

file_name = "/etc/passwd"

print(os.path.basename(file_name))
print(os.path.dirname(file_name))

print(os.path.join("/etc", "passwd"))
print(os.path.splitext(file_name))

print(os.path.isfile(file_name))
print(os.path.isdir(file_name))
print(os.path.islink(file_name))
print(os.path.realpath(file_name))
print(os.path.getsize(file_name))
print(os.path.getctime(file_name))

d = os.listdir("/etc")
for i in d:
    print(i)

import glob
print(glob.glob("/etc/passwd"))


import sys
sys.stdout.buffer.write(b'chandresh')


fd = os.open("/tmp/chandresh", os.O_WRONLY | os.O_CREAT)

f = open(fd, "wt")
f.write("chandresh")
f.close()

from tempfile import TemporaryFile

f = TemporaryFile("w+t")
f.write("chanresh")
f.close()

import tempfile
tempfile.gettempdir()

print(tempfile.mkdtemp())

class Chandresh:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

import pickle
d = Chandresh('chandresh', 23)
f = open("/tmp/chandresh", "wb")
pickle.dump(d, f)

print(pickle.dumps(d))
f.close()

f = open("/tmp/chandresh", "rb")
d = pickle.load(f)
print(d.get_name())

import time
import threading

class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while True:
            print("T-Minus", self.n)
            self.n += 1

    def __getstate__(self):
        return self.n

    def __setstate__(self, state):
        self.__init__(state)

c = Countdown(30)

f = open("/tmp/c", "wb")
pickle.dump(c, f)
f.close()

f = open("/tmp/c", "rb")
c = pickle.load(f)
print(c.n)
