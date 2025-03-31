print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("write your age:"))
    if age<=18 and age>=12:
        print("your fare is $18")
    elif age<12:
        print("your fair is $7!little man")
    elif age<=30:
        print("you fair is $20 ")
    else:
        print("your are too old for this shit!!Anyways your fair is $25")
else:
    print("Sorry you have to grow taller before you can ride.")
