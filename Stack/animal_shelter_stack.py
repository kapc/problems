import time
"""
Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linked List data structure.
Hints: #22, #56, #63

Questions:
    1. While enqueing do we know if we are enqueuing dogs or cats.
    2.

"""
DOG = 1
CAT = 2

class Animal(object):
    """
    """
    def __init__(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        self._name = name
    def __str__(self):
        return self._name

class Cat(Animal):
    def __init__(self, name):
        self._name = name
    def __str__(self):
        return self._name

class Node(object):
    def __init__(self, animal):
        self._animal = animal
        self._time_stamp = time.time()

    def __cmp__(self, other):
        if self._time_stamp < other._time_stamp:
            return True
        return False

    def get_animal(self):
        return self._animal

class AnimalShelter(object):
    """
    Animal shelter object.
    """
    def __init__(self, total_size):
        """

        :param total_size:
        """
        self._dogs = []
        self._cats = []
        self._max_size = total_size
        self._cur_oldest = None

    def enqueue(self, animal):
        node = Node(animal)
        if isinstance(animal, Dog):
            self._dogs.append(node)
        elif isinstance(animal, Cat):
            self._cats.append(node)

    def enqueue_cat(self, animal):
        node = Node(animal)
        self._cats.append(node)

    def enqueue_dog(self, animal):
        node = Node(animal)
        self._dogs.append(node)

    def dequeue_dog(self):
        if self._dogs:
            return self._dogs.pop(0).get_animal()
        return None

    def dequeue_cat(self):
        if self._cats:
            return self._cats.pop(0).get_animal()
        return None

    def dequeue(self):
        node1 = None
        node2 = None
        if self._dogs:
            node1 = self._dogs[0]
        if self._cats:
            node2 = self._cats[0]
        if not node1 and not node2:
            return None
        elif not node1:
            self._cats.pop(0)
            return node2.get_animal()
        elif not node2:
            self._dogs.pop(0)
            return node1.get_animal()
        else:
            if node1._time_stamp < node2._time_stamp:
                return self._dogs.pop(0).get_animal()
            else:
                return self._cats.pop(0).get_animal()

if __name__ == "__main__":
    shelter = AnimalShelter(100)
    shelter.enqueue(Dog("tommy"))
    shelter.enqueue(Cat("Catty"))
    shelter.enqueue(Dog("Chandu"))
    shelter.enqueue(Dog("Landur"))
    shelter.enqueue(Dog("Fitur"))
    shelter.enqueue(Cat("Cattu"))

    print shelter.dequeue_cat()
    print shelter.dequeue_dog()
    print shelter.dequeue()
    print shelter.dequeue_cat()
    print shelter.dequeue()
    print shelter.dequeue()
    print shelter.dequeue()

