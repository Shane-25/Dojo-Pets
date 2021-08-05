# implement __init__( name , type , tricks ):
# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 100
        self.health = 100
    
    def sleep(self):
        self.energy += 25
        print("Pet's Energy after sleep:", self.energy)

    def eat(self):
        self.energy += 5
        self.health += 10
        print("Pet's Health after eating:", self.health,"\n","Pet's Energy after eating:", self.energy)

    def play(self):
        self.health += 5
        print("Pet's Total Health:", self.health)

    def noise(self):
        print(self.noise)

class Dog(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
        self.sound = 'Woof!!!'
    def noise(self):
        print(self.sound)

class Horse(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
        self.sound = 'nay'
    def noise(self):
        print(self.sound)
