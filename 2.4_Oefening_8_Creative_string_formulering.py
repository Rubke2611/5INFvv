voornaam = input("Voornaam: ")
achternaam = input("Achternaam: ")
functietitel = input("Functietitel: ")

naam = f"{voornaam} {achternaam}".upper()

#Breedtje bepalen op basis van de lagnste regel (+ marge van 2 spaties link/rechts)
breedte = max(len(naam), len(functietitel)) + 4

rand = "+" + "-" * breedte + "+"
regel_naam = "|" + naam.center(breedte) + "|"
regel_functie = "|" + functietitel.center(breedte) + "|"

print(rand)
print(regel_naam)
print(regel_functie)
print (rand)
