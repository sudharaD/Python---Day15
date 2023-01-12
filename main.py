from resources import INGREDIENT, MENU, IMOJI

PROFIT = 0
IS_TURNED_OFF = False

while not IS_TURNED_OFF:

    # TODO: 1. Check the user’s input to decide what to do next.
    answer = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: Resource checker function
    def resource_checker(drink, ingredient, menu, imoji, profit):

        # TODO: 2. Check transaction successful?
        # TODO: Check that the user has inserted enough money to purchase the drink they selected
        def process_coins():
            # TODO: 1.3. If there are sufficient resources to make the drink
            # TODO: program should prompt the user to insert coins
            print("Please insert coins")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            return quarters * 0.25 + dimes * 0.10 + nickles * 0.5 + pennies * 0.01

        def profit_and_resource_handler(p, i):
            i["water"] -= menu[drink]["ingredients"]["water"]
            i["milk"] -= menu[drink]["ingredients"]["milk"]
            i["coffee"] -= menu[drink]["ingredients"]["coffee"]
            i["money"] = p

        if ingredient["water"] >= menu[drink]["ingredients"]["water"] and ingredient["milk"] >= menu[drink]["ingredients"]["milk"] and ingredient["coffee"] >= menu[drink]["ingredients"]["coffee"]:
            total = process_coins()
            charge = menu[drink]["cost"]
            profit += charge
            if total <= charge:
                # TODO: If it is not enough refund the money
                print("Sorry, that's not enough money. Monet refunded.")
            else:
                # TODO: If it enough -  ingredients to make the drink should be deducted. Give item to customer

                profit_and_resource_handler(profit, ingredient)

                print(f"Here ${total - charge} in change.")
                print(f"Here is your {drink} {imoji[drink]}. Enjoy!")
        # TODO: If resources not enough - It should not continue to mak ethe drink but print: “Sorry there is not enough water.”
        else:
            print("Sorry there is not enough water.")

        return profit

    # TODO: 1.1. When the user enters “report” to the prompt, a report should be generated
    if answer == "report":
        print(INGREDIENT)
    elif answer == "finish":
        IS_TURNED_OFF = True
    else:
        # TODO: 1.2. When the user chooses a drink, the program should check if there are enough resources to make that drink.
        PROFIT = resource_checker(answer, INGREDIENT, MENU, IMOJI, PROFIT)

    # TODO: Process coins function - (Create dictionary for hold the coin values)
    # TODO: 3. Profit and Balance Handle
    # TODO: Cost of the drink gets added to the machine as the profit
    # TODO: If the user has inserted too much money, the machine should offer change.
    # TODO: 4. Repeat this process
    # TODO: The prompt should show again to serve the next customer
    # TODO: Turn off the Coffee Machine by entering “off”.
