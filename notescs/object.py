# Classes and objects notes

# Class is a blueprint for creating an object"
class pokemon:
    def __init__(self, name, species, hp, damage):
        self.name = name 
        self.species = species 
        self.hp = hp 
        self.damage = damage
    

bob = pokemon("Mr.Bob", "Charizard", 300, 95)
fluffy = pokemon("Fluffy", "Arcanine", 90, 110)

print(bob.species)
print(fluffy.species)

#Every injustice of a class is an object
#A method is a function that is specific to a class
