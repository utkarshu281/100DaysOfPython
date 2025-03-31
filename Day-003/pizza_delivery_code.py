print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "S":
    bill = 15
    print("price is $15")
    sp = input("Do you want pepperoni, y for yes and n for no:")
    if sp == "y":
       bill = bill + 2
    sc = input("Do you want cheese, y for yes and n for no:")
    if sc == "y":
       bill = bill + 1
    print(f"your total bill is:{bill}")
elif size == "M":
    bill = 20
    print("price is $20")
    mp = input("Do you want pepperoni, y for yes and n for no:")
    if mp == "y":
        bill = bill + 3
    mc = input("Do you want cheese, y for yes and n for no:")
    if mc == "y":
        bill = bill+1
    print(f"your total bill is:{bill}")
elif size == "L":
     bill = 25
     print("price is $25")
     lp = input("Do you want pepperoni, y for yes and n for no:")
     if lp == "y":
        bill = bill + 2
     lc = input("Do you want cheese, y for yes and n for no:")
     if lc == "y":
        bill = bill + 1
     print(f"your total bill is:{bill}")


