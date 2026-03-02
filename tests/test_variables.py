from exercises.variables import age, name, hobbies, socials

# DO NOT MODIFY THIS FILE

def test_variable_age():
  assert age > -1 and isinstance(age, int), "The age variable should be a positive integer."

def test_variable_name():
  assert name and isinstance(name, str), "The name variable should be a non-empty string."

def test_variable_hobbies():
  assert hobbies and isinstance(hobbies, list), "The hobbies variable should be a non-empty list."

def test_variable_socials():
  assert socials and isinstance(socials, dict), "The social variable should be a non-empty dictionary."