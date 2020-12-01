print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print("You are arriving in junction. Turn left or right? ")
answer = input().lower()

if answer == 'left':
  print("You turned left. You walked through a jungle and approached a river.")
  print("Swim or wait?")
  answer = input().lower()
  if answer == 'wait':
    print("You waited and looked around. You saw a house. You walked to the house and found three doors.")
    print("Their colors are red, yellow and blue. Which one you choose? ")
    answer = input().lower()
    if answer == 'yellow':
      print("You entered the yellow door and found the tressure. You win!")
    elif answer == 'red':
      print("You entered the red door and exposed to a huge fire.")
      print("You burned by fire. Game over.")
    elif answer == 'blue':
      print("You entered blue door. Behind the door there was a giant beast with massive teeth.")
      print("You were eaten by the beast. Game over")
    else:
      print("You did not enter the house and walked around the house. A giant eagle attacked you. Game over.")
  else:
    print("You tried to swim across the river. But a killer crocodile came and attacked you. Game over.")
else:
  print("You walk to the right and fall into a hole. Game over")
