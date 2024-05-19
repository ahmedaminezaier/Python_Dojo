from Ninja import Ninja
from Pet import Dog, Cat

# Create instances of pets
my_dog = Dog("rocky", ["fetch", "roll over"])
my_cat = Cat("Tom", ["jump", "purr"])

# Create a Ninja instance and assign the dog
Ninja_with_Dog = Ninja("Sasuke", "Uchimaro", "Yuki", "dog food", my_dog)

# Create a Ninja instance and assign the cat
Ninja_with_Cat = Ninja("Son", "Goku", "fish", "cat food", my_cat)

# Have the Ninjas interact with their pets
Ninja_with_Dog.feed()
Ninja_with_Dog.walk()
Ninja_with_Dog.bathe()

Ninja_with_Cat.feed()
Ninja_with_Cat.walk()
Ninja_with_Cat.bathe()