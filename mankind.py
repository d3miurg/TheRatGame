import random

humans = []

class Human(object):
    hunger = 0
    gender = False

    def __init__(self):
        self.gender = genders.get(random.randint(1, 2))
        
        if self.gender:
            self.name = namesMen.get(random.randint(1, 5))

        else:
            self.name = namesWomen.get(random.randint(1, 5))

        self.lifetime = 0

        humans.append(self)

    def __repr__(self):
        return self.name

    def lifeCycle(self):
        self.hunger += 1
        self.lifetime += 1

namesMen = {1: 'Adam', 2: 'Malahiya', 3: 'Aron', 4: 'Gennadiy', 5: 'Ilya'}

namesWomen = {1: 'Polikseniya', 
              2: 'Magdalina', 
              3: 'Vladimira', 
              4: 'Lyubov', 
              5: 'Tamara'}

genders = {1: True, 2: False}
