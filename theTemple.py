import os
import time

os.system('cls')
noAnswer = True
user = "What is your answer?"
choices = ["a", "b", "c", "d"]
answer = 0
entered = ""
question = ""
correct = True
score = 7
response = ""
print("  _______ _            _______                   _      \n |__   __| |          |__   __|                 | |     \n    | |  | |__   ___     | | ___ _ __ ___  _ __ | | ___ \n    | |  | '_ \ / _ \    | |/ _ \ '_ ` _ \| '_ \| |/ _ \ \n    | |  | | | |  __/    | |  __/ | | | | | |_) | |  __/ \n    |_|  |_| |_|\___|    |_|\___|_| |_| |_| .__/|_|\___| \n                                          | |           \n                                          |_|           ")
input("                   Press Enter to begin")
time.sleep(.75)
os.system('cls')
print("Here's how the game works. You will be given a question and must answer a, b, c, or d.\nPress enter to submit it, and only answer the options provided.")
time.sleep(4)
os.system('cls')

while noAnswer:
  print("Question 1\nWhat was the signifigance of the temple?")
  print("a. It was God's physical presence on Earth")
  print("b. It was where they stored their gold")
  print("c. It was Jesus' crib")
  print("d. It was on huge convoluted bathroom")
  entered = input(user)
  
  if entered.lower() == "a":
    print("Correct!")
    time.sleep(.75)
    os.system('cls')
    noAnswer = False
        
  elif entered.lower() in choices:
    print("Incorrect.")
    score -= 1
    time.sleep(.75)
    os.system('cls')
    noAnswer = False
        
  else:
    print("That's not one of the answers.")
    time.sleep(.75)
    os.system('cls')
    noAnswer = True
    
noAnswer = True
while noAnswer:
  print("Question 2\nWhat did Jesus mean in John 2:19?")
  print("a. He was REALLy fast at building")
  print("b. He had magic")
  print("c. He was alluding to himself and his death")
  print("d. He was daring them to try")
  entered = input(user)
  
  if entered.lower() == "c":
    print("Correct!")
    time.sleep(.75)
    os.system('cls')
    noAnswer = False
        
  elif entered.lower() in choices:
    print("Incorrect.")
    score -= 1
    time.sleep(.75)
    os.system('cls')
    noAnswer = False
        
  else:
    print("That's not one of the answers.")
    time.sleep(.75)
    os.system('cls')
    noAnswer = True
    
noAnswer = True
while noAnswer:
  print("Question 3\nWHat does the cornerstone represent in Matthew 21:42?")
  print("a. John the Baptist")
  print("b. Jesus")
  print("c. People rejected by society")
  print("d. The Pharisees")
  entered = input(user)
  
  if entered.lower() == "c":
    print("Correct!")
    time.sleep(.75)
    os.system('cls')
    noAnswer = False
        
  elif entered.lower() in choices:
    print("Incorrect.")
    score -= 1
    time.sleep(.75)
    os.system('cls')
    noAnswer = False
        
  else:
    print("That's not one of the answers.")
    time.sleep(.75)
    os.system('cls')
    noAnswer = True
    
noAnswer = True
while noAnswer:
  print("Question 4\nDid Jesus' prediction about the temple being destroyed come true?")
  print("a. No")
  print("b. Yes")
  entered = input(user)
  
  if entered.lower() == "b":
    print("Correct!")
    time.sleep(.75)
    os.system('cls')
    noAnswer = False
        
  elif entered.lower() == "a":
    print("Incorrect.")
    score -= 1
    time.sleep(.75)
    os.system('cls')
    noAnswer = False
        
  else:
    print("That's not one of the answers.")
    time.sleep(.75)
    os.system('cls')
    noAnswer = True
    
noAnswer = True
while noAnswer:
  print("Question 5\nWhat caused Jesus to overthrow the tables of the merchants in the temple?")
  print("a. Greed")
  print("b. He was a carpenter and he hated the poor craftsmenship of their tables")
  print("c. He really had to pee")
  print("d. The same reason Mr. Teeter throws things at people who aren't respectful, righteous anger")
  entered = input(user)
  
  if entered.lower() == "d":
    print("Correct!")
    time.sleep(.75)
    os.system('cls')
    noAnswer = False
        
  elif entered.lower() in choices:
    print("Incorrect.")
    score -= 1
    time.sleep(.75)
    os.system('cls')
    noAnswer = False
        
  else:
    print("That's not one of the answers.")
    time.sleep(.75)
    os.system('cls')
    noAnswer = True
while noAnswer:
  print("Question 6\nWhat did Jesus reveal to Nicodemus??")
  print("a. How to be redeemed")
  print("b. How to become God")
  print("c. The Crappy Patty formula")
  print("d. Hand Sanitizer that kills 100% of germs")
  entered = input(user)
  
  if entered.lower() == "a":
    print("Correct!")
    time.sleep(.75)
    os.system('cls')
    noAnswer = False
        
  elif entered.lower() in choices:
    print("Incorrect.")
    score -= 1
    time.sleep(.75)
    os.system('cls')
    noAnswer = False
        
  else:
    print("That's not one of the answers.")
    time.sleep(.75)
    os.system('cls')
    noAnswer = True
    
noAnswer = True
while noAnswer:
  print("Question 7\nWho did Jesus come to save??")
  print("a. The puppies")
  print("b. The Jews")
  print("c. The holy people")
  print("d. All who accept his gift of eternal life")
  entered = input(user)
  
  if entered.lower() == "d":
    print("Correct!")
    time.sleep(.75)
    os.system('cls')
    noAnswer = False
        
  elif entered.lower() in choices:
    print("Incorrect.")
    score -= 1
    time.sleep(.75)
    os.system('cls')
    noAnswer = False
        
  else:
    print("That's not one of the answers.")
    time.sleep(.75)
    os.system('cls')
    noAnswer = True
noAnswer = True

while noAnswer:
  print("Bonus Question!\nWhat...is the airspeed velocity of an unladen swallow?")
  print("a. 90 mph")
  print("b. African or European swallow?")
  print("c. Green")
  print("d. 87 tea bags per controlled colony or something, I'm not British")
  entered = input(user)
  
  if entered.lower() == "b":
    print("What? I don't knowAUUGHHHHHHHH!")
    score += 1
    time.sleep(.75)
    os.system('cls')
    noAnswer = False
        
  elif entered.lower() in choices:
    print("Incorrect!")
    time.sleep(.75)
    os.system('cls')
    noAnswer = False

print("Your score is...\n")
time.sleep(0.75)
print(str(score) + "!")