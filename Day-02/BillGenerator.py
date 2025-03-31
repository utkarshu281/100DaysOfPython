print("Welcome to bill generator!!")
bill = float(input("Tell the total amount of bill($):"))#convert isliye kara kyuki input func hr value ko string leta hai
tip = int(input("how much % tip you want to give:"))
nu = int(input("number of people who are going to split bill:"))

total = round(((bill + (tip/100*bill))/nu), 2)
print(f"your bill is:{total}")

#angela mam code
print("Welcome to bill generator!!")
bill = float(input("Tell the total amount of bill($):"))#convert isliye kara kyuki input func hr value ko string leta hai
tip = int(input("how much % tip you want to give:"))
nu = int(input("number of people who are going to split bill:"))
tip_as_percent = tip/100
total_tip_amount = bill*tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill/nu
final_amount = round(bill_per_person,2)
print(f"the final amount each person should pay:{final_amount}")
