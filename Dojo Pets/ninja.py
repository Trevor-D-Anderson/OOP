import pets

class Ninja:
    def __init__(self, firstName, lastName, treats, petFood, pet):
        self.firstName = firstName
        self.lastName = lastName
        self.treats = treats
        self.petFood = petFood
        self.pet = pet

    def findPet(self, name, type, tricks):
        self.pet = pets.Pet(name, type, tricks)
        print(f"You have found a {type} named {name}")

    def walk(self, pet):
        