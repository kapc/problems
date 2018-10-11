#! /usr/env/python

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

example = [1,2,3,4,5,4,4,4]
result = dedupe(example)
for val in result:
    print(val)


def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
a = [{'x' : 1, 'y' : 2}, {'x' : 2, 'y' : 3}, {'x' : 1, 'y' : 2}]
z = list(dedupe2(a, key=lambda d: (d['x'], d['y'])))
print(z)
