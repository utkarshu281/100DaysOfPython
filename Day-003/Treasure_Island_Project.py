print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
direction = input('You\'re at a cross road. Where do you want to go?\nType "left" or "right":')#u can use single quote if u want double quote on line and \ is an escape seq it escapes the next thing behind it
if direction == "left":
    decide = input("swim or wait for the boat:")
    if decide == "wait":
        door = input("choose a door\n (1)red\n(2)blue\n(3)yellow\n")
        if door == "red":
            print("you are burned by fire")
        elif door == "blue":
            print("you are attacked by monsters")
        elif door == "yellow":
            print("Congratulations!!you found the treasure!!")
        else:
            print("wrong input!game over,idiot")
    elif decide == "swim":
        print("you are attacked by trout")
    else:
        print("wrong input! game over")
elif direction == "right":
    print("you fell in the hole")
else:
    print("wrong input")

print("GAME OVER!!")
