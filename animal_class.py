'''
define our animal class

sudo
Looks / characteristics of every animal
   name, age,colour heart and brain

behavious / methods of every animal

  eat, sleep, reproduce, potty , makesound
  '''

class Animal():
    pass
    #define behaviour and characteristics
    #define characteristics of Every Animal
    def __init__(self, name,age,colour) :
        self.name = name
        self.age = age
        self.hearts = True
        self.colour = colour
        self.brain = True



    def eat (self):
        return "nom, nom, nom"

    def sleep(self):
        return 'zzzzzZZZZZZzzzz'

    def reproduce(self):
        return 'I need some privacy'

    def potty(self):
        return 'hmmmm'

    def make_sound(self):
        return 'woof'

# #Creates instance of animal
#
#
# ringo = Animal('Ringo', 200 , 'green')
#
# print(ringo.brain)
# print(ringo.eat())
# print(ringo.potty())
# print(ringo.sleep())
#
# #Second animal
#
# mini = Animal('Stacy',45,'blue')
# print(mini.name, mini.age)



