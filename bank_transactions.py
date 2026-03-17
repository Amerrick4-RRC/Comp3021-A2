"""
Description: Simulated bank teller.
Author: Andrew Merrick
Date: 23-10-2
Usage: for instructor assessment of given material
"""

from random import randint

import os

from time import sleep

# relatable objects
user_function_choice = ["D", "W", "Q"]

user_current_balance = randint(-1000, 10000)

user_current_balance = float(user_current_balance)

TERMINAL_WIDTH = 40

linebreak = ("*".center(TERMINAL_WIDTH, "*"))

# Base program
quit_confirmation = False
sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

# Display
while not quit_confirmation:
    print(linebreak, '\n', "PIXELL RIVER FINANCIAL".center(TERMINAL_WIDTH),
          '\n',"ATM Simulator".center(TERMINAL_WIDTH), '\n',
          f"Your current balance is: ${user_current_balance:,.2f}".center(40),
          '\n', "Deposit: D".center(TERMINAL_WIDTH), '\n',
          "Withdraw: W".center(TERMINAL_WIDTH), '\n',
          "TO Quit: Q".center(TERMINAL_WIDTH), '\n', linebreak)
    
# User selection
    user_selection = input("Enter your selection: ")
    user_selection = user_selection.upper()

    if user_selection == 'Q':
         quit_confirmation = True

    elif user_selection not in user_function_choice:
            print(linebreak, '\n',
                  "INVALID SELECTION".center(TERMINAL_WIDTH),
                  '\n', linebreak)
            
# Given transaction            
    elif user_selection in user_function_choice:
        transaction = input("Enter amount of transaction: ")
        transaction = float(transaction)

        if user_selection == 'D':
            user_current_balance += transaction

        elif user_selection == 'W':
            if transaction > user_current_balance:
                    print(linebreak, '\n', 
                          "INSUFFICIENT FUNDS".center(TERMINAL_WIDTH),
                          '\n', linebreak)
                    
            else:
                 user_current_balance -= transaction
                 
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
        
sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
