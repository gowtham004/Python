yes = True
maximum = 0
bid_store = {}
should_continue = True

print("Welcome to auction")
while should_continue:
    name = input("Enter your name: ")
    bid_price = int(input("How much you like to bid: "))
    bid_store[name] = bid_price
    # print(bid_store)

    should_continue = input("Type \"yes\" to add more bid or \"no\" for result \n").lower()
    if should_continue == "yes":
        should_continue = True
    else:
        should_continue = False
    # print(bid_store)
winner = ""
for name in bid_store:
    check = int(bid_store[name])
    if  check > maximum:
        maximum = check
        winner = name
print(f"The highest bid was {maximum} placed by {winner}")