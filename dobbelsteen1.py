import random
import time

print("Welkom bij mijn prachtige dobbelsteenspel")
print("-------------------------------------------")

print("Hoeveel dobbelstenen wil je gooien>")
### Aantal



while True:

    numberPicked = int(input("Kies tussen de 1 en 1000000 "))
    if(numberPicked > 0 and numberPicked < 1000000):
     break
print("Dobbelstenen worden gegooid:")
time.sleep(2)
#def is een defined function. 
def rollDice(amountOfDice):
  totalSum = 0
  possibleFaces = [1,2,3,4,5,6]
  #Bepaald hoeveel dices die gooit met deze possiblefaces
  for dice in range(amountOfDice):
    roll = random.choice(possibleFaces)
    #dice + 1 weergeeft welke dobbelsteen gegooid is. bv nummer 4
    print("Nummer ", dice + 1, ": ", roll)
    totalSum += roll

  print("Totale som: ", totalSum)



rollDice(numberPicked)