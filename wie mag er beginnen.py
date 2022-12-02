import random 

print("Hoeveel spelers zijn er?")
int(input())

print("Zet de namen een voor een achterelkaar: ")
namen = input()
namen = str(namen).split ()

r = random.choice(namen)

print(r)
