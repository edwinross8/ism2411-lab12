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

print("EXERCISE 4")

total_revenue = 0

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total Revenue: ${total_revenue:.2f}")


print("---Exercise 5---")

high_value = []
rows_read = 0

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header

    for row in reader:
        rows_read += 1
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity

        if total > 100:
            high_value.append([product, f"{price:.2f}", quantity, f"{total:.2f}"])

with open(CLEANED_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    writer.writerows(high_value)

print(f"Rows read: {rows_read}")
print(f"Rows written: {len(high_value)}")

print("---Exercise 6---")

dict_total = 0

with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total += total

        print(f"{row['product']}: ${total:.2f}")

print(f"Total Revenue: ${dict_total:.2f}")

# csv.reader is good for when you know the position of each column
# csv.DictReader is better when you want to access columns by name