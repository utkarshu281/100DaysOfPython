gg=input("What is your name?")
print("hello " + gg + " the number of char in your name is: ", len(gg))
# my attempt
# The walrus operator (:=) is a Python assignment expression operator introduced in Python 3.8. It allows you to assign a value to a variable while using it inside an expression.
# variable := expression
print("hello " + (gname := input("write your name\n")) + " the number of char in your name is: " + str(len(gname)))
# angela mam
print(len(input("whats your name handsome:")))
