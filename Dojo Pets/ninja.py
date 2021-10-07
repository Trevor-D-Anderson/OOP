from pets import Pet

class Ninja:
    def __init__(self, firstName, lastName, treats, petFood, pet):
        self.firstName = firstName
        self.lastName = lastName
        self.treats = treats
        self.petFood = petFood
        self.pet = pet

    def findPet(self, name, type, tricks):
        self.pet = Pet(name, type, tricks)
        print(f"You have found a {type} named {name}")
        return self

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat(self.petFood)
        return self

    def bathe(self):
        self.pet.noise()
        print(f"You have given {self.pet.name} a bath!")
        return self

trevor = Ninja("Trevor", "Anderson", "Bacon", "Steak", "Dog")
trevor.findPet("Fluffy", "Dog", "Jump").walk().bathe().feed()

