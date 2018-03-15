#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'clevergod'

class Animal(object):
  def run(self):
    print('animal is runing...')

class Dog(Animal):
  def run(self):
    print('Dog is runing...')
  
class Cat(Animal):
  def run(self):
    print('Cat is runing...')

animal = Animal()
animal.run()
dog = Dog()
dog.run()
cat = Cat()
cat.run()

def run_twice(animal):
  animal.run()
  animal.run()

run_twice(animal)
run_twice(dog)
run_twice(cat)

print('animal, Animal', isinstance(animal, Animal))
print('dog, Dog', isinstance(dog, Dog))
print('cat, Cat', isinstance(cat, Cat))
print('dog, Animal', isinstance(dog, Animal))
print('cat, Animal', isinstance(cat, Animal))
print('dog, Cat', isinstance(dog, Cat))
print('cat, Dog', isinstance(cat, Dog))

print(type(animal))
print(type(dog))
print(type(cat))

print(type(123))
print(type(type(123)))
