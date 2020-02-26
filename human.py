import random

class Human(object):
	hunger = 0
    gender = False

	def __init__():
		gender = genders.get(random.randint(1, 2))

        if gender:
            name = namesMen.get(random.randint(1, 5))

        else:
            name = namesWomen.get(random.randint(1, 5))

	def cycle():
		hunger += 1

namesMen = {1: 'Adam', 2: 'Malahiya', 3: 'Aron', 4: 'Gennadiy', 5: 'Ilya'}

namesWomen = {1: 'Polikseniya', 
              2: 'Magdalina', 
              3: 'Vladimira', 
              4: 'Lyubov', 
              5: 'Tamara'}

genders = {1: True, 2: False}