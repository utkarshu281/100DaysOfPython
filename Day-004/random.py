import random
import my_module
random_number = random.randint(1,10)
print(random_number)
print(my_module.my_number)
random_nu = random.random()*10
print(random_nu)
random_nu = random.random()
print(random_nu)
random_float = random.uniform(1,10)
print(random_float)

coin = random.randint(1,2)
if coin == 1:
    print("tails")
else:
    print("heads")
