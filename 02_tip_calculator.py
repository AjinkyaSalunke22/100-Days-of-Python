total_bill = float(input("What was the total bill? \n"))
tip = float(input("What percentge tip would you like to give? 10, 12, 15? \n"))
no_of_people = int(input("How many people to split the bill? \n"))

tip = total_bill*(tip/100)

total_bill = total_bill + tip

split = total_bill/no_of_people

split = round(split,2)

print(f"Each person should pay: ${split}.")