print("Welcome to treasure Island.\nYour mission is to find the treasure.")

if ("left" == input("You are at cross road, Where do you want to go? Type left or right.\n").lower()):
    if ("wait" == input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait ot type 'swim' to swim.\n").lower()):
        if ("yellow" == input("you arrieved at the island unharmed. There is a house with 3 doors, One is red, one is yellow and one is blue. Which color do you choose ?\n").lower()):
            print("You Win !!!")
        else:
            print("you entered into the room of ghosts.")
    else:
            print("you have been eaten by the crocodile.")
else:
    print("You hit by the car.")
    print("Game Over")