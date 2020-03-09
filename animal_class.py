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
    def __init__(self, name,age_days,colour) :
        self.name = name
        self.__age_days = age_days
        self.hearts = True
        self.colour = colour
        self.brain = True

    # age
    #we should be able to print or retrieve the age.
    #We should not be able to change/alter the age (user cannot set their own age) without admin access
    #As animal sleeps it should increment the age.
    #first lets make the age private
    #Create method that gets age and returns it
    #Change sleep method to implement age
    def get_age(self):  #getter method
        return self.__age_days




    def set_age(self,age_days):
        self.__age_days = age_days   #Setter Method

        # fake verification
        password = input('what is the password')

        if password == 'SuperSecret\n':
            self.__age_days = age_days
            return  True
        else:
            return False

    def __increment_age(self):
        self.__age_days += 1


    def eat (self):
        #when animal eats age should be incremented __increment_age() method
        return "nom, nom, nom"

    def sleep(self):
        self.__increment_age()
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
ringo = Animal('Ringo', 200 , 'green')
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


print(ringo.get_age())
print(ringo.set_age(500))
ringo.sleep()
print(ringo.get_age())

