"""
CP1404/CP5632 - Practical
Shop Calculator Program
By Hexon Hartley Jimenez
"""
DISCOUNT = 0.10
total_price = 0

number_of_items = int(input("Enter number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Enter number of items: "))

for item in range(number_of_items):
    price_of_items = float(input(f"Enter price of item {item + 1}: $"))
    total_price += price_of_items

if total_price > 100:
    discounted_price = total_price * DISCOUNT
    new_amount = total_price - discounted_price
    print(f"The total sum of {number_of_items} items is: ${new_amount:.2f}")
else:
    print(f"The total sum of {number_of_items} items is: ${total_price:.2f}")
