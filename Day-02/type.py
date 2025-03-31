len("12345")
print(type("hello"),"\n",type(1234),"\n",type(3.14),"\n",type(True))# + is not supported for type
#normal
print(type("hello"))
print(type(1234))
print(type(3.14))
print(type(True))
#type conversion
print(int("123")+int("456"))
int()
bool()
str()
float()
#error correction
print("Number of letters in your name: " + str(len(input("Enter your name:"))))
