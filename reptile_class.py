from animal_class import *

class Reptile(Animal):
    pass

    def make_sound(self):
        return ' not woof'


animal1 = Animal('Nacho',30,'redish')


reptile1 = Reptile('Crocodile',16,'greenish')


print(animal1)
print(reptile1)

print(reptile1.eat())
print(reptile1.potty())
print(reptile1.sleep())
print(reptile1.reproduce())
print(reptile1.make_sound())
print (animal1.make_sound())