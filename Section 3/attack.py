import random


'''
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

'''