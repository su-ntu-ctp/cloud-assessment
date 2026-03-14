"""
Task 1: Create a Person class with the following attributes:
- name (str)
- age (int)
- hobbies (list)
- socials (dict)
"""
class Person:
  def __init__(self, name, age, hobbies, socials):
    self.name = name
    self.age = age
    self.hobbies = hobbies
    self.socials = socials

"""
Task 2: Create an instance of the Person class with the following attributes: 
- name: Alice
- age: 45
- hobbies: coding, reading
- socials: linkedin -> alice, github -> alice
"""
alice = Person("Alice", 45, ["coding", "reading"], {"github": "alice", "linkedin": "alice"})

"""
Task 3: Create a Car class with the following attributes:
- make (str)
- model (str)
- year (int)
"""
class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

"""
Task 4: Create an instance of the Car class with the following attributes:
- make: Tesla
- model: Model 3
- year: 2022
"""
car = Car("Tesla", "Model 3", 2022)

"""
Task 5: Create a variable named 'solution' and assign it a tuple with the values from Task 2 and Task 4. 
"""
solution = (alice, car)
 
def test_solution_person_attributes():
    pass

def test_solution_car_attributes():
    pass
