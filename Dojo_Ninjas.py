# implement __init__( first_name , last_name , treats , pet_food , pet )


# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method

from Dojo_Pets import Pet, Dog, Horse

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
    
    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.noise()

blair = Dog('blair', 'dog', 'sit')
john = Ninja('John', 'Smith', 'kibble', 'Pedigree', blair)

john.feed()
john.walk()
john.bathe()
