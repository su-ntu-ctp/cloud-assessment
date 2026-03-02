import pytest
from exercises.classes import Person, Car, solution

# DO NOT MODIFY THIS FILE

class TestPersonClass:
  
  @pytest.fixture(autouse=True)
  def setup(self):
    self.alice = Person(
      name="Alice",
      age=45, 
      hobbies=["coding"],
      socials={"github": "alice"}
    )
  
  def test_person_class(self):
    assert Person, "The Person class should be defined."

  def test_person_attribute_name(self):
    alice = self.alice
    assert hasattr(alice, "name"), "The person should have a name attribute."
    assert isinstance(alice.name, str), "The name attribute should be a string."
    assert alice.name == "Alice", "The name attribute should be 'Alice'."

  def test_person_attribute_age(self):
    alice = self.alice
    assert hasattr(alice, "age"), "The person should have an age attribute."
    assert isinstance(alice.age, int), "The age attribute should be an integer."
    assert alice.age == 45, "The age attribute should be 45."

  def test_person_attribute_hobbies(self):
    alice = self.alice    
    assert hasattr(alice, "hobbies"), "The person should have a hobbies attribute."
    assert isinstance(alice.hobbies, list), "The hobbies attribute should be a list."
    assert alice.hobbies == ["coding"], "The hobbies attribute should be ['coding']."
    
  def test_person_attribute_socials(self):
    alice = self.alice    
    assert hasattr(alice, "socials"), "The person should have a socials attribute."
    assert isinstance(alice.socials, dict), "The socials attribute should be a dictionary."
    assert alice.socials == {"github": "alice"}, "The socials attribute should be {'github': 'alice'}."

class TestCarClass:
  
  @pytest.fixture(autouse=True)
  def setup(self):
    self.car = Car(
      make="Tesla",
      model="Model 3",
      year=2022
    )
  
  def test_car_class(self):
    assert Car, "The Car class should be defined."
  
  def test_car_attribute_make(self):
    car = self.car
    assert hasattr(car, "make"), "The car should have a make attribute."
    assert isinstance(car.make, str), "The make attribute should be a string."
    assert car.make == "Tesla", "The make attribute should be 'Tesla'."

  def test_car_attribute_model(self):
    car = self.car
    assert hasattr(car, "model"), "The car should have a model attribute."
    assert isinstance(car.model, str), "The model attribute should be a string."
    assert car.model == "Model 3", "The model attribute should be 'Model 3'."

  def test_car_attribute_year(self):
    car = self.car
    assert hasattr(car, "year"), "The car should have a year attribute."
    assert isinstance(car.year, int), "The year attribute should be an integer."
    assert car.year == 2022, "The year attribute should be 2022."

class TestSolution:
  def test_solution(self):
    assert solution, "It should be defined."
    assert isinstance(solution, tuple), "It should be a tuple."
    assert len(solution) == 2, "It should have 2 elements."
    assert isinstance(solution[0], Person), "It should be an instance of the Person class."
    assert isinstance(solution[1], Car), "It should be an instance of the Car class."
