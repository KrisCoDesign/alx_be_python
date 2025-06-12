class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        return name, age

person1 = Person("Alice", 30)
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30