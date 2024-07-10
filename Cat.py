# game.py

class Game:
    def __init__(self, name, food, stamina=100, enjoyment=50):
        self.name = name
        self.food = food
        self.stamina = stamina
        self.enjoyment = enjoyment

    def play(self, play_type):
        if self.stamina >= 20:
            if play_type == 'ball':
                print(f"{self.name} is playing with a ball!")
                self.stamina -= 20
                self.enjoyment += 15
            elif play_type == 'mud':
                print(f"{self.name} is playing in the mud!")
                self.stamina -= 30
                self.enjoyment += 10
            elif play_type == 'toys':
                print(f"{self.name} is playing with toys!")
                self.stamina -= 25
                self.enjoyment += 20
            else:
                print("Invalid play type.")
        else:
            print(f"{self.name} doesn't have enough stamina to play!")

    def eat(self, food_type):
        if self.food == 0:
            print(f"{self.name} is eating {food_type}...")
            self.stamina += 50
            self.food -= 1
        else:
            print(f"{self.name} has no food left to eat!")

    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.stamina += 30

    def check_stamina(self):
        print(f"{self.name} has {self.stamina} stamina.")

    def status(self):
        print(f"Name: {self.name}, Food: {self.food}, Stamina: {self.stamina}, enjoyment: {self.enjoyment}")

    def talk(self):
        user_input = input("What do you want Tom to say? ").strip().lower()
        if user_input == "hello":
            print(f"{self.name} says: hello")
        else:
            print(f"{self.name} says: {user_input}")

    def groom(self):
        print(f"You are grooming {self.name}...")
        self.enjoyment += 20
        print(f"{self.name} looks happier now!")
