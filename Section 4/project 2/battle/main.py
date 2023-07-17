
from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

# instantiate Black Magic
# def __init__(self, name, cost, dmg, type):
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")

# create White Magic
cure = Spell("Cure",  25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")
curaga = Spell("Curaga", 50, 6000, "white")


# create buncha items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully Restores HP/MP of one party-member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
enemy_spells = [fire, meteor, curaga]

player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5}, 
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity": 5}]


# Intantiate People
# Person def __init__(self, name, hp, mp, atk, df, magic, items):
player1 = Person("Valos", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Nick", 4160, 188, 311, 34, player_spells, player_items)
player3 = Person("Robot", 3089, 174, 288, 34, player_spells, player_items)


enemy1 = Person("Imp", 1250, 130, 560, 325, enemy_spells, [])
enemy2 = Person("Magus", 18200, 701, 525, 25, enemy_spells, [])
enemy3 = Person("Imp", 1250, 130, 560, 325, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy2]

running = True
i = 0

print("\n\n")
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:

    # # check if battle is over
    # defeated_enemies = 0
    # defeated_players = 0

    # for enemy in enemies:
    #     if enemy.get_hp() == 0:
    #         defeated_enemies += 1

    # for player in players:
    #     if player.get_hp() == 0:
    #         defeated_players += 1

    # # check if player won
    # if defeated_enemies == 2:
    #     print("\n")
    #     for player in players:
    #         player.get_stats()
    #     print("\n\n")
    #     for enemy in enemies:
    #         enemy.get_enemy_stats()
    #     print(bcolors.BOLD + bcolors.OKGREEN + "\nYou win!\n" + bcolors.ENDC)
    #     running = False
    # # check if enemy won
    # elif defeated_players == 2:
    #     print("\n")
    #     for player in players:
    #         player.get_stats()
    #     print("\n\n")
    #     for enemy in enemies:
    #         enemy.get_enemy_stats()
    #     print(bcolors.BOLD + bcolors.FAIL + "\nYour enemies have defeated you!\n" + bcolors.ENDC)
    #     running = False
    
    #print(bcolors.FAIL + bcolors.BOLD + "Enemy/Players count: " + str(len(enemies)) + "/" + str(len(players)) + bcolors.ENDC )
    
    if len(enemies) == 0:
        print("\n")
        print(bcolors.BOLD + bcolors.OKGREEN + "\nYou win!\n" + bcolors.ENDC)
        running = False
        break

    elif len(players) == 0:
        print("\n")
        print(bcolors.BOLD + bcolors.FAIL + "\nYour enemies have defeated you!\n" + bcolors.ENDC)
        running = False
        break

    print("=============================")

    print("\n")
    #print("NAME                  HP                                      MP")
    print("{:<35}{:<70}".format("NAME","HP") + "MP")
    # to print player stats at the start of every loop/round
    for player in players:
        player.get_stats()
        
    print("\n")
        
    for enemy in enemies:
        enemy.get_enemy_stats()

    # the actual round/loop
    for player in players:
        if len(enemies) == 0 or len(players) == 0:
            continue
        player.choose_action()
        choice = input("    Choose Action: ")
        index = int(choice) - 1



        # player choice between attack or magic
        # attack
        if index == 0:
            dmg = player.generate_damage()
            
            enemy = player.choose_target(enemies)
            
            enemies[enemy].take_damage(dmg)

            print("\nYou attacked " + enemies[enemy].name + " for", dmg, "points of damage.")
            
            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + " has died.")
                del enemies[enemy]
                 
        # player chose magic
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic: ")) - 1                     # to account for the first index in list starting from 0 not 1

            if magic_choice == -1:
                continue


            spell = player.magic[magic_choice]                  # going to the magic class object though the People class object | person's magic's object
            magic_dmg = spell.generate_damage()
            
            
            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)
            # white magic heals player hp
            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", magic_dmg, "HP." + bcolors.ENDC)
            # black magic deals damage
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
            
                enemies[enemy].take_damage(magic_dmg)

                print(bcolors.OKBLUE + "\n" + spell.name + " deals", magic_dmg, "points of damage to " + enemies[enemy].name + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died.")
                    del enemies[enemy]
        # player choose items
        elif index == 2:
            player.choose_item()                                    # prints a list of items for the player to chose
            item_choice = int(input("    Choose Item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            # check if the chosen item is not zero
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None Left ..." + bcolors.ENDC)
                continue
            player.items[item_choice]["quantity"] -= 1              # reduce the quantity of the item being used

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", item.prop, "HP" + bcolors.ENDC)
            elif item.type == "elixer":

                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:        
                    player.hp = player.maxhp
                    player.mp = player.maxmp

                print(bcolors.OKGREEN + "\n" + item.name + " fully restore player HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                
                print(bcolors.FAIL + "\n" + item.name + " deals", item.prop, "points of damage to " + enemies[enemy].name + bcolors.ENDC)
                
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died.")
                    del enemies[enemy]
                 

    print("\n")
    # enemy attack phase

    for enemy in enemies:
        if len(enemies) == 0 or len(players) == 0:
            continue
        enemy_choice = random.randrange(0,2)

        if enemy.mp == 0:
            enemy_choice = 1

        # enemy chose attack
        if enemy_choice == 0:
            target = random.randrange(0,len(players))
            enemy_dmg = enemy.generate_damage()
            players[target].take_damage(enemy_dmg)
            print(enemy.name + " attacked " + players[target].name + " for", enemy_dmg, "points of damage.")

        # enemy chose magic
        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)
            
            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(bcolors.OKBLUE + spell.name + " heals " + enemy.name + " for", magic_dmg, "HP." + bcolors.ENDC)
            # black magic deals damage
            elif spell.type == "black":
                target = random.randrange(0,len(players))
            
                players[target].take_damage(magic_dmg)

                print(bcolors.OKBLUE + enemy.name + "'s " + spell.name + " deals", magic_dmg, "points of damage to " + players[target].name + bcolors.ENDC)

                if players[target].get_hp() == 0:
                    print(players[target].name + " has died.")
                    del players[target]

            # print(enemy.name + " chose", spell.name, "damage is", magic_dmg)

