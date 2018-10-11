#! /usr/env/python


import csv
from collections import namedtuple


from urllib.request import urlopen
from xml.etree.ElementTree import  parse


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))

    next(doc)

    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield item
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass

from xml.etree.ElementTree import Element

def dict_to_xml(tag, d):
    elem = Element(tag)
    for key,value in d.items():
        child = Element(key)
        child.text = str(value)
        elem.append(child)
    return elem

d = {'price' : 200, 'life' : 'death'}
result = dict_to_xml('stock', d)
print(result)

from xml.etree.ElementTree import tostring
print(tostring(result))


class XMLNamespaces:
    def __init__(self, **kwargs):
        self.name_spaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)

    def register(self, name, uri):
        self.name_spaces[name] = '{'+uri+'}'

    def __call__(self, path):
        print("chandresh")
        print(path.format_map(self.name_spaces))



ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
ns('content/{html}html')

stocks = [
    ('GOOG', 100, 490.1),
    ('APPL', 111, 4890),
    ('FB', 1332, 1223)
]

import sqlite3

db = sqlite3.connect('database.db')
c = db.cursor()
c.execute('create table portfolio1 (symbol text, shares integer, price real)')
db.commit()

c.executemany('insert into portfolio1 values (?, ?, ?)', stocks)
db.commit()

for row in db.execute('select * from portfolio1'):
    print(row)










