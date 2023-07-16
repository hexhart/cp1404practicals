"""
CP1404/CP5632 - Practical
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
By Hexon Hartley Jimenez
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.10
        print(f"Your total sales of ${sales:.2f} has a 10% bonus of ${bonus:.2f}")
    elif sales >= 1000:
        bonus = sales * 0.15
        print(f"Your total sales of ${sales:.2f} has a 15% bonus of ${bonus:.2f}")
    sales = float(input("Enter sales: $"))
print("You don't have enough sales to qualify for a bonus")
