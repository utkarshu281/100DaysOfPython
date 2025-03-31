print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    bill = 0
    if age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")
        photo = input("Do you want a photo?y for yes and n for no:")
    if photo == "y":
        print("pay extra $3")
        bill = bill+3
        print(f"your total bill is:{bill}")
    else:
        print(f"your total bill is:{bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
