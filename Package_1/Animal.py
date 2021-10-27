import math


class Animal:

    #default hunger & energy is 5 and must be between 0 - 10
    def __init__(self, name, hunger=5, energy=5):
        self.name = name
        self.hunger = hunger
        if hunger<0 and hunger>10:
            print("hunger level not between 0-10, has been set to default (5)")
            self.hunger=5
        self.energy = energy
        if energy<0 and energy>10:
            print("energy level not between 0-10, has been set to default (5)")
            self.energy=5


    def __str__(self):
        self.name, self.hunger, self.energy
        return

    def eat(self, food):
        self.food=food
        count=0
        eat_repeat=(math.floor(food/50))
        #part in charge of hunger
        for i in range(eat_repeat):
            if food >= 50:
                food -= 50
                self.hunger -= 1
                count += 1
                if self.hunger < 0:
                    self.hunger = 0
                    print(self.name, "is full but not done eating.")
            else:
                print(self.name, "is done eating.")
            #part in charge of energy
            if count%2==0:
                self.energy -= 1
                if self.energy < 0:
                    self.energy = 0

    def play(self, playtime, hunger, energy):
        self.playtime=playtime
        self.hunger=hunger
        self.energy=energy
        play_repeat= (math.floor(playtime/10))
        for i in range(play_repeat):
            if self.playtime > 10:
                self.playtime -= 10
                self.energy -= 2
                self.hunger += 2
                if self.energy < 0:
                    self.energy = 0
                    print(self.name, "game finished, the animal is too tired")
                    break
                if self.hunger > 10:
                    self.hunger = 10


