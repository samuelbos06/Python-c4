import random 
import time

while True:
 open = input("Wil je een lootbox openen? y/n: ")

 if  open == "y":
  lootbox = ("common", "uncommon", "rare", "epic", "legendary")
  print("Spinning.......")
  time.sleep(2)
  print("Je hebt een:")
  print(random.choices(lootbox, weights=(50, 25, 15, 7, 3)))

 if open == "n":
     print("Dan openen we er geen ;)")
     break
