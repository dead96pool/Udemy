import random

class Enemy:

    def __init__(self,low, high):
        self.attkl = low
        self.attkh = high

    def getAttk(self):
        print(self.attkl)

enemy1 = Enemy(60,80)

enemy1.getAttk()