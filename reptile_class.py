from animal_class import *


class Reptile(Animal):
    pass

    def __init__(self,name,age,colour,scales,blood_temp):
        super().__init__ (name, age, colour)
        self.scales = scales
        self.blood_temp = blood_temp


    def make_sound(self):
        return ' not woof'



animal1 = Animal('Nacho',30,'redish')


reptile1 = Reptile('Crocodile',16,'greenish','lots','very cold')


print(animal1)
print(reptile1)

print(reptile1.eat())
print(reptile1.potty())
print(reptile1.sleep())
print(reptile1.reproduce())
print(reptile1.make_sound())
print (reptile1.blood_temp())










# for n in range(100):
#     print ("Fizz"*(not n % 3) + "Buzz"*(not n % 5) or n)