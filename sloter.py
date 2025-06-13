import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count={
    "🏅": 2,
    "🥇": 4,
    "🥈": 6,
    "🥉": 8,
}

symbol_value = {
    "🏅": 5,
    "🥇": 4,
    "🥈": 3,
    "🥉": 2,
}

def for_winnings(columns, lines, values, bet):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break 
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_spin(rows, cols, symbols):
    all_symbols= []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns =[]
    for _ in range (cols):
        column=[]
        current_symbols = all_symbols [:]
        for _ in range (rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

def print_columns(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount=input("enter the value of your wallet, in order to bet :")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0.")
        else:
            print("please enter a number.")

    return amount

def number_of_lines():
    while True:
        lines=input("enter the lines(1-" + str(MAX_LINES) + ")? to bet on the roller of 3 matches ")
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("please enter valid number of lines from 1 to 3.")
        else:
            print("please enter a number.")

    return lines

def input_bet():
    while True:
        amount=input("bet on each line:")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be between {MIN_BET}rs - {MAX_BET}rs.")
        else:
            print("please enter a number.")

    return amount

def spin(balance):
     lines= number_of_lines() 

     while True:
       bet=input_bet()
       total_bet= (bet*lines)

       if total_bet > balance:
                print(f"you do not have enough to bet that amount, your current balance is {balance}rs")
       else:
            break

     print(f"you arre betting {bet}rs on {lines} lines. Total bet is equal to: {total_bet}rs. ")

     slots=get_slot_spin(ROWS, COLS, symbol_count)
     print_columns(slots)
     winnings, winning_lines = for_winnings(slots, lines, symbol_value, bet)

     print (f"you won {winnings}rs.")
     print (f"you won on lines:", *winning_lines)
     return  winnings - total_bet


def game():
    balance=deposit()
    while True:
        print(f"current balance is {balance}rs")
        answer = input ("press enter to spin (q to quit)")
        if answer == "q":
            break
        balance += spin (balance)
        if balance < MIN_BET:
          print("You don't have enough balance to spin. Game over.")
          break

       
    

    print(f"you left with {balance}rs")

game()
    