# -*- coding: utf-8 -*-
class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"Собака по кличке {self.name.title()} садится!")

    def roll_over(self):
        print(f"Собака по кличке {self.name.title()} перекатывается!")