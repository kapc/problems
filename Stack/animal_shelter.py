#! /usr/env/python

"""
Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linked List data structure.
Hints: #22, #56, #63
"""

class Dog:
    def __init__(self, name):
        self.name = name

class Cat:
    def __init__(self, name):
        self.name = name

class AnimalShelter:
    def __init__(self, size):
        self._dog_queue = []
        self._cat_queue = []

    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self._dog_queue.append(animal)
        elif isinstance(animal, Cat):
            self._cat_queue.append(animal)

    def dequeueany(self):
        if self._dog_queue:
            oldest_dog = self._dog_queue[0]
        if self._cat_queue:
            oldest_cat = self._cat_queue[0]


        oldest_cat = self._cat_queue[0]