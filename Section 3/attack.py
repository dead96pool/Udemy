import random

playerhp = 260
enemyattklow = 60     # enemy attack low value 
enemyattkhi = 80      # enemy attack high value


while playerhp > 0:
  dmg = random.randrange(enemyattklow, enemyattkhi)
  playerhp -= dmg
  
  if playerhp <= 0:
    playerhp = 0
  
  print("Attack for ",dmg," points. Remaining HP is ",playerhp)