import random
import time
import os
# EXPERIMENTAL
# import sandwichOrder

wheel = [1, 2, 3, 4, 5]
percent = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
noAnswer = True
noBet = True
dialog = 2
bet = 0
spin = 0
rig = 0
user = 0
money = 1000
os.system('cls')
print("Welcome to...")
time.sleep(dialog)
print("SPIN")
time.sleep(1)
print("THAT")
time.sleep(1)
print("WHEEL!")
time.sleep(1)
input("( ͡° ͜ʖ ͡°) <(lmao)\nThe game show where you always loose! Isn't that fun?!?! (press enter to continue through dialog)")
os.system('cls')
input("( ͡~ ͜ʖ ͡° ) <(hola$)\nHi, I'm Lenny and I'll be your host tonight!")
os.system('cls')
input("( ͡• ͜ʖ ͡• ) <(deli$iou$)\nNow, the way this works is you bet money, and then you will be offered the choice of playing or adjusting your bet.")
os.system('cls')
input("( ͠° ͜ʖ ͡°) <($?)\nIf you play, you will be asked to select a number between 1 and 5.")
os.system('cls')
input("(  • ͜ʖ • ) *lying*\nThen the computer will select a completely not at all rigged or manipulated in any way number guarenteed fair by our sponsers and paid lawyers who also are legit and totally not like the guy who sold me 'magic' hairspray the set my hair on fire and now I have no hair.")
os.system('cls')
input("(。＿。)\n...")
os.system('cls')
input("('￣▽￣) <(heh)\nANYWAY let's move on to betting")
os.system('cls')
input("( ͡• ͜ʖ ͡• )\nSo then the computer will ask you to bet money.")
os.system('cls')
input("( ͡~ ͜ʖ ͡°)\nRemember that you can't bet more than you have! That's cheating and also called going into debt!")
os.system('cls')
input("( ° ͜ʖ °)\nLet's get into it!")
os.system('cls')
# sets and tracks the user's bet, preventing them from betting something
# they can't and warning them if they bet really high
def betting(bet, money, noBet):
  while noBet:
    bet = int(input("$(*￣▽￣*)$ <(alot plea$e)\nHow much would you like to bet in $? (Numbers only, no cents)"))
    os.system('cls')
    # EXPERIMENTAL
    # if type(bet) == :
    #   print("You can't bet that")
    #   noBet = True
    if bet > money:
      input("(╯°□°）╯︵ ┻━┻ <(WHATDIDI$AYEARLIER)\nYou can't bet that much")
      os.system('cls')
      noBet = True
    elif bet == money:
      input("(⊙ ˍ⊙ )\nWarning: You will have to restart if you lose with this bet, change your bet if this was a mistake.")
      os.system('cls')
      noBet = False
      input("( ͡• ͜ʖ ͡• ) <(deli$iou$)\nYou bet $" + str(bet))
      os.system('cls')
      return bet
    elif bet < 0:
      input("( -___-) <(um no)\nYou can't have a negative bet")
      os.system('cls')
      noBet = True
    elif bet == 69:
      noBet = False
      input("( ͡' ︶ ͡' ) <(nice)\nYou bet $" + str(bet))
      os.system('cls')
      return bet
    else:
      noBet = False
      input("( ͡~ ͜ʖ ͡°) <(kool)\nYou bet $" + str(bet))
      os.system('cls')
      return bet
  noBet = False
# creates a mini loading animation
def load():
  sym = [".", ".", "."]
  for i in range(3):
    print(sym[i]),
    time.sleep(.5)
# initiates the game
input("( ͡• ͜ʖ ͡• ) <(deli$iou$)\nYou have $" + str(money) + "")
os.system('cls')
bet = betting(bet, money, noBet)
userChoice = input("(。＿。) <(dont we have mu$ik 4 waiting or $mth...)\nWhat would you like to do? \nPlay \nBet \nQuit \n")
os.system('cls')
# continuously plays the game, asking the user for their choice until they quit or run out of money
while noAnswer:
  # allows the user to play
  if userChoice.lower() == "play":
    os.system('cls')
    user = int(input("(⊙ ͜ʖ⊙ ) <(oooooooo watcha gonna chuu$e?)\nWhat's your number? (1-5)"))
    os.system('cls')    
    print("(。_。) <(i cant count)\nGenerating number"),
    load()
    os.system('cls')
    # (👉ﾟヮﾟ)👉 unimportant, plea$e ignore
    rig = random.choice(percent)
    if rig <= 3:
      if user == 1:
        spin = 5
      else:
        spin = user - 1
    elif rig <= 9:
      spin = random.choice(wheel)
    else:
      spin = user
    print("\n" + str(spin))
    
    if user == spin:
      input("┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻ <(ANDTHEREGOE$OURMARKETINGPLOYWHEREYOUNEVERWIN)\nYou win!")
      os.system('cls')
      money += bet
      
    else:
      input("○( ＾皿＾)っ <(kek)\nYou lose...")
      os.system('cls')
      money -= bet
      
      if money <= 0:
        input("( ͡~ ͜ʖ ͡°) <(deli$iou$ [[MONEIE$]] now get out and go to jail or $mth)\nYour out of money, so you REALLY lose! Restart the program to play again.")
        quit()
        
    print("( ͡• ͜ʖ ͡• ) <(deli$iou$)\nYou have $" + str(money) + "")
    input("\nYour bet is $" + str(bet))
    os.system('cls')
    userChoice = input("( ͡~ ͜ʖ ͡°) <(PRO TIP: $aying [[HYPERLINK BLOCKED]] in cla$$ i$n't nice, you [[LITTLE $PONGE]]!)\nWhat would you like to do? \nPlay \nBet \nQuit \n")
  # allows the user to alter their bet
  elif userChoice.lower() == "bet":
    os.system('cls')
    bet = betting(bet, money, noBet)
    userChoice = input("(._. ) <($o, u doin anything later or are u ju$t gonna play thi$ forever)\nWhat would you like to do? \nPlay \nBet \nQuit \n")
  # starts the order function
    # EXPERIMENTAL:
    # elif userChoice.lower() == "order":
    #   sandwichOrder.orderFood
  # quits the game
  elif userChoice.lower() == "quit":
    os.system('cls')
    print("(• ͟ʖ •) <(wait, wut)")
    load()
    time.sleep(dialog)
    os.system('cls')
    print("(°ロ° ) <(NO)\nThank you so much for playing my game!")
    time.sleep(dialog)
    os.system('cls')
    print("(ʘДʘ) <(№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№)\nShutting down in 3...")
    time.sleep(dialog)
    os.system('cls')
    print("┻━┻ ︵ヽ( ◴  Д  ◷ )ﾉ︵ ┻━┻ <(ŢĦÆʎ Ð|Ď₦Ŧ Ͳ⨊⌊Ĺ ℳĚ ₸HΑΤ ὟὌ⨆ Ⅽ○ύἰↇ Ϳ⩂Ϟ⫟ QUIT‼?⁇⁈¿!‼‽⸘¿¡‽:‼¡⁈⁇¿¿!⁈‼⸘¿¿)\nShutting down in 2...")
    time.sleep(dialog)
    os.system('cls')
    print("ﾉ( ಥ Д ಥ)ﾉ <(IMMELTINGIMMELTINGOHWHATAWORLDWHATAWOLRD)\nShutting down in 1...")
    time.sleep(dialog)
    os.system('cls')  
    print("X﹏X ded...\nSee you later!")
    time.sleep(1)
    os.system('cls')
    quit()
  # makes sure that the program doesn't crash due to the user choice being misspelled or not existing
  else:
    print("(ㆆ_ㆆ ) <(r u leik, [[DYS$FUNCTION IN THE GRAY MATTER]] or $mth?)\nSorry, that's not a choice on the list.")
    time.sleep(dialog)
    os.system('cls')
    userChoice = input("( ㆆ_ㆆ) <(Oor do you ju$t need reading gla$$e$)\nWhat would you like to do? \nPlay \nBet \nQuit \n")
    os.system('cls')