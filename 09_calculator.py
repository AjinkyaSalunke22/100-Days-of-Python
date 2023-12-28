# Author: Ajinkya Salunke
# Date: 28/12/2023 

# Importing OS to clear the screen after the repetative operation
import os

# Art
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# printing art
print(logo)

# Calculator operation functions
# Function to add two numbers
def add(n1, n2):
    return n1+n2

# Function to substract two numbers
def sub(n1, n2):
    return n1-n2

# Function to multiply two numbers
def mul(n1, n2):
    return n1*n2

# Function to divide two numbers
def divide(n1, n2):
    return n1/n2

# Calculator function
def calc(n1 = "",n2= ""):
    # Asking user to select the operation and enter the numbers.
    operation = input("Please select the operation: +, -, *, /.\n")

    # Taking the input if n1 is null othersie only asking for the second value
    if n1 == "":
        n1 = int(input("Enter the first number: \n"))    
    n2 = int(input("Enter the second number: \n"))

    # Calling the desired function based on user's action
    if operation == '+':
        cur_res = add(n1,n2)
    elif operation == "-":
        cur_res = sub(n1,n2)
    elif operation == "*":
        cur_res = mul(n1,n2)
    elif operation == "/":
        cur_res = divide(n1,n2)
    # exception handling
    else:
        print("Provide a correct input.")
        exit()

    # Printing the result
    print(f"The total of your operation is:{cur_res}")

    # Asking user to continue callculatioon or start a new one
    operation_continue = input("Do you want to continue this transaction ? 'y' or 'n'. \n")

    # creating a loop for user's permission
    if operation_continue == 'y':
        os.system('cls')
        calc(n1 = cur_res)
    else:
        print(f"The total of your operation is:{cur_res}")

# Calling the calculator function
calc()  