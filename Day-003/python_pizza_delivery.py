#my code
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total = 0
if size == "S":
    total = 15
elif size == "M":
    total = 20
elif size == "L":
    total = 25
else:
    print("what do you want")
if pepperoni == "y"and size == "S":
    total+=2
elif pepperoni == "y" and (size == "M" or size == "L"):
    total+=3

if extra_cheese == "y":
    total+=1
print(f"Your final bill is: ${total}.")
#angela mam solution
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "S":
    bill+= 15
elif size == "M":
     bill+= 20
elif size == "L":
     bill+= 25
else:
    print("what do you want")
if pepperoni == "Y":
    if size == "S":
        bill+=2
    else:
        bill+=3

if extra_cheese =="Y":
    bill+=1

print(f"Your final bill is: ${bill}.")
