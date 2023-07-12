import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    # initializing the variables
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp                                 # max HP
        self.hp = hp                                    # current hp
        self.maxmp = mp                                 # max MP
        self.mp = mp                                    # current MP
        self.atkl = atk - 10                            # low atk
        self.atkh = atk + 10                            # high atk
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]
    
    # method to generate random damage points
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)
    