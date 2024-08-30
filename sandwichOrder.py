import os
import time
import roulette
from roulette import response

isContinue = True
response = ""
def orderFood(isContinue, response, money):
  while isContinue:
    print("Please use correct spelling. Please only enter in the options presented.")
    totalCost = 0.0
    noAnswer = True
    isKetchup = True
    isSandwich = True
    isDrink = True
    isFries = True
    order = ["", "", "", 0]
    deny = ["no", "nope", "naw", "no thanks"]
    approve = ["yes", "sure", "yep", "yea", "yass", "ya"]
    sandwichIndex = 0
    drinkIndex = 1
    fryIndex = 2
    ketchupIndex = 3
    while noAnswer:
      order[sandwichIndex] = input("Would you like a sandwich? Types: chicken ($5.25), beef ($6.25), tofu ($5.75)")
      if order[sandwichIndex].lower() == "chicken":
            print("You have chosen " + order[sandwichIndex].lower())
            totalCost = 5.25
            noAnswer = False
      elif order[sandwichIndex].lower() == "beef":
            print("You have chosen " + order[sandwichIndex].lower())
            totalCost = 6.25
            noAnswer = False
      elif order[sandwichIndex].lower() == "tofu":
            print("You have chosen " + order[sandwichIndex].lower())
            totalCost = 5.75
            noAnswer = False
      elif order[sandwichIndex].lower() in deny:
            print("You did not order a sandwich")
            isSandwich = False
            noAnswer = False
      else:
            print("Please check if you misspelled anything or your option is present on the list and try again.")
            noAnswer = True
    noAnswer = True
    while noAnswer:
      order[drinkIndex] = input("Would you like a drink? Sizes: small ($1), medium ($1.75), large ($2.25)")
      if order[drinkIndex].lower() == "small":
            totalCost += 1.00
            noAnswer = False
            print("You have chosen " + order[drinkIndex].lower())
      elif order[drinkIndex].lower() == "medium":
            totalCost += 1.75
            noAnswer = False
            print("You have chosen " + order[drinkIndex].lower())
      elif order[drinkIndex].lower() == "large":
            totalCost += 2.25
            noAnswer = False
            print("You have chosen " + order[drinkIndex].lower())
      elif order[drinkIndex].lower() in deny:
            print("You did not select a drink")
            isDrink = False
            noAnswer = False
      else:
            print("Please check if you misspelled anything or your option is present on the list and try again.")
            noAnswer = True
    noAnswer = True
    while noAnswer:
      order[fryIndex] = input("Would you like fries? Sizes: small ($1), medium ($1.50), large ($2.00)")
      noAnswer = True
      if order[fryIndex].lower() == "small":
          megaSize = input("Would you like to mega-size your fries?")
          noAnswer = True
          while noAnswer:
            if megaSize.lower() in approve:
              order[fryIndex] = "large"
              print("You have chosen " + order[fryIndex])
              totalCost += 2.00
              noAnswer = False
            elif megaSize.lower() in deny:
              print("You have chosen " + order[fryIndex].lower())
              totalCost += 1.00
              noAnswer = False
            else:
              noAnswer = True
      elif order[fryIndex].lower() == "medium":
          print("You have chosen " + order[fryIndex].lower())
          totalCost += 1.50
          noAnswer = False
      elif order[fryIndex].lower() == "large":
          print("You have chosen " + order[fryIndex].lower())
          totalCost += 2.00
          noAnswer = False
      elif order[fryIndex].lower() in deny:
          print("You did not chose fries")
          isFries = False
          noAnswer = False
      else:
          print("Please check if you misspelled anything or your option is present on the list and try again.")
          noAnswer = True
    noAnswer = True
    while noAnswer:
      order[ketchupIndex] = int(input("How many ketchup packets would you like? (positive integers only, $0.25 per packet)"))
      if type(order[ketchupIndex]) == int:
          totalCost += (int(order[ketchupIndex]) * 0.25)
          print(str(order[ketchupIndex]) + " ketchup packets.")
          isKetchup = True
          noAnswer = False
      else:
          print("No ketchup packets then")
          isKetchup = False
          order[ketchupIndex] = 0
          noAnswer = False
    if isSandwich == True and isDrink == True and isFries == True:
      totalCost -= 1.00
      print("You've saved $1 by ordering a sandwich, drink and fries!")
    if isSandwich == False and isDrink == False and isFries == False and isKetchup == False:
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
    if isSandwich == False and isDrink == False and isFries == False:
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
      print("\nYour total is $" + str(ketchupIndex * 0.25))
      money -= totalCost
    elif isSandwich == False and isDrink == False:
      print("Your order is some " + str(order[fryIndex].lower()) + " fries and " + str(order[ketchupIndex].lower()) + " ketchup packets. Your final cost is $" + str(totalCost))
      money -= totalCost
    elif isDrink == False and isFries == False:
      print("Your order is a " + str(order[sandwichIndex].lower()) + " sandwich with " + str(order[ketchupIndex]) + " ketchup packets. Your final cost is $" + str(totalCost))
      money -= totalCost
    elif isSandwich == False and isFries == False:
      print("Your order is a " + str(order[drinkIndex].lower()) + " drink and " + str(order[ketchupIndex]) + " ketchup packets. Your final cost is $" + str(totalCost))
      money -= totalCost
    elif isSandwich == False:
      print("Your order is a " + str(order[drinkIndex].lower()) + " drink with " + str(order[fryIndex].lower()) + " fries and " + str(order[ketchupIndex]) + " ketchup packets. Your final cost is $" + str(totalCost))
      money -= totalCost
    elif isDrink == False:
      print("Your order is a " + str(order[sandwichIndex].lower()) + " sandwich with " + str(order[fryIndex].lower()) + " fries and " + str(order[ketchupIndex]) + " ketchup packets. Your final cost is $" + str(totalCost))
      money -= totalCost
    elif isFries == False:
      print("Your order is a " + str(order[sandwichIndex].lower()) + " sandwich with a " + str(order[drinkIndex].lower()) + " drink and " + str(order[ketchupIndex]) + " ketchup packets. Your final cost is $" + str(totalCost))
      money -= totalCost
    else:
      print("Your order is a " + str(order[sandwichIndex].lower()) + " sandwich with a " + str(order[drinkIndex].lower()) + " drink, " + str(order[fryIndex].lower()) + " fries and " + str(order[ketchupIndex]) + " ketchup packets. Your final cost is $" + str(totalCost))
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