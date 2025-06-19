class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def return_name(self):
    return f"Name: {self.name}, Age: {self.age}"

person = Person.return_name("Alice", 30)

print(person)  # Output: Name: Alice, Age: 30