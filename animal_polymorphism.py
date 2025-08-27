# Activity: Polymorphism Challenge
# Classes: Dog, Cat, Bird (all inherit from Animal)

class Animal:
    def sound(self):
        print("Animal must make a sound")

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Bird(Animal):
    def sound(self):
        return "Chirp!"

    # Example
if __name__ == "__main__":
    animals = [Dog(), Cat(), Bird()] 

    print("Polymorphism in action:\n")
    for animal in animals:
        print(animal.sound())
