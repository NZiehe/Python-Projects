MAX_LINES = 3
MAX_BET = 5000
MIN_BET = 10

# function gets a deposit as input from the user
def deposit():
    while True:
        amount = input("What would you like to deposit? $: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0!")
        else:
            print("Please enter a number!")
    return amount

# get the number on lines the user want to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter a valid number of lines!")
        else:
            print("Please enter a number!")
    return lines

# get the amount of money he want to bet
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? MAX: " + str(MAX_BET) + "$, MIN: " + str(MIN_BET) + "$ : ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Bet must be between MAX: " + str(MAX_BET) + "$, MIN: " + str(MIN_BET) + "$ : ")

        else:
            print("Please enter a number!")

    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()

    print(balance, lines)

main()