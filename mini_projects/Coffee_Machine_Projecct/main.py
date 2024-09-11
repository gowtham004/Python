from ingredients import coffee_recipie, storage

is_on = True
profit = 0
def power_off():
    global is_on
    is_on = False
    return is_on

# Get coffee choice
def get_coffee_choice():
    print("Hello, what would you like to have?\n")
    print('Press \'1\' for latte\nPress \'2\' for cappuccino\nPress \'3\' for espresso\n')
    initial_input = input()
    if initial_input == "Off The Machine":
        return power_off()
    elif initial_input == "Report":
        report(),profit_money()
        return None
    else:
        try:
            chose_coffee = int(initial_input)
            if chose_coffee in [1, 2, 3]:
                return chose_coffee
            else:
                print("Invalid choice. Please try again.")
                return get_coffee_choice()
        except ValueError:
            print("!!!INVALID INPUT!!! Please enter a valid choice.")
            return get_coffee_choice()
#Profit
def profit_money():
    print(f"profit: ${profit}")
# Report the current storage
def report():
    print("Current storage status:")
    for key, value in storage.items():
        print(f"{key}: {value}ml")
    return storage

# Check if the requirements are sufficient in the storage
def check_storage(milk_used, water_used, coffee_powder_used):
    if storage["milk"] >= milk_used and storage["water"] >= water_used and storage["coffee"] >= coffee_powder_used:
        return True
    else:
        return False

# Process coins
def process(coffee_cost):
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    print("Insert coins")

    try:
        quarter_count = int(input("How many quarters: "))
        dime_count = int(input("How many dimes: "))
        nickel_count = int(input("How many nickels: "))
        pennies_count = int(input("How many pennies: "))

        value = (quarter_count * quarters) + (dime_count * dimes) + (nickel_count * nickles) + (pennies_count * pennies)
        print(f"Total inserted value: ${round(value, 2)}")

        balance = value - coffee_cost

        if balance > 0:
            print(f"Take your balance: ${round(balance, 2)}")
            return True
        elif balance == 0:
            print("Thanks for the exact change.")
            return True
        else:
            print("Not enough coins. Transaction failed.")
            print("Money Refunded!!!")
            return False

    except ValueError:
        print("Invalid number. Please try again.")
        return process(coffee_cost)

# Prepare coffee and reduce the storage
def prepare_coffee(milk_need, water_need, coffee_powder_need):
    storage["milk"] -= milk_need
    storage["water"] -= water_need
    storage["coffee"] -= coffee_powder_need
    print("Here is your coffee. Enjoy!")

# profit


# Main program
while is_on:
    chosen_coffee = get_coffee_choice()
    if chosen_coffee is None:
        continue
    if not is_on:
        break
    coffee = coffee_recipie[chosen_coffee - 1]
    coffee_cost = coffee["rate"]
    print(f"{coffee['name']} costs ${coffee_cost}")

    milk_used = coffee["milk"]
    water_used = coffee["water"]
    coffee_powder_used = coffee["coffee"]
    profit += coffee_cost
    if check_storage(milk_used, water_used, coffee_powder_used):
        if process(coffee_cost):
            prepare_coffee(milk_used, water_used, coffee_powder_used)
            print("Here is your coffee\nHave a nice day!!!")
        else:
            print("Transaction failed.")
    else:
        print("Not enough resources.")

