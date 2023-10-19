class Animal:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"Animal {self.name}"

class Dog(Animal):
  def __repr__(self):
    return f"Dog: {self.name}"

class Fish(Animal):
  def __repr__(self):
    return f"Fish: {self.name}"

class PetOwner:
    def __init__(self, name, *animals):
       self.name = name
       self.animals = list(animals)
    
    def add_animals(self, *animals):
       self.animals.extend(animals)
    
    def __str__(self):
      owned_animals = ", ".join(str(animal) for animal in self.animals)
      return f"Owner: {self.name}, Animals: {owned_animals}"

owner1 = PetOwner("Ada, owns:", ["Snoopy", "Pluto"], ["Fishy", "Buppy"])
owner2 = PetOwner("Beda, owns:", ["Barkly"] )

print(owner1)
print(owner2)


# Ada owns:
# [Dog: Snoopy, Dog: Pluto]
# [Fish: Fishy, Fish: Buppy]
# Beda owns:
# [Dog: Barkly]