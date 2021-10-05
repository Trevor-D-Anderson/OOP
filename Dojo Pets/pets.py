class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        if self.energy >= 75:
            print(f"{self.name} isn't tired, play with {self.name} some more.")
        elif self.energy <75:
            self.energy += 25
            print(f"{self.name} is sleeping.")

    def eat(self, petFood):
        if self.energy <= 95 and self.health <= 90:
            self.energy += 5
            self.health += 10
            print(f"{self.name} has eaten {petFood} with the following effects:")
            print(f"Energy has increased by 5 to {self.energy}.")
            print(f"Health has increased by 10 to {self.health}.")
        elif self.energy <= 95 and self.health > 90:
            self.energy += 5
            self.health = 100
            print(f"{self.name} has eaten {petFood} with the following effects:")
            print(f"Energy has increased by 5 to: {self.energy}")
            print(f"Health is maxed out to: {self.health}")
        elif self.energy >= 95 and self.health <= 90:
            self.energy = 100
            self.health += 10
            print(f"{self.name} has eaten {petFood} with the following effects:")
            print(f"Health has increased by 10 to: {self.health}")
            print(f"Energy is maxed out to: {self.energy}")
        else:
            print(f"Your pet isn't hungry. Play with them some more.")

    def play(self):
        if self.energy or self.health <= 10:
            print(f"{self.name} needs to rest. Try again later")
        else:
            self.energy -= 10
            self.health -= 5
            print(f"{self.name} loves you!")
    def noise(self):
        if self.type == "Dog":
            print("Woof")
        elif self.type == "Cat":
            print("Meow")
        elif self.type != "Cat" or "Dog":
            print("Get a better pet")
