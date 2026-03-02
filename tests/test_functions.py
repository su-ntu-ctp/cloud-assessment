from exercises.functions import add, average, hello, yes_or_no

def test_average():
  assert average([1, 2, 3]) == 2, "Should return 2 as the average."
  assert average([1, 2, 3, 4, 5]) == 3, "Should return 3 as the average."

def test_add():
  assert add(1, 2) == 3, "Should return 3."
  assert add(8, 2) == 10, "Should return 10."
  assert add(-3, -5) == -8, "Should return -8."

def test_hello():
  assert hello("Alice") == "Hello, Alice!", "Should return 'Hello, Alice!'"
  
def test_yes_or_no():
  assert yes_or_no(True) == "yes", "Should return 'yes'"
  assert yes_or_no(False) == "no", "Should return 'no'"
