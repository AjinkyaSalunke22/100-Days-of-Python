import os

os.system('cls')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bids = []
other_bidder = "y"

while (other_bidder == "y"):
    print("Welcome to the secret auction program.")
    bidder_details = {}
    name = input("What is your name ?\n")
    bidder_details["Name"] = name
    bid = int(input("What is your bid?\n"))
    bidder_details["bid"] = bid
    other_bidder = input("Are there other bidders? Type 'y' ot 'n'. \n")
    bids.append(bidder_details)

    if other_bidder == 'y':
        os.system('cls')
    elif other_bidder == 'n':
        print("Thank you for bidding.\n")

for i in range(0, len(bids)):
    max_bid = 0
    if bids[i]["bid"] > max_bid:
        max_bid = bids[i]["bid"]
        bidder = bids[i]["Name"]

print("Maximun bid is &", max_bid, "and the bidder name is:", bidder, ".")