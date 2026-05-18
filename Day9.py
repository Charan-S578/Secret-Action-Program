# Python Dictionaries
#programming_dictionary = {
#    "Bug": "An error in a program that prevents the program from running as expected",
 #   "Function": "A piece of code that you can easily call over and again and again.",
#}

#print(programming_dictionary["Function"])

# Adding a new dictionary

#programming_dictionary["loop"] = "The action of doing something over and over again."

#print(programming_dictionary)

# Wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

# Edit an item in a dictionary
#programming_dictionary["Bug"] = "A moth in your computer."
#print(programming_dictionary)

# Loop through a dictionary
#for key in programming_dictionary:
#    print(key)
#    print(programming_dictionary[key])

# Python Nesting

#capitals = {
 #   "France": "Paris",
 #   "Germany": "Berlin"
#}

# Nested list in Dictionary

#travel_log = {
#    "France": ["Paris", "Lille", "Dijoin"],
 #   "Germany": ["Stuttgart", "Berlin"],
#}

# Print Dijoin
#print(travel_log["France"][2])

#nested_list = ["A", "B", ["C", "D"]]
#print(nested_list[2][1])

#travel_log = {
 #   "France": {
 #       "cities_visited": ["Paris", "Lille", "Dijoin"],
 #       "number_of_times_visited": 8
 #   },
 #   "Germany": {
  #      "cities_visited": ["Stuttgart", "Berlin", "Hamburg"],
  #      "number_of_times_visited": 12
  #  },
#}

#print(travel_log["France"]["cities_visited"][2])

# Day 9 Project Blind Auction Project

# TODO-1: Ask the user for input

# TODO-2: Save data into dictionary {name: price}

# TODO-3: Whether if new bids need to be added

# TODO-4: Compare bids in dictionary

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder



    print(f"The winner is {winner} with a bid of ${highest_bid}.")        


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)   