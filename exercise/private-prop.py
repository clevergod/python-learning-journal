class Student(object):
  def __init__(self, name, gender):
    self.name = name
    self.__gender = gender
  
  def get_gender(self):
    return self.__gender

  def set_gender(self, value):
    self.__gender = value

geeter = Student('Tom', 'boy')
print(geeter.name,'gender: ',geeter.get_gender())
geeter.set_gender('girl')
print(geeter.name,'gender: ',geeter.get_gender())