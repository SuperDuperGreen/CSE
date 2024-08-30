import os
import time

isContinue = True
response = ""
money = 1000
while isContinue:
    totalCost = 0
    weaponIncrease = 0
    armorIncrease = 0
    kills = 0
    noAnswer = True
    isWeapon = True
    isArmor = True
    isPotion = True
    order = ["", "", "", 0]
    deny = ["no", "nope", "naw", "no thanks"]
    approve = ["yes", "sure", "yep", "yea", "yass", "ya"]
    weaponIndex = 0
    armorIndex = 1
    potionIndex = 2
    trophyIndex = 3
    print("Welcome to the Hero Shop for adventurers like you!")
while noAnswer:
    order[weaponIndex] = input("Would you like upgrade your weapon? (" + weaponIncrease + " gold")
    if order[weaponIndex].lower() in approve:
        print("Thank you! That'll be " + (10 + (10 * weaponIncrease)) + " gold")
        totalCost = (10 + (10 * weaponIncrease))
        weaponIncrease += 0.1
        noAnswer = False
    elif order[weaponIndex].lower() in deny:
        print("No upgrades this time?")
        isWeapon = False
        noAnswer = False
    else:
        print("I'm not pickin' up what you're puttin' down...")
        noAnswer = True
noAnswer = True
while noAnswer:
    order[armorIndex] = input("Would you like some new armor?")
    if order[armorIndex].lower() in approve:
        print("That'll be " + (10 + (10 * armorIncrease)) + " gold. Enjoy!")
        totalCost += (10 + (10 * armorIncrease))
        weaponIncrease += 0.1
        noAnswer = False
    elif order[armorIndex].lower() in deny:
        print("No upgrades this time, then.")
        isArmor = False
        noAnswer = False
    else:
        print("I'm not pickin' up what you're puttin' down...")
        noAnswer = True
noAnswer = True
while noAnswer:
    order[potionIndex] = input("Would you like a nice potion? Types: strength (10 gold), speed (5 gold), defense (15 gold)")
    noAnswer = True
    if order[potionIndex].lower() == "strength":
        print("You have chosen " + order[potionIndex].lower())
        totalCost += 10
        noAnswer = False
    elif order[potionIndex].lower() == "speed":
        print("You have chosen " + order[potionIndex].lower())
        totalCost += 5
        noAnswer = False
    elif order[potionIndex].lower() == "defense":
        print("You have chosen " + order[potionIndex].lower())
        totalCost += 15
        noAnswer = False
    elif order[potionIndex].lower() in deny:
        print("No potions this time then.")
        isPotion = False
        noAnswer = False
    else:
        print("I'm not pickin' up what you're puttin' down...")
        noAnswer = True
noAnswer = True
order[trophyIndex] = int(kills) / 10
print("Let's see how many trophies you earned for your kills...")
print("You got " + order[trophyIndex] + " trophies this time!")
if isWeapon == True and isArmor == True and isPotion == True:
    totalCost -= 10
    print("You've saved 10 gold through our special buddy bundle!")
if isWeapon == False and isArmor == False and isPotion == False:
    time.sleep(2)
    print("Wow. You just ordered nothing.")
    time.sleep(2)
    print("Congrats, now you get to reap your reward.")
    time.sleep(2)
    print("Have fun in the Infinite Print Loop!")
    time.sleep(2)
    totalCost = 0
    while True:
        totalCost += 9999999999
    print(totalCost)
if isWeapon == False and isArmor == False and isPotion == False:
    print("Your order is...")
    time.sleep(1.5)
    print("\nWait. You seriously just got ketchup?")
    time.sleep(1.5)
    print("\nIf you just wanted ketchup,\njust go to the store and buy some!")
    time.sleep(1.5)
    print("\nGet out ya weirdo!")
    time.sleep(1.5)
    os.system('cls')
    time.sleep(3)
    print("Ok. Fine.")
    time.sleep(1)
    print("\nYour total is $" + str(trophyIndex * 0.25))
    money -= totalCost
elif isWeapon == False and isArmor == False:
    print("Your order is some " + str(order[potionIndex].lower()) + " fries and " + str(order[trophyIndex].lower()) + " ketchup packets. Your final cost is $" + str(totalCost))
    money -= totalCost
elif isArmor == False and isPotion == False:
    print("Your order is a " + str(order[weaponIndex].lower()) + " sandwich with " + str(order[trophyIndex]) + " ketchup packets. Your final cost is $" + str(totalCost))
    money -= totalCost
elif isWeapon == False and isPotion == False:
    print("Your order is a " + str(order[armorIndex].lower()) + " drink and " + str(order[trophyIndex]) + " ketchup packets. Your final cost is $" + str(totalCost))
    money -= totalCost
elif isWeapon == False:
    print("Your order is a " + str(order[armorIndex].lower()) + " drink with " + str(order[potionIndex].lower()) + " fries and " + str(order[trophyIndex]) + " ketchup packets. Your final cost is $" + str(totalCost))
    money -= totalCost
elif isArmor == False:
    print("Your order is a " + str(order[weaponIndex].lower()) + " sandwich with " + str(order[potionIndex].lower()) + " fries and " + str(order[trophyIndex]) + " ketchup packets. Your final cost is $" + str(totalCost))
    money -= totalCost
elif isPotion == False:
    print("Your order is a " + str(order[weaponIndex].lower()) + " sandwich with a " + str(order[armorIndex].lower()) + " drink and " + str(order[trophyIndex]) + " ketchup packets. Your final cost is $" + str(totalCost))
    money -= totalCost
else:
    print("Your order is a " + str(order[weaponIndex].lower()) + " sandwich with a " + str(order[armorIndex].lower()) + " drink, " + str(order[potionIndex].lower()) + " fries and " + str(order[trophyIndex]) + " ketchup packets. Your final cost is $" + str(totalCost))
    money -= totalCost
noAnswer = True
if money == 0:
    print("Your outta money. So long!")
    quit()
elif money > 0:
    print("...\n")
    time.sleep(1)
    print("Your in trouble now...\n")
    time.sleep(1)
    print("I'm in your walls...")
    time.sleep(1)
    print(1/0)
else:
    print("Thank you for ordering!")