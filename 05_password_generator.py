import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
pass1 = []
pass2 = []
pass3 = []

for _ in range(0, nr_letters):
    i = random.randint(0, len(letters)-1)
    pass1.append(letters[i])

for _ in range(0, nr_symbols):
    i = random.randint(0, len(symbols)-1)
    pass2.append(symbols[i])

for _ in range(0, nr_numbers):
    i = random.randint(0, len(numbers)-1)
    pass3.append(letters[i])



rand_pass = []
for _ in range(0, nr_letters):
    rand_1 = random.randint(0, len(pass1)-1)
    rand_2 = random.randint(0, len(pass2)-1)
    rand_3 = random.randint(0, len(pass3)-1)

    rand_pass.append(pass1[rand_1])
    rand_pass.append(pass2[rand_2])
    rand_pass.append(pass3[rand_3])

passs = "".join(rand_pass)

print("Your password is:", passs)