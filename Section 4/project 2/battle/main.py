from classes.game import Person, bcolors

magic = [{"name": "Fire",       "cost": 10,     "dmg": 60},
         {"name": "Thunder",    "cost": 12,     "dmg": 80},
         {"name": "Blizzard",   "cost": 10,     "dmg": 60}]

# person class (hp, mp, atk, df, magic) argumetns in order
player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("=============================")
    player.choose_action()

    running = False