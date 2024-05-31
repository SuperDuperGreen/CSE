import random
import time
import os

roulette = [1, 2, 3, 4, 5]
percent = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
noAnswer = True
noBet = True
bet = 0
spin = 0
rig = 0
user = 0
money = 1000
# sets and tracks the user's bet, preventing them from betting something
# they can't and warning them if they bet really high
def betting(bet, money, noBet):
  while noBet:
    bet = int(input("How much would you like to bet in $? (Numbers only, no cents)"))
    # if type(bet) == :
    #   print("You can't bet that")
    #   noBet = True
    if bet > money:
      print("You can't bet that much")
      noBet = True
    elif bet == money:
      print("Warning: You will have to restart if you lose with this bet")
      noBet = False
      print("You bet $" + str(bet))
      return bet
    elif bet < 0:
      print("You can't have a negative bet")
      noBet = True
    else:
      noBet = False
      print("You bet $" + str(bet))
      return bet
  noBet = False
# creates a mini loading animation
def load():
  sym = [".", ".", "."]
  for i in range(3):
    print(sym[i]),
    time.sleep(.5)
# initiates the game
print("You have $" + str(money))
bet = betting(bet, money, noBet)
userChoice = input("What would you like to do? \nPlay \nBet \nQuit \n")
# continuously plays the game, asking the user for their choice until they quit or run out of money
while noAnswer:
  # allows the user to play
  if userChoice.lower() == "play":
    os.system('cls')
    user = int(input("What's your number? (1-5)"))
    print("Generating number"),
    load()
    # unimportant, please ignore
    rig = random.choice(percent)
    if rig <= 3:
      if user == 1:
        spin = 5
      else:
        spin = user - 1
    elif rig <= 9:
      spin = random.choice(roulette)
    else:
      spin = user
    print("\n" + str(spin))
    
    if user == spin:
      print("you win!")
      money += bet
      
    else:
      print("You lose...")
      money -= bet
      
      if money <= 0:
        print("Your out of money, so you REALLY lose! Restart the program to play again.")
        quit()
        
    print("You have $" + str(money))
    print("Your bet is $" + str(bet))
    userChoice = input("What would you like to do? \nPlay \nBet \nQuit \n")
  # allows the user to alter their bet
  elif userChoice.lower() == "bet":
    os.system('cls')
    bet = betting(bet, money, noBet)
    userChoice = input("What would you like to do? \nPlay \nBet \nQuit \n")
  # quits the game
  elif userChoice.lower() == "quit":
    os.system('cls')
    load()
    print("So long!")
    quit()
  # makes sure that the program doesn't crash due to the user choice being misspelled or not existing
  else:
    print("Sorry, that's not a choice on the list.")
    userChoice = input("What would you like to do? \nPlay \nBet \nQuit \n")