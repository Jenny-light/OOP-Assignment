# Create a class representing a Superhero.
class Character:
    def __init__(self, name, age, universe):
        self.name = name
        self.age = age
        self.universe = universe

def character_info(character):
    return f"Name: {character.name}, Age: {character.age}, Universe: {character.universe}" 

# child class (inherits from character)
class Superhero(Character):
    def __init__(self, name, age, universe, power, weapon):
        super().__init__(name, age, universe)
        self.power = power
        self.weapon = weapon

    def use_power(self):
        return f"{self.name} uses {self.power}!"

    def attack(self):
        return f"{self.name} attacks with {self.weapon}!"

    def get_info(self):
        base_info = character_info(self)
        return f"{base_info}, Power: {self.power}, Weapon: {self.weapon}"

# Create an instance of your class and demonstrate its functionality.
hero = Superhero("Spider-Man", 25, "Marvel", "Web-Slinging", "Web Shooters")
print(hero.get_info())
print(hero.use_power())
print(hero.attack()) 

hero2 = Superhero("Batman", 35, "DC", "Stealth", "Batarang")
print(hero2.get_info())
print(hero2.use_power())
print(hero2.attack())












