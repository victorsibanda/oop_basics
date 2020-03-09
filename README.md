#OOP BASICS

This repo will contain our OOP basics. 

- We will look at: 
 - Abstraction 
 - Encapsulation 
 - Inheritance 
 - Polymorphism 


*Usually you want your apps to Create,Read,Update and Delete

##Methods Vs Functions

Methods are function that belong to a specific data type. 
Where functions are anonymous and anything can call and run them 

##What is a class

- A class is like a cookie cutter that creates instances of cookies 
-  an instance is an occurence of something. 
- Classes will wrap characteristic as attributes, and behaviours as methods

#Characteristics of an object/ how an object looks like
These are attributes that are assigned to each instance.

## Self
- Refers to the instance of on which the method is called 
- self.name = 'ringo'
-This means that the specific object attribute will have the name ringo 

## Abstraction 
- This is when the programmer hides all but the relevant data about an object in order to reduce complexity and improve efficiency.
- Ability to hide complexity
- Done using Seperation of concerns, documentation and inheritance.
  - Specify methods and how to use them, that is Abstraction 

Real life Example:
- Cars
- Microwaves

## Encapsulation
- Each object are privately held inside a defined boundary, or class.
- Other objects do not have access to this class or the authority to make changes unless they reference it directly.
- Encapsulation improves the program’s security and avoids unintended data corruption
- Making methods of attributes private, When methods or attributes are private they can be called by its own functions within a class. 
- **Restricts Access**
- **Making Private**

Example:

This leads to getters and setters!

syntax: 

```Python
class Animal():
    pass
    #define behaviour and characteristics
    #define characteristics of Every Animal
    def __init__(self, name,age,colour) :
        self.name = name
        self.__age = age
        self.hearts = True
        self.colour = colour
        self.brain = True

# double underscore makes it private eg. self.__age = age

```
## Inheritance
 - Developers can reuse common logic while maintaining a unique hierarchy by assigning relationships and subclasses between objects.
 - This forces more thorough data analysis, reduces development time and ensures a high level of accuracy.
 - Ability to pass to child class all the methods and characteristics.
 - You can reuse code - **OOP**

## Polymorphism
-  Objects can take multiple forms depending on the context.
- The program will determine which meaning or usage is necessary for each execution of that object, reducing the need to duplicate code.

- Ability to completely override methods, and if need be recall methods from parent class
using .super()


##.Super()

Represents the parent class, and allows you to call methods and characteristics from parent class. 

Usage and case in point:
- situation where you want to overwrite a method (say method .honk())
- You want to add new functionality to the new method, but you still want everything for the first method

--> then you call super()

Most of the times this is used with the __init__ method 
- You want to add new characteristics to child object and you want to keep original characteristics
- You overwrite the init method and still call  the original init method, with the necessary arguments.

```Python
class Animal():

    def __init__(self,age,colour_fur):
        self.age = age
        self.colour_fur = colour_fur    

```

## Use from Original Class

```Python
class Reptile(Animal):
    pass

#Using same attributes
```

## Overwrite Completely
```Python
class Reptile(Animal):

    def __init__(self,scales,blood_temp):
        self.scales = scales
        self.blood_temp = blood_temp

#Completely Overwritten

```
## Overwrite and Use from Original Class
```Python
class Reptile(Animal):

    def __init__(self,age,colour_fur,scales,blood_temp):
        super().__init__ (age, colour_fur)
        self.scales = scales
        self.blood_temp = blood_temp

#Added Attributes

```





