from classes.game import Person, bcolors
from classes.magic import Spell

# instantiate Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# create White Magic
cure = Spell("Cure",  12, 120, "white")
cura = Spell("Cura", 18, 200, "white")


# Intantiate People
# person class (hp, mp, atk, df, magic) argumetns in order
player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("=============================")
    player.choose_action()

    choice = input("Enter choice: ")
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
        magic_choice = int(input("Choose magic: ")) - 1                     # to account for the first index in list starting from 0 not 1

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
        elif spell.name == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals", magic_dmg, "points of damage." + bcolors.ENDC)


    #enemy turn to attack or magic
    enemy_choice = 1                    # enemy chose to attack
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacked for", enemy_dmg, "points of damage.")

    # end of player and enemy turn
    # display both player and enemy HP/MAX_HP
    print("=============================")
    print("Enemy HP: ", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    
    print("Your HP: " + bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP: " + bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")
    
    # end look if hp reaches 0
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False
