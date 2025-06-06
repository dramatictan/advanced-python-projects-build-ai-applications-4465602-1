# Introduction to Object-Oriented Programming with Python: Creating and Using Classes

# Class Definition
class Car: 
  # Constructor (Initialization) - __init__ method
  def __init__(self, make, model):
    self.make = make # similar to Java class constructor
    self.model = model 

  # Method - start_engine
  def start_engine(self):
    print(f"The {self.make} {self.model}'s engine is running!")

# Creating instances (objects) of the Car class
# Inheritance: Car is a class that can be used to create objects (instances).
car1 = Car("Toyota", "Camry")  # Creating the first car (object)
car2 = Car("Ford", "Mustang")  # Creating the second car (object)

print(f"I have a {car1.make} {car1.model}.")
print(f"I also own a {car2.make} {car2.model}.")

# Abstraction: We create objects without worrying about the internal details of the Car class.
# Polymorphism: Different objects (car1 and car2) can perform the same action (start_engine).
# Method Overriding: The start_engine method can be customised into subclasses
car1.start_engine() 
car2.start_engine()