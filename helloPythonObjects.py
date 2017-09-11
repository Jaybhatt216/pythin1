import random
import sys
import os

# time to learn object oriented programming by learning class and objects
#class is real world objects
# tw0 underscores __ means its private
class Animal:
    __name = ""
    __height =0
    __weight =0
    __sound = 0
    #need to create a function to set the class

    def __init__(self,name,height,weight,sound): #initalze class

        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
# now you need to create setters and getters

    def set_name__(self, name):
        self.__name = name

    def set_height__(self, height):
            self.__height = height

    def set_weight__(self, weight):
        self.__weight = weight

        def set_sound_(self, sound):
            self.__sound = sound

        def get_name(self):
            return self.__name

        def get_height(self):
            return self.__height

        def get_weight(self):
            return self.__weight

        def get_sound(self):
            return self.__sound

        def get_type(self):
            print("Animal")

        def toString(self):
            return "{} is {} cm tall and {} kg and says {}".format(self.__name,
                                                                   self.__height,
                                                                   self.__wieght,
                                                                   self.__sound)

        #class is created now to create object
        cat = Animal('Whiskers',33,10,'Meow')
        print(cat.toString())

        #inheiritance
        class Dog(Animal):
            __owner = ""
            def  __init__(self,name,height,weight,sound,owner):
                self.__owner = owner
                super(Dog, self).__init__(name,height,weight,sound)
                def set_owner(self,owner):
                    self.__owner = owner
                def get__owner(self):
                    return self.__owner
                def get_type(self):
                    print("Dog")

                    def toString(self):
                        return "{} is {} cm tall and {} kg and says {} His owner is {}".format(self.__name,
                                                                               self.__height,
                                                                               self.__wieght,
                                                                               self.__sound,
                                                                               self.__owner)

                    #method overloading

                    def multiple_sounds(self, how_Many=None):
                        if how_Many is None:
                            print(self.get_sound())
                        else:
                            print(self.get_sound() * how_Many)

                            spot = Dog("spot", 53,27,"ruff","Jay")

                         print(spot.toString())

                        #polymorphism

                        class AnimalTesting
                            def get_type(selfself, animal):
                                animal.get_type()

                                test_animal = AnimalTesting()

                                test_animal.get_type(cat)
                                test_animal.get_type(spot)

                                spot.multiple_sounds(4)
                                spot.multiple_sound()
