from random import *
import re
import requests


randomHero1 = "https://superheroapi.com/api/537520747252406/" + str(randint(1,731))
randomHero2 = "https://superheroapi.com/api/537520747252406/" + str(randint(1,731))


character1 = requests.get(randomHero1).json()
character2 = requests.get(randomHero2).json()


print(character1)
print("")
print(character2)

for key, value in character1.items():
    if value == "null":
        character2.update({key: "0"})

for key, value in character2.items():
    if value == "null":
        character2.update({key: "0"})



def getCharName(character):
    charName = character['name']
    charFullName = character['biography']['full-name']
    return "Alias: " + charName + " " + "Fullname: " + charFullName


def getCharPowerstats(character):
    charInt = int(character['powerstats']['intelligence'].replace("null", "0"))
    charStr = int(character['powerstats']['strength'].replace("null", "0"))
    charSpd = int(character['powerstats']['speed'].replace("null", "0"))
    charDur = int(character['powerstats']['durability'].replace("null", "0"))
    charPow = int(character['powerstats']['power'].replace("null", "0"))
    charCom = int(character['powerstats']['combat'].replace("null", "0"))
    print("Intelligene: " + str(charInt) + '\n' + "Strength: " + str(charStr) + '\n' + "Speed: " +str(charSpd) + '\n' + "Durability: " + str(charDur) + '\n' + "Power: " + str(charPow) 
    + '\n' + "Combat: " +str(charCom))
    totalPower = charInt + charStr + charSpd + charDur + charPow + charCom
    print("Total Power: " + str(totalPower))
    return totalPower
     

def calcWinner(character1,character2):
    print(getCharName(character1))
    char1Power = getCharPowerstats(character1) 
    print("\n")
    print(getCharName(character2))
    char2Power = getCharPowerstats(character2)
    print("\n")
    if char1Power > char2Power:
        print(getCharName(character1) + " Wins")
    else:
        print(getCharName(character2) + " Wins")
    

calcWinner(character1,character2)