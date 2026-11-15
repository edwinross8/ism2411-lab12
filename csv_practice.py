# LAB 12

# Author: Edwin Ross
# 11 / 09 / 2026

import csv

from datetime import datetime 

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"


print("EXERCISE 1")

with open(SALES_FILE, "r") as f:
    print("Sales file opened successfully!")

print("EXERCISE 2")

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)



print("EXERCISE 3")

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(f"Header: {header}")
    for row in reader:
        print(row)

