

bids = {}
continue_bidding = True

print("Welcome to the secret auction program.")

def check_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = None
    for bidder in bidding_dictionary:
        if bids[bidder] > highest_bid:
            highest_bid_amount = bids[bidder]
            highest_bidder_name = bidder

    print(f"The auction winner is {winner} with the bidding amount of $ {highest_bid}")

while continue_bidding:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $ "))
    bids[bidder_name] = bid_amount
    print(bids)

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if should_continue == "no":
        continue_bidding = False
        check_highest_bidder(bids)

    else:
       print("\n" * 50)






