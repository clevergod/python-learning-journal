# -*- coding: utf-8 -*-

class Student(object):
  def __init__(self, name, gender):
    self.name = name
    self.__gender = gender
  
  def get_gender(self):
    return self.__gender

  def set_gender(self, value):
    self.__gender = value

  @property
  def score(self):
    return self._score

  @score.setter
  def score(self, value):
    if not isinstance(value, int):
      raise ValueError('score must be an integer!')
    if value < 0 or value > 100:
      raise ValueError('score must between 0 ~ 100!')
    self._score = value


geeter = Student('Tom', 'boy')
print(geeter.name,'gender: ',geeter.get_gender())
geeter.set_gender('girl')
print(geeter.name,'gender: ',geeter.get_gender())

# 使用 @property
geeter.score = 66
print('score', geeter.score)
