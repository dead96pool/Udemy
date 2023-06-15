import random

class Enemy:

  #class variables
  hp = 200
  #init method
  def __init__(self,atk_low, atk_high):
    #class variables
    self.atk_low = atk_low
    self.atk_high = atk_high

  #class methods
  def getAtk(self):
    print("Low attack is:",self.atk_low)
  
  def getHP(self):
    print("hp is:",self.hp)


enemy1 = Enemy(60,80)
enemy1.getAtk()
enemy1.getHP()

enemy2 = Enemy(50,80)
enemy2.getAtk()
enemy2.getHP()
"""
playerhp = 260
enemyattklow = 60     # enemy attack low value 
enemyattkhi = 80      # enemy attack high value

while playerhp > 0:
  dmg = random.randrange(enemyattklow, enemyattkhi)
  playerhp -= dmg
  
  if playerhp < 30:     # player health doesnt go below 30
    playerhp = 30
  
  print("Attack for ",dmg," points. Remaining HP is ",playerhp)
    
  if playerhp > 30:
    continue            # continue to while if hp above 30 
  
  # when player hp is at 30
  print("HP too low. You have been teleported to the nearest inn.")
  break
"""