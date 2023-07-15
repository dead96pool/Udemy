
from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item


# instantiate Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# create White Magic
cure = Spell("Cure",  12, 120, "white")
cura = Spell("Cura", 18, 200, "white")


# create buncha items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully Restores HP/MP of one party-member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]

player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5}, 
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity": 5}]


# Intantiate People
# person class (hp, mp, atk, df, magic) argumetns in order
player1 = Person("Valos:", 31190, 1165, 60, 34, player_spells, player_items)
player2 = Person("Nick :", 4160, 1165, 60, 34, player_spells, player_items)
player3 = Person("Robot:", 3089, 1165, 60, 34, player_spells, player_items)
enemy = Person("Magus", 12000, 65, 380, 25, [], [])

players = [player1]



running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("=============================")

    print("\n\n")
    print("NAME                  HP                                      MP")
    # to print player stats at the start of every loop/round
    for player in players:
        player.get_stats()
        
    print("\n")
        

    # the actual round/loop
    for player in players:
        player.choose_action()
        choice = input("    Choose Action: ")
        index = int(choice) - 1
        

        # player choice between attack or magic
        # attack
        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for", dmg, "points of damage.")

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
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", magic_dmg, "points of damage." + bcolors.ENDC)

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
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restore player HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", item.prop, "points of damage" + bcolors.ENDC)


    #enemy turn to attack or magic
    enemy_choice = 1                    # enemy chose to attack
    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)
    print("Enemy attacked for", enemy_dmg, "points of damage.")

    # end of player and enemy turn
    # display both player and enemy HP/MAX_HP
    print("=============================")
    print("Enemy HP: ", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    

    # end the game if hp reaches 0
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player1.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False
