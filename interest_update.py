"""
Description: Update accounts for monthly interest from a txt file.
Author: Andrew Merrick
Date: 23-10-2
Usage: for instructor assessment of given material.
"""
import csv

from csv import DictReader

from csv import DictWriter

from pprint import pprint

file_input = {}

accounts = "account_balances.txt"


with open(accounts) as file:
    file_count = len(file.readlines())
    line_count = 0

if line_count < file_count:
    with open(accounts) as update:
        for line in update:
           number,balance = line.rstrip('\n').split('|')
           file_input[number] = [balance]
           line_count += 1

    pprint(file_input)
 
for number, balance in file_input.items():

    amount = balance[0]
    amount = float(amount)

    if amount < 1000:
        balance = amount + ((amount * .01) / 12)

    elif amount >= 1000 and amount < 5000:
        balance = amount + ((amount * .025) / 12)

    elif amount >= 5000:
        balance = amount + ((amount * .5) / 12)

    else:
        balance = amount - ((amount * .1) / 12)

    file_input[number] = balance

pprint(file_input)

output_file = "2023-10-02-AM.csv"

field_names = ["Account", "Balance"]

with open("2023-10-02-AM.csv", 'w', newline = '') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    for account, balance in file_input.items():
        writer.writerow({"Account": account, "Balance" : balance})

with open("2023-10-02-AM.csv", 'r', newline = '') as file:
    reader = csv.DictReader(file)
    for line in reader:
        print(line)