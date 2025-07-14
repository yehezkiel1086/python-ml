#!/bin/python3

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self): # polymorphism
    return f"Person: {self.name}, {self.age}"

class Student(Person):
  def __init__(self, name, age, gpa):
    super().__init__(name, age)
    self.gpa = gpa

  def __str__(self): # polymorphism
    return f"Student: {self.name}, {self.age}, {self.gpa}"
  
ben = Student("Ben", 24, 3.4)

print(ben)
