import random
#from .magic import Spell

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
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp                                 # max HP
        self.hp = hp                                    # current hp
        self.maxmp = mp                                 # max MP
        self.mp = mp                                    # current MP
        self.atkl = atk - 10                            # low atk
        self.atkh = atk + 10                            # high atk
        self.df = df
        self.magic = magic
        self.items = items
        self.name = name
        self.actions = ["Attack", "Magic", "Items"]
    
    # method to generate random damage points
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
    
    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self.maxhp
    
    def get_mp(self):
        return self.mp
    
    def get_max_mp(self):
        return self.maxmp
    
    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n    " + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "    ACTIONS:" + bcolors.ENDC)
        for item in self.actions:
            print("     " + str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print("     " + str(i) + ".", spell.name, "(Cost:", str(spell.cost)+")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "    ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print("     " + str(i) + ".", item["item"].name + ":", item["item"].desc, " (x" + str(item["quantity"]) + ")" )
            i += 1

    def choose_target(self, enemies):
        i = 1
        
        if len(enemies) == 1:
            return 0


        print(bcolors.BOLD + bcolors.FAIL + "    TARGET:" + bcolors.ENDC)
        
        for enemy in enemies:
            print("        " + str(i) + "." + enemy.name)
            i += 1
        choice = int(input("    Choose Target: ")) - 1
        return choice
    
    # print enemy stats
    def get_enemy_stats(self):
        hp_bar = ""
        hp_ticks = (self.hp/self.maxhp) * 50

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 10

        while hp_ticks > 0:
            hp_bar += "█"
            hp_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "


        # mp bar
        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += " "


        print("{:<35}{:<70}{:}".format("", str("_"*50), str("_"*10) ))
        # formating to align left and be 4 and 2 characters long resp
        print(bcolors.BOLD + "{:<13}{:>20} ".format(self.name + ":", str(self.hp) + "/" + str(self.maxhp)) + "|" + bcolors.FAIL + hp_bar + bcolors.ENDC + "|" +
                        "{:>17} ".format(str(self.mp) + "/" + str(self.maxmp)) + "|" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|\n" )        
    
    # ascii 219 | █ to print player HP/MP bar
    def get_stats(self):
        hp_bar = ""
        hp_ticks = (self.hp / self.maxhp) * 25            # calculate the percentage of the bar

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 10

        # hp bar
        while hp_ticks > 0:
            hp_bar += "█"
            hp_ticks -= 1
        while len(hp_bar) < 25:
            hp_bar += " "

        # mp bar
        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += " "

        #print("                      _________________________               __________")
        print("{:<35}{:<70}{:}".format("",str("_"*25), str("_"*10)))
        # formating to align left and be 4 and 2 characters long resp
        """print(bcolors.BOLD + self.name + "     " + 
                "{:>{hp_len}}".format(str(self.hp), hp_len = hp_len) + "/" + str(self.maxhp) + " |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + "|       " + bcolors.BOLD +
                "{:>{mp_len}s}".format(str(self.mp), mp_len = mp_len) + "/" + str(self.maxmp) + " |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|\n")
        """
        print(bcolors.BOLD + "{:<13}{:>20} ".format(self.name + ":", str(self.hp) + "/" + str(self.maxhp)) + "|" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + "|" +
                        "{:>42} ".format(str(self.mp) + "/" + str(self.maxmp)) + "|" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|\n" )
        

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))

        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        # enemy hp percentage
        pct = self.hp / self.maxhp * 100

        # if enemy hp more than 50% and the spell is white or mp lower than cost of spell
        if self.mp < spell.cost or spell.type == "white" and pct > 50:
            return self.choose_enemy_spell()
        else:
            return spell, magic_dmg

