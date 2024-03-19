# Animal class (parent class)
class Animal:
  """
  This class represents a generic animal.
  """
  def __init__(self, name, species):
    self.name = name
    self.species = species

  def make_sound(self):
    print("Generic animal sound")  # Placeholder sound

# Dog class (child class inheriting from Animal)
class Dog(Animal):
  """
  This class represents a dog, inheriting from Animal.
  """
  def __init__(self, name, species, breed):
    super().__init__(name, species)  # Call parent class constructor
    self.breed = breed

  def make_sound(self):
    print("Woof!")  # Specific sound for Dog

# Cat class (child class inheriting from Animal)
class Cat(Animal):
  """
  This class represents a cat, inheriting from Animal.
  """
  def __init__(self, name, species, fur_color):
    super().__init__(name, species)  # Call parent class constructor
    self.fur_color = fur_color

  def make_sound(self):
    print("Meow!")  # Specific sound for Cat

# Create Animal object (not recommended as make_sound is generic)
animal = Animal("Generic", "Unknown")

# Create Dog object
dog = Dog("Buddy", "Canine", "Labrador")

# Create Cat object
cat = Cat("Whiskers", "Feline", "Orange")

# Make animal objects speak (not ideal sound for Animal class)
animal.make_sound()  # Prints "Generic animal sound"
dog.make_sound()    # Prints "Woof!" (Polymorphism in action)
cat.make_sound()    # Prints "Meow!" (Polymorphism in action)

# Accessing attributes
print(f"Dog breed: {dog.breed}")
print(f"Cat fur color: {cat.fur_color}")
